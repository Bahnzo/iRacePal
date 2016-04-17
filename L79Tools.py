import firstWindow
import irsdk
#from L79Fuel import FuelWindow
#from L79Race import RaceWindow
import L79Fuel
import L79Race
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from time import sleep
import logging


class FirstWindow(QMainWindow, firstWindow.Ui_WindowOne):
    def __init__(self, parent=None):
        super(FirstWindow, self).__init__(parent)
        self.setupUi(self)

        self.version_label.setText('v0.2')
        self.thread = Worker()
        self.thread.status[str].connect(self.set_status)
        self.thread.race.connect(self.run_race)
        self.thread.progress[int].connect(self.show_progress)
        self.thread.start()
        self.thread.practice.connect(self.run_fuel)

    def show_progress(self, i):
        if self.progressBar.value() == self.progressBar.maximum():
            self.progressBar.reset()
        self.progressBar.setValue(i)

    def set_status(self, i):
        self.status_label.setText(i)

    def run_race(self):
        self.thread.stop()
        self.thread.wait()
        self.thread = None
        self.r_window = L79Race.RaceWindow(self)
        self.r_window.show()
        self.hide()

    def run_fuel(self):  # this is the test
        self.thread.stop()
        self.thread.wait()
        self.thread = None
        self.st_window = L79Fuel.FuelWindow(self)
        self.st_window.show()
        self.hide()


class Worker(QThread):
    status = pyqtSignal(str)
    race = pyqtSignal()
    practice = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.ir = irsdk.IRSDK()
    '''
    def __del__(self):
        self.wait()
    '''
    def stop(self):
        self.terminate()

    def run(self):
        self.look_for_sim()

    def look_for_sim(self):
        count = 0
        while True:
            if self.ir.startup():
                self.status.emit('Iracing Found')
                self.determine_session()
                break
            else:
                count += 1
                self.status.emit('Looking For iRacing')
                self.progress.emit(count)
                if count == 100:
                    count = 0
                sleep(0.050)

    def determine_session(self):
        if self.ir['WeekendInfo']['EventType'] == 'Race':
            self.race.emit()
        elif self.ir['WeekendInfo']['EventType'] == 'Test':
            self.practice.emit()
        elif self.ir['WeekendInfo']['EventType'] == 'Practice':
            self.practice.emit()

def main():
    app = QApplication(sys.argv)
    window = FirstWindow()
    window.show()
    #app.exec_()
    sys.exit(app.exec_())

logging.basicConfig(filename='error.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(e)

