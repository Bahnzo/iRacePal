from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import settingsWindow
import os
import sys
import logging



class setWindow(QMainWindow, settingsWindow.Ui_settingsDialog):
    def __init__(self, parent=None):
        super(setWindow, self).__init__(parent)
        self.setupUi(self)
        data = self.look_for_settings_file()
        if not data:
            self.setup_checkBox.setChecked(False)
        else:
            self.setup_checkBox.setChecked(True)
            self.setup_folder_label.setText(data[0])
        self.setup_checkBox.stateChanged.connect(self.do_checkbox)
        self.ok_button.clicked.connect(self.okButtonClicked)

    def okButtonClicked(self):
        if not self.setup_checkBox.isChecked():  # erase settings.txt
            filename = './settings.txt'
            os.remove(filename)
        self.hide()
        self.close()

    def do_checkbox(self):
        if self.setup_checkBox.isChecked():
            folder = str(QFileDialog.getExistingDirectory(self, 'Select Directory'))
            self.setup_folder_label.setText(folder)
            self.write_to_file(folder)

    def look_for_settings_file(self):
        filename = './settings.txt'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'a+') as f:
            f.seek(0)
            data = f.readlines()
        data = [line.strip('\n') for line in data]
        f.close()
        return data

    def write_to_file(self, folder):
        with open('./settings.txt', 'w') as f:
            f.write(folder)
        f.close()



def main():
    app = QApplication(sys.argv)
    window = setWindow()
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
        logger.error(e)
