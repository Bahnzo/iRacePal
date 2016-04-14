#! python3
# L79ToolsFuel.py - a program to get exact fuel calculations for iRacing

# liter to gallons = L * 0.26417
# 'DriverInfo''DriverCarFuelKgPerLtr' - weight of fuel
# 'DriverCarIdx' - index of driver's car
# FuelLevel - in liters remaining
# FuelUsePerHour - in kg/h
# Speed = meters/second
# LFwearM - wear in percent

# TODO: checkbox for deleting car file

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
import TopWindow
import irsdk
from time import sleep
import math
import re
import os
import logging
import traceback


fuel_used = []  # global for fuel used

class Worker(QThread):
    status = pyqtSignal(str)
    laps = pyqtSignal(str)
    fuel_used_last_lap = pyqtSignal(float)
    avg_fuel_used = pyqtSignal(float)
    weather_type = pyqtSignal(str)
    track_temp = pyqtSignal(str)
    wind_dir = pyqtSignal(str)
    wind_vel = pyqtSignal(str)
    fuel_in_tank = pyqtSignal(str)
    laps_fuel = pyqtSignal(float)
    curr_time = pyqtSignal(str)
    session_left = pyqtSignal(str)
    laps_label = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.ir = irsdk.IRSDK()

    def __del__(self):
        self.wait()

    def look_for_sim(self):
        count = 0
        while True:
            if self.ir.startup():
                self.determine_metric()
                self.status.emit('iRacing found. Waiting for car on track')
                self.get_weather()
                self.set_time()
                self.set_session_time_left()
                self.look_for_car()
            else:
                self.status.emit('Waiting for iRacing: {}'.format(count))
                self.set_time()
                count += 1
                sleep(1)

    def look_for_car(self):
        global fuel_used
        while True:
            self.set_time()
            self.current_stint = 0
            driver = self.ir['DriverInfo']['DriverCarIdx']
            if self.ir['IsOnTrack']:
                self.determine_metric()
                lap_store = False  # set this so we don't use the first lap from pits for fuel calc's
                self.current_lap = self.ir['Lap']
                self.current_stint = 0
                self.lap_switch = 1
                self.show_stint = False
                fuel_store = self.ir['FuelLevel']
                self.laps.emit(str(self.current_lap))
                self.trackname = self.ir['WeekendInfo']['TrackDisplayShortName']
                self.track_config = self.ir['WeekendInfo']['TrackConfigName']
                driver = self.ir['DriverInfo']['DriverCarIdx']
                self.car_type = self.ir['DriverInfo']['Drivers'][driver]['CarPath']
                avg = self.avg_fuel_calculation()
                self.set_session_time_left()
                while True:
                    x = self.ir['CarIdxTrackSurface'][driver]
                    if x == 1:  # if car is in pits, then reset also
                        break
                    if self.ir['IsOnTrack'] == 0:
                        break
                    else:
                        self.status.emit('Driver in car.')
                        self.set_time()
                        self.set_session_time_left()
                        if self.ir['Lap'] > self.current_lap:
                            fpl = fuel_store - self.ir['FuelLevel']
                            if not self.metric:
                                if self.is_car_imp_gal():  # gets car type for Lotus79 or 49
                                    self.fuel_used_last_lap.emit(fpl * 0.21997)  # conv to imp gals
                                else:
                                    self.fuel_used_last_lap.emit(fpl * 0.264)  # gallons
                            else:
                                self.fuel_used_last_lap.emit(fpl)  # liters
                            self.current_lap = self.ir['Lap']
                            self.current_stint += 1
                            self.laps.emit(str(self.current_lap))
                            if not self.metric:
                                if self.is_car_imp_gal():  # gets car type for Lotus79 or 49
                                    self.avg_fuel_used.emit(avg * 0.21997)  # conv to imp gals
                                else:
                                    self.avg_fuel_used.emit(avg * 0.264)  # gallons
                            else:
                                self.avg_fuel_used.emit(avg)
                            weight_of_fuel = self.ir['FuelLevel'] * self.ir['DriverInfo']['DriverCarFuelKgPerLtr']
                            if lap_store:  # don't store data from first lap out of pits
                                if self.average_fuel_limit(avg, fpl) and len(fuel_used) > 5:  #  check that lap usage is within set limits
                                    self.write_lap(fpl, weight_of_fuel)  # write lap data to file
                                    fuel_used.append(fuel_store - self.ir['FuelLevel'])  # fuel use list
                                    data = [float(line) for line in fuel_used]
                                if len(fuel_used) <= 5: #  write anyways, gotta have some data!
                                    self.write_lap(fpl, weight_of_fuel)  # write lap data to file
                                    fuel_used.append(fuel_store - self.ir['FuelLevel'])  # fuel use list
                                    data = [float(line) for line in fuel_used]
                                try:
                                    avg = sum(data) / float(len(data))
                                except ZeroDivisionError:
                                    avg = 0
                            else:
                                lap_store = True
                            fuel_store = self.ir['FuelLevel']
                        if self.ir['WeatherType']:
                            self.get_weather()
                        self.lap_switch += 1
                        self.show_lap_switch()  # changes between total laps, and laps completed since leaving pits
                        self.display_fuel_in_car()
                        self.display_laps_remaining(avg)
                        sleep(0.0016)  # 16ms
            else:
                if self.ir.startup() == 0:
                    break
                self.status.emit('Waiting for Driver in car.')
                self.current_stint = 0
                self.set_time()
                self.set_session_time_left()
                sleep(0.0016)

    def show_lap_switch(self):
        if self.lap_switch > 1000:  # 125 * 16ms = 2 secs, switch every 2 secs
            self.lap_switch = 1
            if self.show_stint:
                self.laps_label.emit('<font color = "red">Laps this Stint</font>')
                self.laps.emit(str(self.current_stint))
                self.show_stint = False
            else:
                self.laps_label.emit('<font color = "black">Total Laps</font>')
                self.laps.emit(str(self.current_lap))
                self.show_stint = True

    def set_session_time_left(self):
        time_left = self.ir['SessionTimeRemain']
        if time_left == 604800:  # this is the time for an unlimited test session
            self.session_left.emit('Unlimited')
        else:
            m, s = divmod(time_left, 60)
            h, m = divmod(m, 60)
            self.session_left.emit('%d:%02d:%02d' % (h, m, s))

    def average_fuel_limit(self, avg_fuel, curr_lap_fuel):
        if curr_lap_fuel < (avg_fuel * .9):  # if current laps fuel usage is not within 90% of the average
            return False
        if curr_lap_fuel > (avg_fuel * 1.1):  # if over 110%...it happens sometimes..
            return False
        else:
            return True

    def is_car_imp_gal(self):
        if self.car_type == 'lotus79':
            return True
        elif self.car_type == 'lotus49':
            return True
        else:
            return False

    def set_time(self):
        dt = QTime.currentTime()
        time = dt.toString('h:mm:ssap')
        self.curr_time.emit(time)

    def determine_metric(self):
        self.metric = self.ir['DisplayUnits']

    def display_laps_remaining(self, avg):
        try:
            if not self.metric:
                if self.is_car_imp_gal():
                    self.laps_fuel.emit((self.ir['FuelLevel'] * 0.21997) / (avg * 0.21997))  # conv imp gallons
                else:
                    self.laps_fuel.emit((self.ir['FuelLevel'] * 0.264) / (avg * 0.264))  # convert gallons
            else:
                self.laps_fuel.emit((self.ir['FuelLevel']) / avg)
        except ZeroDivisionError:
            self.laps_fuel.emit(0.0)

    def avg_fuel_calculation(self):
        global fuel_used
        fuel_used = (self.open_file(self.trackname, self.track_config , self.car_type))
        data = [float(line) for line in fuel_used]
        try:
            avg = sum(data) / float(len(data))
        except ZeroDivisionError:
            avg = 0
        if not self.metric:
            if self.is_car_imp_gal():
                self.avg_fuel_used.emit(avg * 0.21997)  # conv imp gallons
            else:
                self.avg_fuel_used.emit(avg * 0.264)  # conv gallons
        else:
            self.avg_fuel_used.emit(avg)
        return avg

    def open_file(self, track, config, car):
        #lap_regex = re.compile(r'(.+,)')
        filename = './data/{}/{}-{}.txt'.format(car, track, config)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'a+') as f:
            f.seek(0)
            data = f.readlines()
        data = [line.strip('\n') for line in data]
        #data = [m.group(1).rstrip(',') for l in data for m in [lap_regex.search(l)] if m]
        f.close()
        return data

    def write_lap(self, fuel, weight):
        with open('./data/{}/{}-{}.txt'.format(self.car_type, self.trackname, self.track_config), 'a') as f:
            f.write('{}\n'.format(fuel, weight))
        f.close()

    def display_fuel_in_car(self):
        if not self.metric:
            if self.is_car_imp_gal():
                fuel_in_tank = self.ir['FuelLevel'] * 0.21997  # conv to imp gals
            else:
                fuel_in_tank = self.ir['FuelLevel'] * 0.264  # conv gals
        else:
            fuel_in_tank = self.ir['FuelLevel']
        self.fuel_in_tank.emit(str(round(fuel_in_tank, 1)))

    def get_weather(self):
        w_type = self.ir['WeatherType']  # 0=constant, 1=dynamic
        if not self.metric:
            t_temp = round((self.ir['TrackTempCrew'] * 9 / 5) + 32)
        else:
            t_temp = round(self.ir['TrackTempCrew'])
        self.track_temp.emit(str(t_temp))
        degrees = round(math.degrees(self.ir['WindDir']))
        wind_txt = self.winddir_text(degrees)
        self.wind_dir.emit(wind_txt)
        if not self.metric:
            self.wind_vel.emit(str(round(self.ir['WindVel'] / 0.44704)))
        else:
            self.wind_vel.emit(str(round(self.ir['WindVel'])))
        if w_type:
            self.weather_type.emit('Dynamic')
        else:
            self.weather_type.emit('Constant')

    def winddir_text(self, pts):
        "Convert wind direction from 0..15 to compass point text"
        if pts is None:
            return None
        i = int((pts + 11.25)/22.5)
        pts = i % 16
        #pts = int(pts + 0.5) % 16
        winddir_text_array = (('N'),('NNE'),('NE'),('ENE'),('E'),('ESE'),('SE'),('SSE'),('S'),('SSW'),('SW'),('WSW'),('W'),('WNW'),('NW'),('NNW'),)

        return winddir_text_array[pts]

    def run(self):
        self.look_for_sim()


class StartWindow(QMainWindow, TopWindow.Ui_TopWindow):
    global fuel_used

    def __init__(self, parent=None):
        super(StartWindow, self).__init__(parent)
        self.setupUi(self)

        self.version_label.setText('v1.4a')
        self.lcd_palette = self.laps_completed_lcd.palette()
        self.thread = Worker()
        self.thread.status[str].connect(self.set_status)
        self.thread.laps[str].connect(self.set_laps)
        self.thread.laps_label[str].connect(self.set_laps_label)
        self.thread.fuel_used_last_lap[float].connect(self.set_fuel_used_last_lap)
        self.thread.avg_fuel_used[float].connect(self.set_avg_fuel_used)
        self.thread.avg_fuel_used[float].connect(self.set_fuel_needed)
        self.thread.weather_type[str].connect(self.set_weather_type)
        self.thread.track_temp[str].connect(self.set_track_temp)
        self.thread.wind_dir[str].connect(self.set_wind_dir)
        self.thread.wind_vel[str].connect(self.set_wind_vel)
        self.thread.fuel_in_tank[str].connect(self.set_fuel_in_tank)
        self.thread.laps_fuel[float].connect(self.set_fuel_laps_remaining)
        self.thread.curr_time[str].connect(self.set_time)
        self.thread.session_left[str].connect(self.set_session_time)
        self.thread.start()
        self.quit_button.clicked.connect(self.quit_button_pushed)
        self.race_laps.valueChanged.connect(self.set_fuel_needed2)

    def set_laps_label(self, i):
        self.laps_label.setText(i)

    def set_session_time(self, i):
        self.session_label.setText(i)

    def set_time(self, i):
        self.time_label.setText(i)

    def set_fuel_laps_remaining(self, i):
        self.laps_left_lcd.display(i)

    def set_fuel_needed2(self):
        self.fuel_needed_lcd.display(self.race_laps.value() * self.avg_fuel_per_lap_lcd.value())

    def set_fuel_in_tank(self, i):
        self.fuel_in_car_lcd.display(i)

    def set_fuel_needed(self):
        self.fuel_needed_lcd.display(self.race_laps.value() * self.avg_fuel_per_lap_lcd.value())

    def set_wind_vel(self, i):
        self.wind_vel_label.setText(i)

    def set_wind_dir(self, i):
        self.wind_dir_label.setText(i)

    def set_track_temp(self, i):
        self.track_temp_label.setText(i)

    def quit_button_pushed(self):
        self.thread.terminate()
        QCoreApplication.instance().quit()

    def set_status(self, i):
        self.status_label.setText(i)

    def set_laps(self, i):
        self.laps_completed_lcd.display(i)

    def set_fuel_used_last_lap(self, i):
        self.fuel_used_last_lap_lcd.display(i)

    def set_avg_fuel_used(self, i):
        self.avg_fuel_per_lap_lcd.display(i)

    def set_weather_type(self, i):
        self.weather_type_label.setText(i)


def main():
    app = QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec_())

'''
def setup_logging_to_file(filename):
    logging.basicConfig(filename=filename,
                        filemode='w',
                        level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        )


def extract_function_name():
    """Extracts failing function name from Traceback
    by Alex Martelli
    http://stackoverflow.com/questions/2380073/\
    how-to-identify-what-function-call-raise-an-exception-in-python
    """
    tb = sys.exc_info()[-1]
    stk = traceback.extract_tb(tb, 1)
    fname = stk[0][3]
    return fname


def log_exception(e):
    logging.error(
        "Function {function_name} raised {exception_class} ({exception_docstring}): {exception_message}".format(
            function_name=extract_function_name(),  # this is optional
            exception_class=e.__class__,
            exception_docstring=e.__doc__,
            exception_message=e.message))
'''
logf = open('error.log', 'w')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logf.write(str(e))
