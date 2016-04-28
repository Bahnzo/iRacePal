#! python3
"""
L79Race.py - a program that tracks the players position and the cars around them.
3 cars ahead, and 3 behind. Will display the players most recent lap time, and the
most recent lap times of those cars around. Will then show the time difference, in
 a plus/minue fashion as well as highlight the background depending on whether the
 player is catching or running away from that car.
"""


'''
TODO: fuel calculations. Do an average over a 3 lap span, throwing out odd readings (ie: first lap, pace laps)
TODO: color backgrounds based on fuel calculations?
HTML color codes:
GREENS:
#ccffdd - very light green....black text
#66ff99 - light green
#0099cc - green
REDS:
#ffccc - light red...black text
#ff8080 - red
#ff1a1a - dark red..black text ok...maybe white

ir['SessionInfo']['Sessions'][2]['ResultsPositions'] = car data by IDX..ie lap times, etc
'''
import irsdk
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
import race
import race2
import L79Tools
from time import sleep
import math
import os
import logging

logging.basicConfig(filename='error.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

large = race.Ui_RaceWindow
small = race2.Ui_raceSmall
window_size = large

class RaceWindow(QMainWindow, window_size):
    def __init__(self, parent=None):
        super(RaceWindow, self).__init__(parent)
        self.setupUi(self)

        self.ok_button.hide()
        #self.frame.setStyleSheet('background-color:grey')
        self.version_label.setText('v0.4')
        self.thread = Worker()
        self.thread.name_p4[list].connect(self.display_drivers)
        self.thread.status[str].connect(self.show_status)
        self.thread.weather[object].connect(self.show_weather)
        self.thread.curr_time[str].connect(self.show_time)
        self.thread.laps2go[int].connect(self.show_laps_remaining)
        self.thread.laps_fuel[list].connect(self.show_fuel_laps_remaining)
        #self.thread.ok.connect(self.race_done)
        self.thread.race_over.connect(self.show_ok_button)
        self.thread.start()
        self.ok_button.clicked.connect(self.race_done)

    def show_ok_button(self):
        self.ok_button.show()

    def race_done(self):
        self.thread.stop()
        self.thread.wait()
        self.r_window = L79Tools.FirstWindow(self)
        self.r_window.show()
        self.hide()
    '''
    def closeEvent(self, event):
        self.thread.stop()
        self.thread.wait()
    '''
    def show_fuel_laps_remaining(self, i):
        self.laps_empty_lcd.display(i[0])
        self.laps_empty_lcd.setStyleSheet('background-color: {}'.format(i[1]))

    def show_laps_remaining(self, i):
        self.laps_left_lcd.display(i)

    def show_time(self, i):
        self.time_label.setText(i)

    def show_weather(self, i):
        self.w_type_label.setText(i.w_type)
        self.w_dir_label.setText(i.wind_dir)
        self.w_speed_label.setText(i.wind_vel)
        self.w_temp_label.setText(i.track_temp)
        self.sky_type_label.setText(i.skies)
        self.race_dist_label.setText(i.race_dist)

    def quit_button_pushed(self):
        self.thread.terminate()
        QCoreApplication.instance().quit()

    def show_status(self, i):
        self.status_label.setText(i)

    def display_drivers(self, i):  # i = list of driver info?
        count = 1
        player_lap = self.get_player_lap(i)
        for driver in reversed(i):
            str1 = 'pos_label_p{}'.format(count)
            func1 = getattr(self, str1, None)
            func1.setText(str(driver.pos))
            str1 = 'name_label_p{}'.format(count)
            func1 = getattr(self, str1, None)
            func1.setText(self.calc_driver_color(player_lap, round(driver.rawlap, 2), driver.name, driver.is_player))
            str1 = 'lap_label_p{}'.format(count)
            func1 = getattr(self, str1, None)
            func1.setText(str(driver.laptime))
            str1 = 'lap_diff_p{}'.format(count)
            func1 = getattr(self, str1, None)
            lap_diff = self.calc_lap_diff(player_lap, round(driver.rawlap, 2))
            func1.setText(str(lap_diff))
            str1 = 'lap_complete_label_p{}'.format(count)
            func1 = getattr(self, str1, None)
            func1.setText(str(driver.cur_lap))
            count += 1

    def calc_lap_diff(self, player_lap, driver_lap):
        diff = driver_lap - player_lap
        if diff == 0.0:
            return '<font color = "black">{}</font>'.format('--:--')
        elif diff >= 0:  # player is faster than driver we compare to
            return '<font color = "green">{}{:0.2f}</font>'.format('+', diff)
        else:  # driver's lap is faster than player's lap.
            return '<font color = "red">{:0.2f}</font>'.format(diff)

    def calc_driver_color(self, player_lap, driver_lap, name, is_player):
        diff = driver_lap - player_lap
        if is_player:
            return '<font color = "black">{}{}{}</font>'.format('+++', name, '+++')
        elif diff > 0:
            return '<font color = "green">{}</font>'.format(name)
        else:
            return '<font color = "red">{}</font>'.format(name)

    def get_player_lap(self, i):
        for driver in i:
            if driver.is_player:
                return round(driver.rawlap, 2)


class Racer():
    """
    Stores info about each driver to be displayed
    """
    def __init__(self, pos, name, laptime, rawlap, is_player, cur_lap, car_type, car_classID):
        self.pos = pos
        self.name = name
        self.laptime = laptime
        self.rawlap = rawlap
        self.is_player = is_player
        self.cur_lap = cur_lap
        self.car_type = car_type
        self.car_classID = car_classID


class TrackInfo():
    """
    Holds info about the weather.
    """
    def __init__(self, track_temp, wind_dir, wind_vel, w_type, skies, race_dist):
        self.track_temp = track_temp
        self.wind_dir = wind_dir
        self.wind_vel = wind_vel
        self.w_type = w_type
        self.skies = skies
        self.race_dist = race_dist


class Worker(QThread):
    """
    The main thread
    """
    name_p4 = pyqtSignal(list)
    status = pyqtSignal(str)
    track_temp = pyqtSignal(str)
    weather = pyqtSignal(object)
    tire_temps = pyqtSignal(object)
    curr_time = pyqtSignal(str)
    laps2go = pyqtSignal(int)
    laps_fuel = pyqtSignal(list)
    race_over = pyqtSignal()
    #ok = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ir = irsdk.IRSDK()
        self.driver_lib = {}  # lib for drivers and their idx
        self.racer_info = []  # a list of the Racer() class which contains the driver info
        self.avg_fuel_list = []  # list of drivers avg fuel use
        self.avgfuellaps = 5  # num of laps to average fuel over

    def __del__(self):
        self.wait()

    def run(self):
        self.find_sim()

    def stop(self):
        self.terminate()
        self.ir.shutdown()

    def find_sim(self):
        while True:
            if self.ir.startup():
                self.get_race_details()
                self.get_weather()
                self.set_time()
                #self.status.emit('iRacing Found - Waiting for Session')
                self.determine_session()  # discover session type
            else:
                self.status.emit('Looking For iRacing')
                self.set_time()
                sleep(1)

    def determine_session(self):
        if self.ir['SessionState'] == 4 and self.ir['SessionNum'] == 2:  # 4 = racing 2 = race session
            self.green_flag_race()
        elif self.ir['SessionState'] == 3:  # parade laps
            self.status.emit('Warmup Laps')
            sleep(0.0016)
        #elif self.ir['SessionState'] == 5 and self.ir['SessionNum'] == 2:
        #    self.ir.shutdown()
        #    self.race_over.emit()
        else:
            self.status.emit('Waiting for Race Session')
            sleep(1)

    def green_flag_race(self):
        self.current_lap = self.ir['Lap']
        self.get_race_details()
        self.get_weather()
        self.get_drivers()
        self.car_type_long = self.ir['DriverInfo']['Drivers'][self.DriverCarIdx]['CarPath']
        self.fuel_store = self.ir['FuelLevel']
        self.DriverCarIdx = self.ir['DriverInfo']['DriverCarIdx']  # the player/driver's carIdx
        self.is_imp()  # if car uses IMP gallons or not
        while True:
            self.status.emit('In Race')
            self.current_lap = self.ir['Lap']
            if self.ir.startup() == 0:
                break
            try:  # attempt at an error catching loop
                self.ir.freeze_var_buffer_latest()  # freeze input so data doesn't change while doing stuff
                if self.ir['CarIdxTrackSurface'][self.DriverCarIdx] == 1:  # car in pits
                    self.status.emit('In Race, Car in Pits')
                    self.set_time()
                    self.avg_fuel_list = []
                    sleep(1)
                elif self.ir['SessionState'] == 5:  # look for race over
                #    self.ir.shutdown()
                    self.race_over.emit()
                    break
                else:
                    if self.current_lap > 0:
                        self.loop()  # main loop for getting driver info
                        sleep(0.0016)  # 16ms
            except Exception as e:
                    logging.exception(e)



    def loop(self):  # main loop executed during race
        try:
            #self.car_positions = self.ir['CarIdxClassPosition']  # gets a list of all cars positions by class
            self.car_positions = self.ir['CarIdxPosition']  # gets a list of car positions regardless of class
            self.driver_pos = self.car_positions[self.DriverCarIdx]  # the players position
            self.get_driver_positions()
            self.session_laps_remaining()
            self.get_avg_fuel()
            if self.ir['WeatherType']:
                self.get_weather()
            self.set_time()
            self.display_drivers()
        except Exception as e:
            logging.exception(e)

    def is_imp(self):
        if self.car_type_long == 'lotus79' or 'lotus49':
            return True
        else:
            return False

    def session_laps_remaining(self):
        self.laps_remaining = self.ir['SessionLapsRemainEx']
        self.laps2go.emit(self.laps_remaining)

    def set_time(self):
        dt = QTime.currentTime()
        time = dt.toString('h:mm:ssap')
        self.curr_time.emit(time)

    def conv_c(self, temp):  # converts F to C
        x = round((temp * 9 / 5) + 32)
        return str(x)

    def conv_k(self, speed):  # converts kph to mph
        x = speed * 0.6213711922
        return x

    def conv_imp(self, fuel):  # converts liters to imp gallons
        return fuel * 0.21997

    def conv_gal(self, fuel):  # converts liters to gallons
        return fuel * 0.264

    def get_sky_condition(self, skies):
        if skies == 0:
            sky_cond = 'Clear'
        elif skies == 1:
            sky_cond = 'Partly Cloudy'
        elif skies == 2:
            sky_cond = 'Mostly Cloudy'
        else:
            sky_cond = 'Overcast'
        return sky_cond

    def get_race_details(self):
        """
        Gets all sorts of static variables about the session/race for use later
        :return:
        """
        self.DriverCarIdx = self.ir['DriverInfo']['DriverCarIdx']  # the player/driver's carIdx
        self.car_type_long = self.ir['DriverInfo']['Drivers'][self.DriverCarIdx]['CarPath']
        self.is_imp()  # if car uses IMP gallons or not
        self.trackname = self.ir['WeekendInfo']['TrackDisplayShortName']
        self.track_weather = self.ir['WeekendInfo']['TrackWeatherType']  # constant or dynamic
        self.metric = self.ir['DisplayUnits']  # what measurement units is the player using
        if self.ir['WeekendInfo']['EventType'] == 'Race':
            self.race_laps = str(self.ir['SessionInfo']['Sessions'][2]['SessionLaps'])
        else:
            self.race_laps = 'Practice'
        self.sky_cond = self.get_sky_condition(self.ir['WeekendInfo']['WeekendOptions']['Skies'])
        self.num_classes = self.ir['WeekendInfo']['NumCarClasses']
        self.track_config = self.ir['WeekendInfo']['TrackConfigName']
        if self.track_config == None:
            self.track_config = 'None'
        if self.ir['WeekendInfo']['Category'] == 'Road':
            self.race_type = True
            self.avgfuellaps = 3  # use last three laps for avg fuel on road course
        else:
            self.race_type = False
            self.avgfuellaps = 5  # use last 5 laps for avg fuel on oval
        fuel_used = (self.open_file(self.trackname, self.track_config, self.car_type_long))

    def get_weather(self):
        w_type = self.ir['WeatherType']  # 0=constant, 1=dynamic
        if not self.metric:
            t_temp = round((self.ir['TrackTempCrew'] * 9 / 5) + 32)
            track_temp = '{}{}'.format(str(t_temp), 'F')
        else:
            t_temp = round(self.ir['TrackTempCrew'])
            track_temp = '{}{}'.format(str(t_temp), 'C')
        degrees = round(math.degrees(self.ir['WindDir']))
        wind_txt = self.winddir_text(float(degrees))
        wind_dir = wind_txt
        if not self.metric:
            wind_vel = str(round(self.ir['WindVel'] / 0.44704))
        else:
            wind_vel = str(round(self.ir['WindVel']))
        if w_type:
            w_type = 'Dynamic'
        else:
            w_type = 'Constant'
        w = TrackInfo(track_temp, wind_dir, wind_vel, w_type, self.sky_cond, self.race_laps)
        self.weather.emit(w)

    def winddir_text(self, pts):
        "Convert wind direction from 0..15 to compass point text"
        if pts is None:
            return None
        i = int((pts + 11.25)/22.5)
        pts = i % 16
        #pts = int(pts + 0.5) % 16
        winddir_text_array = (('N'),('NNE'),('NE'),('ENE'),('E'),('ESE'),('SE'),('SSE'),('S'),('SSW'),('SW'),('WSW'),('W'),('WNW'),('NW'),('NNW'),)

        return winddir_text_array[pts]

    def get_driver_idx_by_pos(self, pos, car_pos):
        '''
        :param pos: cars pos to get idx for
        :param car_pos: list of cars position in race by carIdx. for example x[1] is carIdx 1's position.
        :return:
        '''
        for Caridx, position in enumerate(car_pos):
            if position == pos:
                idx = Caridx
                break
            else:  # for some reason I can't find, this sometimes doesn't find the idx. In pits?
                idx = 1
        return idx

    def convert_laptime(self, lap):  # converts lap to min:sec:ms if needed
        if lap >= 60:
            m, s = divmod(lap, 60)  # gets minute, seconds from laptime with divmod()
            #s = round(s, 2)
            x = '{}:{:05.2f}'.format(int(m), s)
            return x
        else:
            s = round(lap, 2)
            x = '{}'.format(s)
            return x

    def get_drivers(self):  # gets a lib of all drivers and their idx
        count = len(self.ir['DriverInfo']['Drivers']) - 1
        while count > 0:
            self.driver_lib[count] = self.ir['DriverInfo']['Drivers'][count]['UserName']
            count -= 1

    def get_driver_positions(self):  # this is main function for getting drivers needed for positions
        try:
            total_drivers = len(self.ir['SessionInfo']['Sessions'][2]['ResultsPositions'])
            if self.driver_pos == total_drivers:  # player is in last place
                count = self.driver_pos
                low_limit = self.driver_pos - 6  # low_limit is how low in the placings to get driver positions
                if low_limit <= 0:
                    low_limit = 1
            elif self.driver_pos == total_drivers - 1:  # second to last place
                count = self.driver_pos + 1
                low_limit = self.driver_pos - 5
            elif self.driver_pos == total_drivers - 2: #  third from last
                count = self.driver_pos + 2
                low_limit = self.driver_pos - 4
            elif self.driver_pos <= 3:  # driver is in top 3
                count = 7
                low_limit = 1
            else:
                count = self.driver_pos + 3
                low_limit = self.driver_pos - 3
            self.racer_info.clear()  #  empty list in prep for new drivers
            while count >= low_limit:
                pos = count
                idx = self.get_driver_idx_by_pos(pos, self.car_positions)
                name = self.driver_lib[idx]
                rawlap = self.ir['SessionInfo']['Sessions'][2]['ResultsPositions'][pos - 1]['LastTime']
                if rawlap > 0:  # some backmarkers might not have a lap time because they in garage
                    laptime = self.convert_laptime(rawlap)
                else:
                    rawlap = 0.00
                    laptime = 0.00
                if idx == self.DriverCarIdx:
                    player = True
                else:
                    player = False
                car_type = self.ir['DriverInfo']['Drivers'][idx]['CarScreenNameShort']
                cur_lap = self.ir['SessionInfo']['Sessions'][2]['ResultsPositions'][pos - 1]['LapsComplete']
                classID = self.ir['DriverInfo']['Drivers'][idx]['CarClassID']
                car = Racer(pos, name, laptime, rawlap, player, cur_lap, car_type, classID)
                self.racer_info.append(car)
                count -= 1
        except TypeError:
            pass

    def display_drivers(self):
        self.name_p4.emit(self.racer_info)

    def get_avg_fuel(self):
        if self.ir['Lap'] > self.current_lap:  # do fuel average
            count = 0
            fuel_hold = 0
            fpl = self.fuel_store - self.ir['FuelLevel']
            self.write_lap(fpl)
            self.avg_fuel_list.append(fpl)
            #logging.warning('{}'.format(self.avg_fuel_list))
            self.current_lap = self.ir['Lap']  # reset current lap fuel
            #self.avg_fuel = mean(self.avg_fuel_list)
            if len(self.avg_fuel_list) >= self.avgfuellaps:
                for fuel in reversed(self.avg_fuel_list):
                    fuel_hold += fuel
                    count += 1
                    if count == self.avgfuellaps:
                        break
                self.avg_fuel = fuel_hold / self.avgfuellaps
                self.display_laps_remaining()
            else:
                self.avg_fuel = self.avg_fuel_calculation()
                self.display_laps_remaining()
            self.fuel_store = self.ir['FuelLevel']

    def get_fuel_laps_color(self, laps):
        if laps > self.laps_remaining:
            return 'green'
        else:
            return 'red'

    def avg_fuel_calculation(self):
            fuel_used = (self.open_file(self.trackname, self.track_config, self.car_type_long))
            data = [float(line) for line in fuel_used]
            try:
                avg = sum(data) / float(len(data))
            except ZeroDivisionError:
                avg = 0
            return avg

    def display_laps_remaining(self):
        y = []
        try:
            if not self.metric:
                if self.is_imp():
                    laps_remain = ((self.ir['FuelLevel'] * 0.21997) / (self.avg_fuel * 0.21997))  # conv imp gallons
                else:
                    laps_remain = ((self.ir['FuelLevel'] * 0.264) / (self.avg_fuel * 0.264))  # convert gallons
            else:
                laps_remain = ((self.ir['FuelLevel']) / self.avg_fuel)
        except ZeroDivisionError:
            laps_remain = 0.0
        x = self.get_fuel_laps_color(laps_remain)
        y.append(laps_remain)
        y.append(x)
        self.laps_fuel.emit(y)

    def open_file(self, track, config, car):
        filename = './data/{}/{}-{}.txt'.format(car, track, config)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'a+') as f:
            f.seek(0)
            data = f.readlines()
        data = [line.strip('\n') for line in data]
        f.close()
        return data

    def write_lap(self, fuel):
        with open('./data/{}/{}-{}.txt'.format(self.car_type_long, self.trackname, self.track_config), 'a') as f:
            f.write('{}\n'.format(fuel))
        f.close()


def main():
    app = QApplication(sys.argv)
    window = RaceWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(e)
