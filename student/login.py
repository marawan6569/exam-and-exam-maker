import sys
from os import path
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from subprocess import call
import sqlite3

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "login_form.ui"))


class mainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()

    def db_connecton(self):
        self.con = sqlite3.connect("exam")
        self.cur = self.con.cursor()

    def Handel_UI(self):
        self.setFixedSize(440, 235)

    def Handel_Buttons(self):
        self.start_exam_btn.clicked.connect(self.start_exam)

    def save_data(self,name,num,sec):
        self.db_connecton()
        self.save_sql = "INSERT INTO studentInfo (studentName,studentNum,section,degree,percent) VALUES ('{}','{}','{}',0,0); ".format(name, num, sec)
        self.cur.execute(self.save_sql)
        self.con.commit()
        self.con.close()

    def start_exam(self):
        self.Sname = self.name_lineEdit.text()
        self.idNum = self.idNum_lineEdit.text()
        self.section = self.section_lineEdit.text()
        if self.Sname and self.idNum and self.section != "":
            self.save_data(name=self.Sname, num=self.idNum, sec=self.section)
            self.close()
            call(["python", "exam.py"])

        else:
            QMessageBox.information(self, "خطأ", "من فضلك ادخل بياناتك كاملة")

        print(self.Sname)
        print(self.idNum)
        print(self.section)


def main():
    app = QApplication(sys.argv)
    Mainwindow = mainApp()
    Mainwindow.show()
    app.exec_()


if __name__ == '__main__':
    main()
