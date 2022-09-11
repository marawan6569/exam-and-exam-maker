import sys
from os import path
from escpos.connections import getUSBPrinter

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sqlite3

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "print_form.ui"))


class mainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()
        self.show_data()

    def db_connecton(self):
        self.con = sqlite3.connect("exam")
        self.cur = self.con.cursor()

    def Handel_UI(self):
        self.setFixedSize(475, 465)

    def Handel_Buttons(self):
        self.print_btn.clicked.connect(self.print_fun)

    def show_data(self):
        global  reslute_file
        self.get_data_sql = " SELECT * FROM studentInfo WHERE id = 1;"
        self.total_questions_sql = "SELECT question_num FROM general WHERE id = 1;"

        self.db_connecton()
        self.cur.execute(self.total_questions_sql)
        self.datat = self.cur.fetchall()
        self.con.close()
        self.total_questions = self.datat[0][0]

        self.db_connecton()
        self.cur.execute(self.get_data_sql)
        self.data = self.cur.fetchall()
        self.con.close()
        print(self.data)

        self.full_name = self.data[0][1]
        self.student_num = str(self.data[0][2])
        self.section = self.data[0][3]
        self.degree = str(self.data[0][4])
        self.percent = round(self.data[0][5], 2)
        self.percent = str(self.percent)+" %"

        self.name_lablel.setText(self.full_name)
        self.idNum_label.setText(self.student_num)
        self.section_label.setText(self.section)
        self.degree_label.setText(self.degree+str(" من ")+str(self.total_questions)+"                                               ")
        self.percent_label.setText(self.percent)
        self.writen_data = f"الاسم ==>   {self.full_name}\n\nالرقم ==>          {self.student_num}\n\nالشعبة ==>       {self.section}\n\nالدرجة ==>        {self.degree} من {self.total_questions}\n\nالنسبة ==>        {self.percent}"
        print(self.writen_data)
        with open(file=f'{self.full_name}.txt', mode='w', encoding='utf-8') as reslute_file:
            reslute_file.write(self.writen_data)


    def print_fun(self):
        printer = getUSBPrinter()(idVendor=0x1504,
                                  idProduct=0x0006,
                                  inputEndPoint = 0x82,
                                  outputEndPoint = 0x01)
        printer.text("Hello World")
        printer.lf()


def main():
    app = QApplication(sys.argv)
    Mainwindow = mainApp()
    Mainwindow.show()
    app.exec_()


if __name__ == '__main__':
    main()
