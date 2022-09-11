# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 630)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icons/exam_creator.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QToolTip\n"
"{\n"
"     border: 2px solid #fff;\n"
"     background-color: #ffa02f;\n"
"    color:#222;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 1000;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    background-color: silver;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 1px solid darkgray;*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/dark_orange/img/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"    border: 1px solid darkgray;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/dark_orange/img/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/dark_orange/img/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid darkgray;\n"
"\n"
"    border-radius: 2px;\n"
"    min-width: 50px;\n"
"}")
        MainWindow.setWindowFilePath("")
        MainWindow.setIconSize(QtCore.QSize(16, 16))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_exam_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_exam_btn.setGeometry(QtCore.QRect(140, 0, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.open_exam_btn.setFont(font)
        self.open_exam_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\icons/open.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_exam_btn.setIcon(icon1)
        self.open_exam_btn.setIconSize(QtCore.QSize(36, 36))
        self.open_exam_btn.setObjectName("open_exam_btn")
        self.New_exam_btn = QtWidgets.QPushButton(self.centralwidget)
        self.New_exam_btn.setGeometry(QtCore.QRect(230, 0, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.New_exam_btn.setFont(font)
        self.New_exam_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.New_exam_btn.setIcon(icon2)
        self.New_exam_btn.setIconSize(QtCore.QSize(36, 36))
        self.New_exam_btn.setObjectName("New_exam_btn")
        self.add_question_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_question_btn.setGeometry(QtCore.QRect(320, 0, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.add_question_btn.setFont(font)
        self.add_question_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\icons/adding.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_question_btn.setIcon(icon3)
        self.add_question_btn.setIconSize(QtCore.QSize(36, 36))
        self.add_question_btn.setObjectName("add_question_btn")
        self.export_btn = QtWidgets.QPushButton(self.centralwidget)
        self.export_btn.setGeometry(QtCore.QRect(410, 0, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.export_btn.setFont(font)
        self.export_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\icons/export.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_btn.setIcon(icon4)
        self.export_btn.setIconSize(QtCore.QSize(36, 36))
        self.export_btn.setObjectName("export_btn")
        self.setting_btn = QtWidgets.QPushButton(self.centralwidget)
        self.setting_btn.setGeometry(QtCore.QRect(500, 0, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.setting_btn.setFont(font)
        self.setting_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\icons/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_btn.setIcon(icon5)
        self.setting_btn.setIconSize(QtCore.QSize(36, 36))
        self.setting_btn.setObjectName("setting_btn")
        self.about_btn = QtWidgets.QPushButton(self.centralwidget)
        self.about_btn.setGeometry(QtCore.QRect(590, 0, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.about_btn.setFont(font)
        self.about_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.about_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\icons/about.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_btn.setIcon(icon6)
        self.about_btn.setIconSize(QtCore.QSize(36, 36))
        self.about_btn.setObjectName("about_btn")
        self.qusetion_textEdit_field = QtWidgets.QTextEdit(self.centralwidget)
        self.qusetion_textEdit_field.setGeometry(QtCore.QRect(300, 140, 421, 101))
        self.qusetion_textEdit_field.setStyleSheet("\n"
"QTextEdit:hover\n"
"{\n"
"    border: 1px solid #ff8c00;\n"
"}\n"
"QTextEdit:focus\n"
"{\n"
"    border: 1px solid #ff8c00;\n"
"\n"
"}")
        self.qusetion_textEdit_field.setObjectName("qusetion_textEdit_field")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 90, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.qusetion_img_lable = QtWidgets.QLabel(self.centralwidget)
        self.qusetion_img_lable.setEnabled(True)
        self.qusetion_img_lable.setGeometry(QtCore.QRect(30, 90, 211, 231))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.qusetion_img_lable.setFont(font)
        self.qusetion_img_lable.setAutoFillBackground(False)
        self.qusetion_img_lable.setStyleSheet("QLabel{\n"
"    border: 1px solid #ff8c00;\n"
"}")
        self.qusetion_img_lable.setFrameShape(QtWidgets.QFrame.Box)
        self.qusetion_img_lable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.qusetion_img_lable.setTextFormat(QtCore.Qt.AutoText)
        self.qusetion_img_lable.setScaledContents(True)
        self.qusetion_img_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.qusetion_img_lable.setWordWrap(True)
        self.qusetion_img_lable.setOpenExternalLinks(False)
        self.qusetion_img_lable.setObjectName("qusetion_img_lable")
        self.add_img_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_img_btn.setGeometry(QtCore.QRect(130, 330, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.add_img_btn.setFont(font)
        self.add_img_btn.setObjectName("add_img_btn")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 260, 421, 58))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_7 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout.addWidget(self.line_7)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(14)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.line_4 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_4.setEnabled(True)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.choose_Rbtn = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(14)
        self.choose_Rbtn.setFont(font)
        self.choose_Rbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.choose_Rbtn.setObjectName("choose_Rbtn")
        self.horizontalLayout.addWidget(self.choose_Rbtn)
        self.line_5 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout.addWidget(self.line_5)
        self.true_or_false_Rbtn = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(14)
        self.true_or_false_Rbtn.setFont(font)
        self.true_or_false_Rbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.true_or_false_Rbtn.setObjectName("true_or_false_Rbtn")
        self.horizontalLayout.addWidget(self.true_or_false_Rbtn)
        self.line_6 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout.addWidget(self.line_6)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.line_8 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout.addWidget(self.line_8)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(300, 330, 423, 5))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(300, 250, 423, 5))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 340, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(690, 390, 31, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Rbtn_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Rbtn_layout.setContentsMargins(0, 0, 0, 0)
        self.Rbtn_layout.setObjectName("Rbtn_layout")
        self.first_answer_Rbtn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.first_answer_Rbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.first_answer_Rbtn.setText("")
        self.first_answer_Rbtn.setObjectName("first_answer_Rbtn")
        self.Rbtn_layout.addWidget(self.first_answer_Rbtn)
        self.second_answer_Rbtn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.second_answer_Rbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.second_answer_Rbtn.setText("")
        self.second_answer_Rbtn.setObjectName("second_answer_Rbtn")
        self.Rbtn_layout.addWidget(self.second_answer_Rbtn)
        self.third_answer_Rbtn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.third_answer_Rbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.third_answer_Rbtn.setText("")
        self.third_answer_Rbtn.setObjectName("third_answer_Rbtn")
        self.Rbtn_layout.addWidget(self.third_answer_Rbtn)
        self.fourth_answer_Rbtn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.fourth_answer_Rbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.fourth_answer_Rbtn.setText("")
        self.fourth_answer_Rbtn.setObjectName("fourth_answer_Rbtn")
        self.Rbtn_layout.addWidget(self.fourth_answer_Rbtn)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(730, 0, 5, 561))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(220, 6, 3, 40))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(310, 6, 3, 40))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(400, 6, 3, 40))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(490, 6, 3, 40))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(580, 6, 3, 40))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.question_list = QtWidgets.QListWidget(self.centralwidget)
        self.question_list.setGeometry(QtCore.QRect(740, 0, 181, 551))
        self.question_list.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_list.setTabKeyNavigation(False)
        self.question_list.setProperty("isWrapping", False)
        self.question_list.setViewMode(QtWidgets.QListView.ListMode)
        self.question_list.setUniformItemSizes(True)
        self.question_list.setWordWrap(False)
        self.question_list.setSelectionRectVisible(False)
        self.question_list.setObjectName("question_list")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(390, 390, 301, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.first_answer_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.first_answer_lineEdit.setStyleSheet("QLineEdit:hover{\n"
"    border:1px solid #ff8c00;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border: 1px solid #ff8c00;\n"
"\n"
"}")
        self.first_answer_lineEdit.setObjectName("first_answer_lineEdit")
        self.verticalLayout.addWidget(self.first_answer_lineEdit)
        self.second_answer_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.second_answer_lineEdit.setStyleSheet("QLineEdit:hover{\n"
"    border:1px solid #ff8c00;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border: 1px solid #ff8c00;\n"
"}")
        self.second_answer_lineEdit.setObjectName("second_answer_lineEdit")
        self.verticalLayout.addWidget(self.second_answer_lineEdit)
        self.third_answer_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.third_answer_lineEdit.setStyleSheet("QLineEdit:hover{\n"
"    border:1px solid #ff8c00;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border: 1px solid #ff8c00;\n"
"\n"
"}")
        self.third_answer_lineEdit.setObjectName("third_answer_lineEdit")
        self.verticalLayout.addWidget(self.third_answer_lineEdit)
        self.fourth_answer_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.fourth_answer_lineEdit.setStyleSheet("QLineEdit:hover{\n"
"    border:1px solid #ff8c00;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border: 1px solid #ff8c00;\n"
"\n"
"}")
        self.fourth_answer_lineEdit.setObjectName("fourth_answer_lineEdit")
        self.verticalLayout.addWidget(self.fourth_answer_lineEdit)
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(80, 490, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.update_btn.setFont(font)
        self.update_btn.setObjectName("update_btn")
        self.clear_img_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_img_btn.setGeometry(QtCore.QRect(50, 330, 61, 41))
        self.clear_img_btn.setObjectName("clear_img_btn")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(120, 330, 3, 40))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.img_path_label = QtWidgets.QLabel(self.centralwidget)
        self.img_path_label.setGeometry(QtCore.QRect(960, 130, 16, 16))
        self.img_path_label.setText("")
        self.img_path_label.setObjectName("img_path_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        self.action_connect_us = QtWidgets.QMenu(self.menuhelp)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(".\\icons/connectUs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_connect_us.setIcon(icon7)
        self.action_connect_us.setObjectName("action_connect_us")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.action_open.setFont(font)
        self.action_open.setObjectName("action_open")
        self.action_new = QtWidgets.QAction(MainWindow)
        self.action_new.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.action_new.setFont(font)
        self.action_new.setIconVisibleInMenu(True)
        self.action_new.setObjectName("action_new")
        self.action_export = QtWidgets.QAction(MainWindow)
        self.action_export.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.action_export.setFont(font)
        self.action_export.setObjectName("action_export")
        self.action_export_nodataBase = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(".\\icons/export2.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_export_nodataBase.setIcon(icon8)
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(12)
        self.action_export_nodataBase.setFont(font)
        self.action_export_nodataBase.setObjectName("action_export_nodataBase")
        self.action_close = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(".\\icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_close.setIcon(icon9)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.action_close.setFont(font)
        self.action_close.setObjectName("action_close")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setIcon(icon6)
        self.action_about.setObjectName("action_about")
        self.action_facebook = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(".\\icons/facebook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_facebook.setIcon(icon10)
        self.action_facebook.setObjectName("action_facebook")
        self.action_twitter = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(".\\icons/tiwetter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_twitter.setIcon(icon11)
        self.action_twitter.setObjectName("action_twitter")
        self.action_instagram = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(".\\icons/instagram.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_instagram.setIcon(icon12)
        self.action_instagram.setObjectName("action_instagram")
        self.action_setting = QtWidgets.QAction(MainWindow)
        self.action_setting.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.action_setting.setFont(font)
        self.action_setting.setObjectName("action_setting")
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_new)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_export)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_setting)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_close)
        self.action_connect_us.addAction(self.action_facebook)
        self.action_connect_us.addAction(self.action_twitter)
        self.action_connect_us.addAction(self.action_instagram)
        self.menuhelp.addSeparator()
        self.menuhelp.addAction(self.action_connect_us.menuAction())
        self.menuhelp.addSeparator()
        self.menuhelp.addSeparator()
        self.menuhelp.addSeparator()
        self.menuhelp.addAction(self.action_about)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "exam creator"))
        MainWindow.setToolTip(_translate("MainWindow", "created By marwan Mohamed"))
        self.open_exam_btn.setToolTip(_translate("MainWindow", "فتح إختبار سابق"))
        self.New_exam_btn.setToolTip(_translate("MainWindow", "إنشاء اختبار جديد"))
        self.add_question_btn.setToolTip(_translate("MainWindow", "إضافة سؤال جديد"))
        self.export_btn.setToolTip(_translate("MainWindow", "تصدير  إختبار جديد أو إختبار قديم تم التعديل فيه "))
        self.setting_btn.setToolTip(_translate("MainWindow", "الإعدادات"))
        self.about_btn.setToolTip(_translate("MainWindow", "حول"))
        self.label.setText(_translate("MainWindow", "السؤال"))
        self.qusetion_img_lable.setText(_translate("MainWindow", "يمكنك أن تضيف صورة للسؤال بالضغط علي الز أدناه"))
        self.add_img_btn.setText(_translate("MainWindow", "إضافة صورة"))
        self.radioButton_3.setText(_translate("MainWindow", "أكمل"))
        self.choose_Rbtn.setText(_translate("MainWindow", "اختر "))
        self.true_or_false_Rbtn.setText(_translate("MainWindow", "صح/خطأ"))
        self.label_2.setText(_translate("MainWindow", "نوع السؤال"))
        self.label_3.setText(_translate("MainWindow", "الإجابة"))
        self.question_list.setSortingEnabled(False)
        self.first_answer_lineEdit.setPlaceholderText(_translate("MainWindow", "الإجابة الأولي"))
        self.second_answer_lineEdit.setPlaceholderText(_translate("MainWindow", "الإجابة الثانية"))
        self.third_answer_lineEdit.setPlaceholderText(_translate("MainWindow", "الإجابة الثالثة"))
        self.fourth_answer_lineEdit.setPlaceholderText(_translate("MainWindow", "الإجابة الرابعة"))
        self.update_btn.setText(_translate("MainWindow", "تعديل"))
        self.clear_img_btn.setText(_translate("MainWindow", "حذف"))
        self.menuFile.setTitle(_translate("MainWindow", "ملف"))
        self.menuhelp.setTitle(_translate("MainWindow", "مساعدة"))
        self.action_connect_us.setTitle(_translate("MainWindow", ".         اتصل بنا"))
        self.action_open.setText(_translate("MainWindow", ".            فتح"))
        self.action_new.setText(_translate("MainWindow", ".          جديد"))
        self.action_export.setText(_translate("MainWindow", ".         تصدير"))
        self.action_export_nodataBase.setText(_translate("MainWindow", ".         تحويل"))
        self.action_close.setText(_translate("MainWindow", ".          إغلاق"))
        self.action_about.setText(_translate("MainWindow", ".             حول"))
        self.action_facebook.setText(_translate("MainWindow", "     Facebook"))
        self.action_twitter.setText(_translate("MainWindow", "    Twitter"))
        self.action_instagram.setText(_translate("MainWindow", "    Instagram"))
        self.action_setting.setText(_translate("MainWindow", ".       الإعدادات"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
