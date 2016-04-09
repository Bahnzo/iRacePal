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
'''

import irsdk
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import race

ir = irsdk.IRSDK()
ir.startup(test_file='data.bin')


class RaceWindow(QMainWindow, race.Ui_RaceWindow):
    def __init__(self, parent=None):
        super(RaceWindow, self).__init__(parent)
        self.setupUi(self)

        #self.frame.setStyleSheet('background-color:grey')


class Racer():
    def __init__(self, pos, name, laptime, is_player):
        self.pos = pos
        self.name = name
        self.laptime = laptime
        self.is_player = is_player


def get_driver_idx_by_pos(pos, car_pos):
    for position, item in enumerate(car_pos):
        if item == pos:
            idx = position
            break
    return idx

driver_lib = {}
count = len(ir['DriverInfo']['Drivers']) - 1
while count > 0:
    driver_lib[count] = ir['DriverInfo']['Drivers'][count]['UserName']
    count -= 1

DriverCarIdx = ir['DriverInfo']['DriverCarIdx']
car_positions = ir['CarIdxClassPosition']
driver_pos = car_positions[DriverCarIdx]

if driver_pos >= 4 and driver_pos <= (len(ir['DriverInfo']['Drivers']) - 1) - 3:
    count = driver_pos + 3
    racer_info = []
    while count >= driver_pos - 3:
        pos = count
        idx = get_driver_idx_by_pos(pos, car_positions)
        name = driver_lib[idx]
        laptime = ir['SessionInfo']['Sessions'][2]['ResultsPositions'][pos]['LastTime']
        if idx == DriverCarIdx:
            player = True
        else:
            player = False
        car = Racer(pos, name, laptime, player)
        racer_info.append(car)
        count -= 1
half = ((len(racer_info) - 1) / 2)


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
