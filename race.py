# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\race.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RaceWindow(object):
    def setupUi(self, RaceWindow):
        RaceWindow.setObjectName("RaceWindow")
        RaceWindow.resize(435, 377)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RaceWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(RaceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.position_frame = QtWidgets.QFrame(self.centralwidget)
        self.position_frame.setGeometry(QtCore.QRect(0, 0, 433, 235))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.position_frame.setFont(font)
        self.position_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.position_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.position_frame.setLineWidth(3)
        self.position_frame.setMidLineWidth(3)
        self.position_frame.setObjectName("position_frame")
        self.label = QtWidgets.QLabel(self.position_frame)
        self.label.setGeometry(QtCore.QRect(10, 6, 31, 16))
        self.label.setObjectName("label")
        self.pos_label_p1 = QtWidgets.QLabel(self.position_frame)
        self.pos_label_p1.setGeometry(QtCore.QRect(8, 28, 31, 16))
        self.pos_label_p1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pos_label_p1.setAlignment(QtCore.Qt.AlignCenter)
        self.pos_label_p1.setObjectName("pos_label_p1")
        self.pos_label_p2 = QtWidgets.QLabel(self.position_frame)
        self.pos_label_p2.setGeometry(QtCore.QRect(8, 53, 31, 16))
        self.pos_label_p2.setAlignment(QtCore.Qt.AlignCenter)
        self.pos_label_p2.setObjectName("pos_label_p2")
        self.pos_label_p3 = QtWidgets.QLabel(self.position_frame)
        self.pos_label_p3.setGeometry(QtCore.QRect(8, 78, 31, 16))
        self.pos_label_p3.setAlignment(QtCore.Qt.AlignCenter)
        self.pos_label_p3.setObjectName("pos_label_p3")
        self.pos_label_p4 = QtWidgets.QLabel(self.position_frame)
        self.pos_label_p4.setGeometry(QtCore.QRect(8, 103, 31, 16))
        self.pos_label_p4.setAlignment(QtCore.Qt.AlignCenter)
        self.pos_label_p4.setObjectName("pos_label_p4")
        self.pos_label_p5 = QtWidgets.QLabel(self.position_frame)
        self.pos_label_p5.setGeometry(QtCore.QRect(8, 128, 31, 16))
        self.pos_label_p5.setAlignment(QtCore.Qt.AlignCenter)
        self.pos_label_p5.setObjectName("pos_label_p5")
        self.pos_label_p6 = QtWidgets.QLabel(self.position_frame)
        self.pos_label_p6.setGeometry(QtCore.QRect(8, 153, 31, 16))
        self.pos_label_p6.setAlignment(QtCore.Qt.AlignCenter)
        self.pos_label_p6.setObjectName("pos_label_p6")
        self.pos_label_p7 = QtWidgets.QLabel(self.position_frame)
        self.pos_label_p7.setGeometry(QtCore.QRect(8, 178, 31, 16))
        self.pos_label_p7.setAlignment(QtCore.Qt.AlignCenter)
        self.pos_label_p7.setObjectName("pos_label_p7")
        self.line = QtWidgets.QFrame(self.position_frame)
        self.line.setGeometry(QtCore.QRect(0, 18, 601, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.position_frame)
        self.line_2.setGeometry(QtCore.QRect(0, 43, 601, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.position_frame)
        self.line_3.setGeometry(QtCore.QRect(0, 68, 601, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.position_frame)
        self.line_4.setGeometry(QtCore.QRect(0, 93, 601, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.position_frame)
        self.line_5.setGeometry(QtCore.QRect(0, 118, 601, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.position_frame)
        self.line_6.setGeometry(QtCore.QRect(0, 143, 601, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_8 = QtWidgets.QFrame(self.position_frame)
        self.line_8.setGeometry(QtCore.QRect(0, 168, 601, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_7 = QtWidgets.QFrame(self.position_frame)
        self.line_7.setGeometry(QtCore.QRect(0, 193, 601, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_9 = QtWidgets.QFrame(self.position_frame)
        self.line_9.setGeometry(QtCore.QRect(33, 25, 20, 175))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_2 = QtWidgets.QLabel(self.position_frame)
        self.label_2.setGeometry(QtCore.QRect(50, 6, 61, 16))
        self.label_2.setObjectName("label_2")
        self.name_label_p1 = QtWidgets.QLabel(self.position_frame)
        self.name_label_p1.setGeometry(QtCore.QRect(48, 24, 181, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_label_p1.setFont(font)
        self.name_label_p1.setObjectName("name_label_p1")
        self.name_label_p2 = QtWidgets.QLabel(self.position_frame)
        self.name_label_p2.setGeometry(QtCore.QRect(48, 49, 181, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_label_p2.setFont(font)
        self.name_label_p2.setObjectName("name_label_p2")
        self.name_label_p3 = QtWidgets.QLabel(self.position_frame)
        self.name_label_p3.setGeometry(QtCore.QRect(48, 74, 181, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_label_p3.setFont(font)
        self.name_label_p3.setObjectName("name_label_p3")
        self.name_label_p4 = QtWidgets.QLabel(self.position_frame)
        self.name_label_p4.setGeometry(QtCore.QRect(48, 99, 181, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_label_p4.setFont(font)
        self.name_label_p4.setObjectName("name_label_p4")
        self.name_label_p5 = QtWidgets.QLabel(self.position_frame)
        self.name_label_p5.setGeometry(QtCore.QRect(48, 124, 181, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_label_p5.setFont(font)
        self.name_label_p5.setObjectName("name_label_p5")
        self.name_label_p6 = QtWidgets.QLabel(self.position_frame)
        self.name_label_p6.setGeometry(QtCore.QRect(48, 149, 181, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_label_p6.setFont(font)
        self.name_label_p6.setObjectName("name_label_p6")
        self.name_label_p7 = QtWidgets.QLabel(self.position_frame)
        self.name_label_p7.setGeometry(QtCore.QRect(48, 174, 181, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_label_p7.setFont(font)
        self.name_label_p7.setObjectName("name_label_p7")
        self.line_10 = QtWidgets.QFrame(self.position_frame)
        self.line_10.setGeometry(QtCore.QRect(216, 25, 20, 175))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label_10 = QtWidgets.QLabel(self.position_frame)
        self.label_10.setGeometry(QtCore.QRect(234, 0, 79, 25))
        self.label_10.setObjectName("label_10")
        self.lap_label_p1 = QtWidgets.QLabel(self.position_frame)
        self.lap_label_p1.setGeometry(QtCore.QRect(234, 30, 61, 16))
        self.lap_label_p1.setAlignment(QtCore.Qt.AlignCenter)
        self.lap_label_p1.setObjectName("lap_label_p1")
        self.line_11 = QtWidgets.QFrame(self.position_frame)
        self.line_11.setGeometry(QtCore.QRect(288, 25, 20, 175))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_12 = QtWidgets.QLabel(self.position_frame)
        self.label_12.setGeometry(QtCore.QRect(312, 0, 37, 25))
        self.label_12.setObjectName("label_12")
        self.lap_diff_p1 = QtWidgets.QLabel(self.position_frame)
        self.lap_diff_p1.setGeometry(QtCore.QRect(306, 28, 67, 19))
        self.lap_diff_p1.setToolTipDuration(0)
        self.lap_diff_p1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lap_diff_p1.setObjectName("lap_diff_p1")
        self.lap_label_p2 = QtWidgets.QLabel(self.position_frame)
        self.lap_label_p2.setGeometry(QtCore.QRect(234, 55, 61, 16))
        self.lap_label_p2.setAlignment(QtCore.Qt.AlignCenter)
        self.lap_label_p2.setObjectName("lap_label_p2")
        self.lap_label_p3 = QtWidgets.QLabel(self.position_frame)
        self.lap_label_p3.setGeometry(QtCore.QRect(234, 80, 61, 16))
        self.lap_label_p3.setAlignment(QtCore.Qt.AlignCenter)
        self.lap_label_p3.setObjectName("lap_label_p3")
        self.lap_label_p4 = QtWidgets.QLabel(self.position_frame)
        self.lap_label_p4.setGeometry(QtCore.QRect(234, 105, 61, 16))
        self.lap_label_p4.setAlignment(QtCore.Qt.AlignCenter)
        self.lap_label_p4.setObjectName("lap_label_p4")
        self.lap_label_p5 = QtWidgets.QLabel(self.position_frame)
        self.lap_label_p5.setGeometry(QtCore.QRect(234, 130, 61, 16))
        self.lap_label_p5.setAlignment(QtCore.Qt.AlignCenter)
        self.lap_label_p5.setObjectName("lap_label_p5")
        self.lap_label_p6 = QtWidgets.QLabel(self.position_frame)
        self.lap_label_p6.setGeometry(QtCore.QRect(234, 155, 61, 16))
        self.lap_label_p6.setAlignment(QtCore.Qt.AlignCenter)
        self.lap_label_p6.setObjectName("lap_label_p6")
        self.lap_label_p7 = QtWidgets.QLabel(self.position_frame)
        self.lap_label_p7.setGeometry(QtCore.QRect(234, 180, 61, 16))
        self.lap_label_p7.setAlignment(QtCore.Qt.AlignCenter)
        self.lap_label_p7.setObjectName("lap_label_p7")
        self.lap_diff_p2 = QtWidgets.QLabel(self.position_frame)
        self.lap_diff_p2.setGeometry(QtCore.QRect(306, 53, 67, 19))
        self.lap_diff_p2.setToolTipDuration(0)
        self.lap_diff_p2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lap_diff_p2.setObjectName("lap_diff_p2")
        self.lap_diff_p3 = QtWidgets.QLabel(self.position_frame)
        self.lap_diff_p3.setGeometry(QtCore.QRect(306, 78, 67, 19))
        self.lap_diff_p3.setToolTipDuration(0)
        self.lap_diff_p3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lap_diff_p3.setObjectName("lap_diff_p3")
        self.lap_diff_p4 = QtWidgets.QLabel(self.position_frame)
        self.lap_diff_p4.setGeometry(QtCore.QRect(306, 103, 67, 19))
        self.lap_diff_p4.setToolTipDuration(0)
        self.lap_diff_p4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lap_diff_p4.setObjectName("lap_diff_p4")
        self.lap_diff_p5 = QtWidgets.QLabel(self.position_frame)
        self.lap_diff_p5.setGeometry(QtCore.QRect(306, 128, 67, 19))
        self.lap_diff_p5.setToolTipDuration(0)
        self.lap_diff_p5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lap_diff_p5.setObjectName("lap_diff_p5")
        self.lap_diff_p6 = QtWidgets.QLabel(self.position_frame)
        self.lap_diff_p6.setGeometry(QtCore.QRect(306, 153, 67, 19))
        self.lap_diff_p6.setToolTipDuration(0)
        self.lap_diff_p6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lap_diff_p6.setObjectName("lap_diff_p6")
        self.lap_diff_p7 = QtWidgets.QLabel(self.position_frame)
        self.lap_diff_p7.setGeometry(QtCore.QRect(306, 178, 67, 19))
        self.lap_diff_p7.setToolTipDuration(0)
        self.lap_diff_p7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lap_diff_p7.setObjectName("lap_diff_p7")
        self.status_label = QtWidgets.QLabel(self.position_frame)
        self.status_label.setGeometry(QtCore.QRect(6, 204, 337, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.status_label.setFont(font)
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.label_7 = QtWidgets.QLabel(self.position_frame)
        self.label_7.setGeometry(QtCore.QRect(372, 0, 37, 25))
        self.label_7.setObjectName("label_7")
        self.line_12 = QtWidgets.QFrame(self.position_frame)
        self.line_12.setGeometry(QtCore.QRect(360, 25, 13, 175))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.lap_complete_label_p1 = QtWidgets.QLabel(self.position_frame)
        self.lap_complete_label_p1.setGeometry(QtCore.QRect(372, 28, 37, 19))
        self.lap_complete_label_p1.setObjectName("lap_complete_label_p1")
        self.lap_complete_label_p2 = QtWidgets.QLabel(self.position_frame)
        self.lap_complete_label_p2.setGeometry(QtCore.QRect(372, 53, 37, 19))
        self.lap_complete_label_p2.setObjectName("lap_complete_label_p2")
        self.lap_complete_label_p3 = QtWidgets.QLabel(self.position_frame)
        self.lap_complete_label_p3.setGeometry(QtCore.QRect(372, 78, 37, 19))
        self.lap_complete_label_p3.setObjectName("lap_complete_label_p3")
        self.lap_complete_label_p4 = QtWidgets.QLabel(self.position_frame)
        self.lap_complete_label_p4.setGeometry(QtCore.QRect(372, 103, 37, 19))
        self.lap_complete_label_p4.setObjectName("lap_complete_label_p4")
        self.lap_complete_label_p5 = QtWidgets.QLabel(self.position_frame)
        self.lap_complete_label_p5.setGeometry(QtCore.QRect(372, 128, 37, 19))
        self.lap_complete_label_p5.setObjectName("lap_complete_label_p5")
        self.lap_complete_label_p6 = QtWidgets.QLabel(self.position_frame)
        self.lap_complete_label_p6.setGeometry(QtCore.QRect(372, 153, 37, 19))
        self.lap_complete_label_p6.setObjectName("lap_complete_label_p6")
        self.lap_complete_label_p7 = QtWidgets.QLabel(self.position_frame)
        self.lap_complete_label_p7.setGeometry(QtCore.QRect(372, 178, 37, 19))
        self.lap_complete_label_p7.setObjectName("lap_complete_label_p7")
        self.time_label = QtWidgets.QLabel(self.position_frame)
        self.time_label.setGeometry(QtCore.QRect(348, 204, 85, 25))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.weather_frame = QtWidgets.QFrame(self.centralwidget)
        self.weather_frame.setGeometry(QtCore.QRect(0, 234, 433, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.weather_frame.setFont(font)
        self.weather_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.weather_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.weather_frame.setObjectName("weather_frame")
        self.label_3 = QtWidgets.QLabel(self.weather_frame)
        self.label_3.setGeometry(QtCore.QRect(10, 8, 55, 19))
        self.label_3.setObjectName("label_3")
        self.w_type_label = QtWidgets.QLabel(self.weather_frame)
        self.w_type_label.setGeometry(QtCore.QRect(72, 8, 57, 19))
        self.w_type_label.setObjectName("w_type_label")
        self.label_4 = QtWidgets.QLabel(self.weather_frame)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 56, 19))
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setObjectName("label_4")
        self.w_dir_label = QtWidgets.QLabel(self.weather_frame)
        self.w_dir_label.setGeometry(QtCore.QRect(72, 30, 57, 19))
        self.w_dir_label.setObjectName("w_dir_label")
        self.label_5 = QtWidgets.QLabel(self.weather_frame)
        self.label_5.setGeometry(QtCore.QRect(138, 30, 76, 19))
        self.label_5.setObjectName("label_5")
        self.w_speed_label = QtWidgets.QLabel(self.weather_frame)
        self.w_speed_label.setGeometry(QtCore.QRect(222, 30, 25, 19))
        self.w_speed_label.setObjectName("w_speed_label")
        self.label_6 = QtWidgets.QLabel(self.weather_frame)
        self.label_6.setGeometry(QtCore.QRect(138, 8, 73, 19))
        self.label_6.setObjectName("label_6")
        self.w_temp_label = QtWidgets.QLabel(self.weather_frame)
        self.w_temp_label.setGeometry(QtCore.QRect(216, 8, 37, 19))
        self.w_temp_label.setObjectName("w_temp_label")
        self.label_8 = QtWidgets.QLabel(self.weather_frame)
        self.label_8.setGeometry(QtCore.QRect(258, 30, 67, 19))
        self.label_8.setObjectName("label_8")
        self.race_dist_label = QtWidgets.QLabel(self.weather_frame)
        self.race_dist_label.setGeometry(QtCore.QRect(324, 30, 49, 19))
        self.race_dist_label.setObjectName("race_dist_label")
        self.label_9 = QtWidgets.QLabel(self.weather_frame)
        self.label_9.setGeometry(QtCore.QRect(258, 8, 43, 19))
        self.label_9.setObjectName("label_9")
        self.sky_type_label = QtWidgets.QLabel(self.weather_frame)
        self.sky_type_label.setGeometry(QtCore.QRect(300, 8, 91, 19))
        self.sky_type_label.setObjectName("sky_type_label")
        self.version_label = QtWidgets.QLabel(self.weather_frame)
        self.version_label.setGeometry(QtCore.QRect(402, 0, 25, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.version_label.setFont(font)
        self.version_label.setObjectName("version_label")
        self.fuel_frame = QtWidgets.QFrame(self.centralwidget)
        self.fuel_frame.setGeometry(QtCore.QRect(0, 294, 433, 80))
        self.fuel_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fuel_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fuel_frame.setObjectName("fuel_frame")
        self.laps_left_lcd = QtWidgets.QLCDNumber(self.fuel_frame)
        self.laps_left_lcd.setGeometry(QtCore.QRect(294, 24, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.laps_left_lcd.setFont(font)
        self.laps_left_lcd.setAutoFillBackground(False)
        self.laps_left_lcd.setProperty("intValue", 0)
        self.laps_left_lcd.setObjectName("laps_left_lcd")
        self.label_13 = QtWidgets.QLabel(self.fuel_frame)
        self.label_13.setGeometry(QtCore.QRect(162, 0, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.laps_empty_lcd = QtWidgets.QLCDNumber(self.fuel_frame)
        self.laps_empty_lcd.setGeometry(QtCore.QRect(156, 24, 131, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.laps_empty_lcd.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.laps_empty_lcd.setFont(font)
        self.laps_empty_lcd.setSmallDecimalPoint(False)
        self.laps_empty_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.laps_empty_lcd.setProperty("value", 0.0)
        self.laps_empty_lcd.setProperty("intValue", 0)
        self.laps_empty_lcd.setObjectName("laps_empty_lcd")
        self.label_11 = QtWidgets.QLabel(self.fuel_frame)
        self.label_11.setGeometry(QtCore.QRect(318, 0, 97, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.fuel_needed_lcd = QtWidgets.QLCDNumber(self.fuel_frame)
        self.fuel_needed_lcd.setGeometry(QtCore.QRect(18, 24, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.fuel_needed_lcd.setFont(font)
        self.fuel_needed_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.fuel_needed_lcd.setObjectName("fuel_needed_lcd")
        self.label_14 = QtWidgets.QLabel(self.fuel_frame)
        self.label_14.setGeometry(QtCore.QRect(36, 0, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        RaceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RaceWindow)
        QtCore.QMetaObject.connectSlotsByName(RaceWindow)

    def retranslateUi(self, RaceWindow):
        _translate = QtCore.QCoreApplication.translate
        RaceWindow.setWindowTitle(_translate("RaceWindow", "RaceWindow"))
        self.label.setText(_translate("RaceWindow", "POS"))
        self.pos_label_p1.setText(_translate("RaceWindow", "1"))
        self.pos_label_p2.setText(_translate("RaceWindow", "2"))
        self.pos_label_p3.setText(_translate("RaceWindow", "3"))
        self.pos_label_p4.setText(_translate("RaceWindow", "4"))
        self.pos_label_p5.setText(_translate("RaceWindow", "5"))
        self.pos_label_p6.setText(_translate("RaceWindow", "6"))
        self.pos_label_p7.setText(_translate("RaceWindow", "7"))
        self.label_2.setText(_translate("RaceWindow", "Name"))
        self.name_label_p1.setText(_translate("RaceWindow", "-----------------------------"))
        self.name_label_p2.setText(_translate("RaceWindow", "-----------------------------"))
        self.name_label_p3.setText(_translate("RaceWindow", "-----------------------------"))
        self.name_label_p4.setText(_translate("RaceWindow", "-----------------------------"))
        self.name_label_p5.setText(_translate("RaceWindow", "-----------------------------"))
        self.name_label_p6.setText(_translate("RaceWindow", "-----------------------------"))
        self.name_label_p7.setText(_translate("RaceWindow", "-----------------------------"))
        self.label_10.setText(_translate("RaceWindow", "Last Lap"))
        self.lap_label_p1.setText(_translate("RaceWindow", "0:00.00"))
        self.label_12.setText(_translate("RaceWindow", "Diff"))
        self.lap_diff_p1.setText(_translate("RaceWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">+0.32</span></p></body></html>"))
        self.lap_label_p2.setText(_translate("RaceWindow", "0:00.00"))
        self.lap_label_p3.setText(_translate("RaceWindow", "0:00.00"))
        self.lap_label_p4.setText(_translate("RaceWindow", "0:00.00"))
        self.lap_label_p5.setText(_translate("RaceWindow", "0:00.00"))
        self.lap_label_p6.setText(_translate("RaceWindow", "0:00.00"))
        self.lap_label_p7.setText(_translate("RaceWindow", "0:00.00"))
        self.lap_diff_p2.setText(_translate("RaceWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">+0.32</span></p></body></html>"))
        self.lap_diff_p3.setText(_translate("RaceWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">+0.32</span></p></body></html>"))
        self.lap_diff_p4.setText(_translate("RaceWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">+0.32</span></p></body></html>"))
        self.lap_diff_p5.setText(_translate("RaceWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">+0.32</span></p></body></html>"))
        self.lap_diff_p6.setText(_translate("RaceWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">+0.32</span></p></body></html>"))
        self.lap_diff_p7.setText(_translate("RaceWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">+0.32</span></p></body></html>"))
        self.label_7.setText(_translate("RaceWindow", "Lap"))
        self.lap_complete_label_p1.setText(_translate("RaceWindow", "10"))
        self.lap_complete_label_p2.setText(_translate("RaceWindow", "10"))
        self.lap_complete_label_p3.setText(_translate("RaceWindow", "10"))
        self.lap_complete_label_p4.setText(_translate("RaceWindow", "10"))
        self.lap_complete_label_p5.setText(_translate("RaceWindow", "10"))
        self.lap_complete_label_p6.setText(_translate("RaceWindow", "10"))
        self.lap_complete_label_p7.setText(_translate("RaceWindow", "10"))
        self.time_label.setText(_translate("RaceWindow", "10:00:01 pm"))
        self.label_3.setText(_translate("RaceWindow", "Weather:"))
        self.w_type_label.setText(_translate("RaceWindow", "TextLabel"))
        self.label_4.setText(_translate("RaceWindow", "Wind Dir:"))
        self.w_dir_label.setText(_translate("RaceWindow", "TextLabel"))
        self.label_5.setText(_translate("RaceWindow", "Wind Speed:"))
        self.w_speed_label.setText(_translate("RaceWindow", "0"))
        self.label_6.setText(_translate("RaceWindow", "Track Temp:"))
        self.w_temp_label.setText(_translate("RaceWindow", "0"))
        self.label_8.setText(_translate("RaceWindow", "Race Dist:"))
        self.race_dist_label.setText(_translate("RaceWindow", "0"))
        self.label_9.setText(_translate("RaceWindow", "Skies:"))
        self.sky_type_label.setText(_translate("RaceWindow", "Cloudy"))
        self.version_label.setText(_translate("RaceWindow", "v0.1"))
        self.label_13.setText(_translate("RaceWindow", "Laps Until Empty"))
        self.label_11.setText(_translate("RaceWindow", "Laps Remain"))
        self.label_14.setText(_translate("RaceWindow", "Fuel to Finish"))

