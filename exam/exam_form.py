# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\exam_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_exam(object):
    def setupUi(self, exam):
        exam.setObjectName("exam")
        exam.resize(947, 693)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icons/1490886301-09-examination_82492.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        exam.setWindowIcon(icon)
        exam.setLayoutDirection(QtCore.Qt.RightToLeft)
        exam.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
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
"\n"
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
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(exam)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 501, 161))
        font = QtGui.QFont()
        font.setFamily("Noto Kufi Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\pannar.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.timer_label = QtWidgets.QLabel(self.centralwidget)
        self.timer_label.setGeometry(QtCore.QRect(50, 10, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.timer_label.setFont(font)
        self.timer_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.timer_label.setMouseTracking(False)
        self.timer_label.setStyleSheet("QLabel{\n"
"    border: 1px  solid #ff8c00;\n"
"    background-color: transparent;\n"
"    color:  #FCF7DC;\n"
"}")
        self.timer_label.setText("")
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_label.setObjectName("timer_label")
        self.finish_btn = QtWidgets.QPushButton(self.centralwidget)
        self.finish_btn.setEnabled(True)
        self.finish_btn.setGeometry(QtCore.QRect(30, 80, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.finish_btn.setFont(font)
        self.finish_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.finish_btn.setStyleSheet("\n"
"QPushButton{\n"
"color:#FCF7DC;\n"
"border:2px solid #ff8c00;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    color:#ff8c00;\n"
"    border:2px solid #FCF7DC;\n"
"\n"
"    \n"
"}")
        self.finish_btn.setObjectName("finish_btn")
        self.q_img = QtWidgets.QLabel(self.centralwidget)
        self.q_img.setGeometry(QtCore.QRect(30, 270, 201, 201))
        font = QtGui.QFont()
        font.setFamily("Noto Kufi Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.q_img.setFont(font)
        self.q_img.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.q_img.setStyleSheet("QLabel{\n"
"    border: 3px solid #ff8c00\n"
"}")
        self.q_img.setText("")
        self.q_img.setPixmap(QtGui.QPixmap(".\\../IMG/setting.png"))
        self.q_img.setScaledContents(True)
        self.q_img.setObjectName("q_img")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 430, 341, 240))
        font = QtGui.QFont()
        font.setFamily("Noto Kufi Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.answer_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.answer_layout.setContentsMargins(0, 0, 0, 0)
        self.answer_layout.setSpacing(12)
        self.answer_layout.setObjectName("answer_layout")
        self.answer_1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.answer_1.setFont(font)
        self.answer_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.answer_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.answer_1.setText("")
        self.answer_1.setObjectName("answer_1")
        self.answer_layout.addWidget(self.answer_1)
        self.answer_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.answer_2.setFont(font)
        self.answer_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.answer_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.answer_2.setStyleSheet("color:#FCF7DC")
        self.answer_2.setText("")
        self.answer_2.setObjectName("answer_2")
        self.answer_layout.addWidget(self.answer_2)
        self.answer_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.answer_3.setFont(font)
        self.answer_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.answer_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.answer_3.setText("")
        self.answer_3.setObjectName("answer_3")
        self.answer_layout.addWidget(self.answer_3)
        self.answer_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.answer_4.setFont(font)
        self.answer_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.answer_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.answer_4.setStyleSheet("color:#FCF7DC;")
        self.answer_4.setText("")
        self.answer_4.setObjectName("answer_4")
        self.answer_layout.addWidget(self.answer_4)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(638, 362, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_6.setStyleSheet("QLabel{\n"
"    color:#FCF7DC;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.exam_name_label = QtWidgets.QLabel(self.centralwidget)
        self.exam_name_label.setGeometry(QtCore.QRect(400, 190, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.exam_name_label.setFont(font)
        self.exam_name_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.exam_name_label.setStyleSheet("QLabel{\n"
"    border: 0px;\n"
"    background-color: transparent;\n"
"    background-color: transparent;\n"
"    color:  #ff8c00;\n"
"}")
        self.exam_name_label.setText("")
        self.exam_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.exam_name_label.setObjectName("exam_name_label")
        self.end_exam_btn = QtWidgets.QPushButton(self.centralwidget)
        self.end_exam_btn.setGeometry(QtCore.QRect(60, 570, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.end_exam_btn.setFont(font)
        self.end_exam_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.end_exam_btn.setStyleSheet("QPushButton{\n"
"color:#FCF7DC;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    color:#ff8c00;\n"
"}")
        self.end_exam_btn.setObjectName("end_exam_btn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(640, 250, 81, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setStyleSheet("QLabel{\n"
"    color:#FCF7DC;\n"
"}")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.question_label = QtWidgets.QLabel(self.centralwidget)
        self.question_label.setGeometry(QtCore.QRect(240, 250, 401, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.question_label.setFont(font)
        self.question_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.question_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_label.setStyleSheet("QLabel{\n"
"    border: 0px;\n"
"    background-color: transparent;\n"
"    background-color: transparent;\n"
"    color:  #ff8c00;\n"
"}")
        self.question_label.setText("")
        self.question_label.setScaledContents(True)
        self.question_label.setWordWrap(True)
        self.question_label.setObjectName("question_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(638, 352, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Kufi Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(628, 360, 20, 45))
        font = QtGui.QFont()
        font.setFamily("Noto Kufi Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(638, 398, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Kufi Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.line_3.setFont(font)
        self.line_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(720, 360, 20, 45))
        font = QtGui.QFont()
        font.setFamily("Noto Kufi Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.line_4.setFont(font)
        self.line_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.line_4.setStyleSheet("color:#FCF7DC;")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 200, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    color:#FCF7DC;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.start_exam_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_exam_btn.setGeometry(QtCore.QRect(390, 250, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.start_exam_btn.setFont(font)
        self.start_exam_btn.setStyleSheet("QPushButton{\n"
"    border: 5px solid #ff8c00\n"
"}")
        self.start_exam_btn.setObjectName("start_exam_btn")
        self.skiped_question_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.skiped_question_listWidget.setGeometry(QtCore.QRect(740, 90, 201, 411))
        self.skiped_question_listWidget.setObjectName("skiped_question_listWidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(750, 30, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"    border: 1px solid #ff8c00\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        exam.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(exam)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 947, 21))
        self.menubar.setObjectName("menubar")
        exam.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(exam)
        self.statusbar.setObjectName("statusbar")
        exam.setStatusBar(self.statusbar)

        self.retranslateUi(exam)
        QtCore.QMetaObject.connectSlotsByName(exam)
        exam.setTabOrder(self.answer_1, self.answer_3)
        exam.setTabOrder(self.answer_3, self.answer_4)
        exam.setTabOrder(self.answer_4, self.finish_btn)

    def retranslateUi(self, exam):
        _translate = QtCore.QCoreApplication.translate
        exam.setWindowTitle(_translate("exam", "MainWindow"))
        self.finish_btn.setText(_translate("exam", "تسليم"))
        self.label_6.setText(_translate("exam", " الإجابة :"))
        self.end_exam_btn.setText(_translate("exam", "إنهاء الإختبار"))
        self.label_4.setText(_translate("exam", " السؤال :"))
        self.label_2.setText(_translate("exam", "المادة:"))
        self.start_exam_btn.setText(_translate("exam", "إبدأ الإمتحان"))
        self.label_3.setText(_translate("exam", "الأسئلة "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exam = QtWidgets.QMainWindow()
    ui = Ui_exam()
    ui.setupUi(exam)
    exam.show()
    sys.exit(app.exec_())
