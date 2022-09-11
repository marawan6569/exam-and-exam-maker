import sys
from os import path

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sqlite3


FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "general_form.ui"))


class mainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()

    def Handel_UI(self):
        self.setFixedSize(470, 300)

    def Handel_Buttons(self):
        self.save_btn.clicked.connect(self.update_data)
        self.browes_btn.clicked.connect(self.Handel_browes)

    def Handel_browes(self):
        self.saveLocation = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.exam_pass_LD.setText(self.saveLocation)

    def db_connection(self, sql):
        self.con = sqlite3.connect("./student/exam")
        self.cur = self.con.cursor()
        self.cur.execute(sql)


    def update_data(self):
        self.saveLocation  = self.exam_pass_LD.text()
        self.exam_name = self.exam_name_LD.text()
        self.question_num = self.question_num_sp.value()
        self.degree = self.degree_sp.value()
        self.exam_time = self.exam_time_sp.value()
        self.update_data_sql = f"""
            UPDATE general SET 
            exam_Name = '{self.exam_name}',
            exam_time = {self.exam_time},
            total_degrees = {self.degree},
            question_num = {self.question_num},
            newExamSaveLocation = '{self.saveLocation}'
        """
        if self.exam_name != "" and self.saveLocation != "":
            self.db_connection(self.update_data_sql)
            self.con.commit()
            self.con.close()
            self.close()
        else:
            QMessageBox.information(self, "خطأ", "برجأء إدخال البيانات")


def main():
    app = QApplication(sys.argv)
    Mainwindow = mainApp()
    Mainwindow.show()
    app.exec_()


if __name__ == '__main__':
    main()