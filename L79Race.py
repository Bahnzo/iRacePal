#! python3
"""
L79Race.py - a program that tracks the players position and the cars around them.
3 cars ahead, and 3 behind. Will display the players most recent lap time, and the
most recent lap times of those cars around. Will then show the time difference, in
 a plus/minue fashion as well as highlight the background depending on whether the
 player is catching or running away from that car.
"""


'''
position_label:
pos_label_player: the players position in the race
pos_label_p1: drivers around player...thru _p6

name_label_player: players name
name_label_p1: drivers names around player...thru _p6

lap_label: lap time
lap_label_player and lap_label_p1

lap_diff: difference between the player's lap and the opponent's lap time
lap_diff_player - not sure this needs anything
lap_diff_p1-6 if lap is faster, turn number red, green for slower

ir['SessionInfo']['Sessions'][2]['ResultsPositions'] = car data by IDX..ie lap times, etc
'''

import irsdk
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
import race
from time import sleep

#ir = irsdk.IRSDK()
#ir.startup(test_file='data.bin')


class RaceWindow(QMainWindow, race.Ui_RaceWindow):
    def __init__(self, parent=None):
        super(RaceWindow, self).__init__(parent)
        self.setupUi(self)

        #self.frame.setStyleSheet('background-color:grey')
        self.thread = Worker()
        self.thread.name_p4[list].connect(self.display_drivers)
        self.thread.status[str].connect(self.show_status)
        self.thread.start()
        self.quit_button.clicked.connect(self.quit_button_pushed)

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
    def __init__(self, pos, name, laptime, rawlap, is_player):
        self.pos = pos
        self.name = name
        self.laptime = laptime
        self.rawlap = rawlap
        self.is_player = is_player


class Worker(QThread):
    """
    The main thread
    """
    name_p4 = pyqtSignal(list)
    status = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.ir = irsdk.IRSDK()
        #self.ir.startup()
        self.driver_lib = {}  # lib for drivers and their idx
        self.racer_info = []  # a list of the Racer() class which contains the driver info

    def __del__(self):
        self.wait()

    def run(self):
        self.find_sim()

    def find_sim(self):
        while True:
            if self.ir.startup():
                self.status.emit('iRacing Found - Waiting for Session')
                if self.ir['SessionState'] == 4 and self.ir['SessionNum'] == 2:  # 4 = racing
                    self.status.emit('In Race')
                    self.get_drivers()
                    self.DriverCarIdx = self.ir['DriverInfo']['DriverCarIdx']  # the player/driver's carIdx
                    while True:
                        self.ir.freeze_var_buffer_latest()  # freeze input so data doesn't change while doing stuff
                        if self.ir['CarIdxTrackSurface'][self.DriverCarIdx] == 1:  # car in pits
                            self.status.emit('In Race, Car in Pits')
                            break
                        elif self.ir['SessionState'] == 5:
                            self.status.emit('Race over')
                            break
                        else:
                            self.loop()
                            sleep(1)
                else:
                    self.status.emit('Waiting for Race Session')
                    sleep(1)
            else:
                self.status.emit('Looking For iRacing')
                sleep(1)

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
        return idx

    def convert_laptime(self, lap):  # converts lap to min:sec:ms if needed
        if lap >= 60:
            m, s = divmod(lap, 60)  # gets minute, seconds from laptime with divmod()
            #s = round(s, 2)
            x = '{}:{:0.2f}'.format(int(m), s)
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
        total_drivers = len(self.ir['SessionInfo']['Sessions'][2]['ResultsPositions'])
        if self.driver_pos == total_drivers:  # player is in last place
            count = self.driver_pos
            low_limit = self.driver_pos - 6  # low_limit is how low in the placings to get driver positions
        elif self.driver_pos == total_drivers - 1:  # second to last place
            count = self.driver_pos + 1
            low_limit = self.driver_pos - 5
        elif self.driver_pos == total_drivers - 2: #  third from last
            count = self.driver_pos + 2
            low_limit = self.driver_pos - 4
        elif self.driver_pos <= 3:
            count = 7
            low_limit = 1
        else:
            count = self.driver_pos + 3
            low_limit = self.driver_pos - 3

        #count = self.driver_pos + 3
        self.racer_info.clear()
        while count >= low_limit:
            pos = count
            idx = self.get_driver_idx_by_pos(pos, self.car_positions)
            name = self.driver_lib[idx]
            rawlap = self.ir['SessionInfo']['Sessions'][2]['ResultsPositions'][pos - 1]['LastTime']
            if rawlap > 0:  # some backmarkers might not have a lap time
                laptime = self.convert_laptime(rawlap)
            else:
                rawlap = 0.00
                laptime = 0.00
            if idx == self.DriverCarIdx:
                player = True
            else:
                player = False
            car = Racer(pos, name, laptime, rawlap, player)
            self.racer_info.append(car)
            count -= 1

    def loop(self):
        # self.ir.freeze_var_buffer_latest()
        self.car_positions = self.ir['CarIdxClassPosition']  # gets a list of all cars positions
        self.driver_pos = self.car_positions[self.DriverCarIdx]  # this drivers position
        self.get_driver_positions()
        self.display_drivers()

    def display_drivers(self):
        self.name_p4.emit(self.racer_info)



def main():
    app = QApplication(sys.argv)
    window = RaceWindow()
    window.show()
    sys.exit(app.exec_())

logf = open('error.log', 'w')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logf.write(str(e))
