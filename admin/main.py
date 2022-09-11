import sys
import os
from os import path
import shutil

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5.QtGui import QPixmap

import sqlite3
from subprocess import call
from webbrowser import open

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main_form.ui"))


class mainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.id = 1
        self.index = 1
        self.Handel_UI()
        self.Handel_Buttons()
        self.hide_answer_fields()
        self.disable_all_fields()
        self.enable_add_question_btn()
        self.question_IMG_path = ""
        


    def db_connection(self, sql):
        self.con = sqlite3.connect("./student/exam")
        self.cur = self.con.cursor()
        self.cur.execute(sql)

    def Handel_UI(self):
        self.setFixedSize(960, 600)

    def Handel_Buttons(self):
        self.open_exam_btn.clicked.connect(self.open_exam)
        self.New_exam_btn.clicked.connect(self.new_exam)
        self.true_or_false_Rbtn.clicked.connect(self.true_or_false_question)
        self.choose_Rbtn.clicked.connect(self.choose_question)
        self.add_question_btn.clicked.connect(self.add_question)
        self.setting_btn.clicked.connect(self.setting)
        self.add_img_btn.clicked.connect(self.questionIMG)
        self.add_question_btn.clicked.connect(self.reset_question_Img)

        self.export_btn.clicked.connect(self.exporting)

        self.first_answer_Rbtn.clicked.connect(self.enable_add_question_btn)
        self.second_answer_Rbtn.clicked.connect(self.enable_add_question_btn)
        self.third_answer_Rbtn.clicked.connect(self.enable_add_question_btn)
        self.fourth_answer_Rbtn.clicked.connect(self.enable_add_question_btn)

        self.action_facebook.triggered.connect(self.my_facebook)
        self.action_twitter.triggered.connect(self.my_twitter)
        self.action_instagram.triggered.connect(self.my_instagram)

    def Handel_browes(self):
        self.saveLocation = str(QFileDialog.getExistingDirectory(self, "Select Directory"))


    def enable_add_question_btn(self):
        self.queston_text = self.qusetion_textEdit_field.toPlainText()
        self.first_answer_text = self.first_answer_lineEdit.text()
        self.second_answer_text = self.second_answer_lineEdit.text()
        self.third_answer_text = self.third_answer_lineEdit.text()
        self.fourth_answer_text = self.fourth_answer_lineEdit.text()
        if self.queston_text != "" and self.first_answer_text != "" and self.second_answer_text != "" and self.third_answer_text != "" and self.fourth_answer_text != "":
            self.add_question_btn.setEnabled(True)

    def hide_answer_fields(self):
        self.label_3.hide()
        self.first_answer_Rbtn.hide()
        self.second_answer_Rbtn.hide()
        self.third_answer_Rbtn.hide()
        self.fourth_answer_Rbtn.hide()
        self.first_answer_lineEdit.hide()
        self.second_answer_lineEdit.hide()
        self.third_answer_lineEdit.hide()
        self.fourth_answer_lineEdit.hide()

    def disable_all_fields(self):
        self.add_question_btn.setEnabled(False)
        self.export_btn.setEnabled(False)
        self.export_No_dataBase_btn.setEnabled(False)
        self.setting_btn.setEnabled(False)
        self.qusetion_textEdit_field.setEnabled(False)
        self.true_or_false_Rbtn.setEnabled(False)
        self.choose_Rbtn.setEnabled(False)
        self.add_img_btn.setEnabled(False)
        self.action_export.setEnabled(False)
        self.action_export_nodataBase.setEnabled(False)
        self.action_setting.setEnabled(False)

        self.radioButton_3.setEnabled(False)

    def enabal_all_fields(self):
        self.add_question_btn.setEnabled(False)
        self.export_btn.setEnabled(True)
        self.export_No_dataBase_btn.setEnabled(True)
        self.setting_btn.setEnabled(True)
        self.qusetion_textEdit_field.setEnabled(True)
        self.true_or_false_Rbtn.setEnabled(True)
        self.choose_Rbtn.setEnabled(True)
        self.add_img_btn.setEnabled(True)
        self.action_export.setEnabled(True)
        self.action_export_nodataBase.setEnabled(True)
        self.action_setting.setEnabled(True)

    def new_exam(self):
        os.remove(os.getcwd()+"/student/exam")
        self.answer_table_sql = """ CREATE TABLE IF NOT EXISTS `Answers` (
                `AnswerId`	INTEGER PRIMARY KEY AUTOINCREMENT,
                `answer_1`	TEXT NOT NULL,
                `answer_2`	TEXT NOT NULL,
                `answer_3`	TEXT NOT NULL,
                `answer_4`	TEXT NOT NULL
            ); """
        self.genral_table_sql = """CREATE TABLE IF NOT EXISTS `general` (
                `id`	INTEGER PRIMARY KEY AUTOINCREMENT,
                `exam_Name`	TEXT NOT NULL,
                `exam_time`	INTEGER NOT NULL,
                `total_degrees`	INTEGER NOT NULL,
                `question_num`	INTEGER NOT NULL,
                `newExamSaveLocation`	INTEGER NOT NULL
            ); """
        self.question_table_sql = """ CREATE TABLE IF NOT EXISTS `questions` (
                `questionId`	INTEGER PRIMARY KEY AUTOINCREMENT,
                `question`	TEXT NOT NULL UNIQUE,
                `correctAnswer`	TEXT NOT NULL,
                `questionType`	INTEGER NOT NULL,
                `questionIMG`	TEXT
            ); """
        self.studentInfo_table_sql = """ CREATE TABLE IF NOT EXISTS `studentInfo` (
                `id`	INTEGER,
                `studentName`	TEXT NOT NULL,
                `studentNum`	INTEGER NOT NULL,
                `section`	TEXT NOT NULL,
                `degree`	INTEGER NOT NULL,
                `percent`	INTEGER NOT NULL,
                PRIMARY KEY(`id`)
            ); """
        try:
            self.db_connection(self.answer_table_sql)
            self.con.commit()
            self.con.close()
        except Exception as AE:
            print("error from answer table ==> ", AE)

        try:
            self.db_connection(self.genral_table_sql)
            self.con.commit()
            self.con.close()
        except Exception as GE:
            print("error from general table ==> ", GE)

        try:
            self.db_connection(self.question_table_sql)
            self.con.commit()
            self.con.close()
        except Exception as QE:
            print("error form question table ==> ", QE)

        try:
            self.db_connection(self.studentInfo_table_sql)
            self.con.commit()
            self.con.close()
        except Exception as SE:
            print("error from studentInfo table ==> ", SE)


        call(['python3.6', 'setting.py'])
        call(['python3.6', 'new_exam_script.py'])
        self.enabal_all_fields()

    def open_exam(self):
        self.enabal_all_fields()

    def true_or_false_question(self):
        self.label_3.show()
        self.first_answer_Rbtn.show()
        self.second_answer_Rbtn.show()
        self.first_answer_lineEdit.show()
        self.second_answer_lineEdit.show()

        self.first_answer_lineEdit.setText("صح")
        self.second_answer_lineEdit.setText("خطأ")
        self.third_answer_lineEdit.setText("0")
        self.fourth_answer_lineEdit.setText("0")

        self.first_answer_lineEdit.setEnabled(False)
        self.second_answer_lineEdit.setEnabled(False)

        self.third_answer_Rbtn.hide()
        self.fourth_answer_Rbtn.hide()
        self.third_answer_lineEdit.hide()
        self.fourth_answer_lineEdit.hide()

    def choose_question(self):
        self.label_3.show()
        self.first_answer_Rbtn.show()
        self.second_answer_Rbtn.show()
        self.third_answer_Rbtn.show()
        self.fourth_answer_Rbtn.show()
        self.first_answer_lineEdit.show()
        self.second_answer_lineEdit.show()
        self.third_answer_lineEdit.show()
        self.fourth_answer_lineEdit.show()

        self.first_answer_lineEdit.setEnabled(True)
        self.second_answer_lineEdit.setEnabled(True)
        self.first_answer_lineEdit.setText("")
        self.second_answer_lineEdit.setText("")
        self.third_answer_lineEdit.setText("")
        self.fourth_answer_lineEdit.setText("")

    def Handel_Browse(self):
        try:
            self.img_place = QFileDialog.getOpenFileName(self, caption='choose an Img', directory='./IMG',
                                                         filter=('*.png *.xpm *.jpg *.bmp *.jpeg'))
            text = str(self.img_place)
            self.name = (text[2:].split(',')[0].replace("'", ""))
        except:
            pass

    def questionIMG(self):
        try:
            self.Handel_Browse()
            self.question_IMG_path = self.name
            self.question_IMG_path = list(self.question_IMG_path.split('/'))
            self.question_IMG_path = str("./" + self.question_IMG_path[-2] + "/" + self.question_IMG_path[-1])
            self.qusetion_img_lable.setText("")
            self.qusetion_img_lable.setPixmap(QPixmap(self.question_IMG_path))
        except:
            pass

    def add_question(self):
        self.question_IMG =str(self.question_IMG_path)
        print(self.question_IMG)
        self.queston_text = self.qusetion_textEdit_field.toPlainText()
        self.first_answer_text = self.first_answer_lineEdit.text()
        self.second_answer_text = self.second_answer_lineEdit.text()
        self.third_answer_text = self.third_answer_lineEdit.text()
        self.fourth_answer_text = self.fourth_answer_lineEdit.text()
        self.question_type = 0
        self.correct_answer = 0

        if self.queston_text == "":
            print("please enter question")

        if not self.true_or_false_Rbtn.isChecked() and not self.choose_Rbtn.isChecked():
            print("please choose question type")
        elif self.choose_Rbtn.isChecked():
            self.question_type = 0

        elif self.true_or_false_Rbtn.isChecked():
            self.question_type = 1

        else:
            print("choose the q type")

        if not self.first_answer_Rbtn.isChecked() and not self.second_answer_Rbtn.isChecked() and not self.third_answer_Rbtn.isChecked() and not self.fourth_answer_Rbtn.isChecked():
            QMessageBox.information(self, "خطأ", "من فضلك اختر الإجابة الصحيحة")

        elif self.first_answer_Rbtn.isChecked():
            self.correct_answer = "answer_1"

        elif self.second_answer_Rbtn.isChecked():
            self.correct_answer = "answer_2"

        elif self.third_answer_Rbtn.isChecked():
            self.correct_answer = "answer_3"

        elif self.fourth_answer_Rbtn.isChecked():
            self.correct_answer = "answer_4"

        else:
            QMessageBox.information(self, "خطأ", "من فضلك اختر الإجابة الصحيحة")

        if self.question_type == 0:
            if self.first_answer_text == "":
                QMessageBox.information(self, "خطأ", "من فضلك املأ جميع الحقول")

            if self.second_answer_text == "":
                QMessageBox.information(self, "خطأ", "من فضلك املأ جميع الحقول")

            if self.third_answer_text == "":
                QMessageBox.information(self, "خطأ", "من فضلك املأ جميع الحقول")

            if self.fourth_answer_text == "":
                QMessageBox.information(self, "خطأ", "من فضلك املأ جميع الحقول")
            else:
                pass

        if self.queston_text != "":
            if self.true_or_false_Rbtn.isChecked():
                if self.first_answer_Rbtn.isChecked() or self.second_answer_Rbtn.isChecked():

                    try:
                        self.add_question_sql = """ INSERT INTO questions
                         VALUES('{}','{}','{}','{}','{}');""".format(self.id, self.queston_text, self.correct_answer, self.question_type, self.question_IMG)
                        self.db_connection(self.add_question_sql)
                        self.con.commit()
                        self.con.close()
                    except Exception as e:
                        QMessageBox.information(self, "خطأ", str(e))

                    try:
                        self.add_answer_sql = """ INSERT INTO Answers
                         VALUES('{}','{}','{}','{}','{}'); 
                         """.format(self.id, self.first_answer_text, self.second_answer_text, self.third_answer_text, self.fourth_answer_text)
                        self.db_connection(self.add_answer_sql)
                        self.con.commit()
                        self.con.close()
                        self.id += 1
                    except:
                        pass

            elif self.choose_Rbtn.isChecked():
                if self.first_answer_Rbtn.isChecked() or self.second_answer_Rbtn.isChecked() or self.third_answer_Rbtn.isChecked() or self.fourth_answer_Rbtn.isChecked():
                    if self.first_answer_text != "" and self.second_answer_text != "" and self.third_answer_text != "" and self.fourth_answer_text != "":
                        try:
                            self.add_question_sql = """ INSERT INTO questions
                             VALUES('{}','{}','{}','{}','{}');""".format(self.id, self.queston_text,
                                                                         self.correct_answer, self.question_type,
                                                                         self.question_IMG)
                            self.db_connection(self.add_question_sql)
                            self.con.commit()
                            self.con.close()
                        except Exception as e:
                            QMessageBox.information(self, "خطأ", str(e))

                        try:
                            self.add_answer_sql = """ INSERT INTO Answers
                             VALUES('{}','{}','{}','{}','{}'); 
                             """.format(self.id, self.first_answer_text, self.second_answer_text,
                                        self.third_answer_text, self.fourth_answer_text)
                            self.db_connection(self.add_answer_sql)
                            self.con.commit()
                            self.con.close()
                            self.id += 1
                        except Exception as e:
                            print(e)

        self.index += 1
        if self.index == self.id:
            self.add_question_btn.setEnabled(False)
            self.question_list.addItem("السؤال رقم: " + str(self.id - 1))
        else:
            self.index = self.id
        self.question_IMG_path = ""

    def exporting(self):
        call(['python3.6', 'exporting_script.py'])

    def open_exam(self):
        self.exam_location = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        try:
           os.remove(os.getcwd()+"/student/exam")
           shutil.copy(self.exam_location, os.getcwd()+"/student/exam")
        except:
            pass

    def set_list_item(self):
        self.question_num_sql = f"SELECT questionId FROM questions;"
        self.db_connection(self.question_num_sql)
        self.num = self.cur.fetchall()
        self.con.close()
        for i in self.num:
            self.question_list.addItem("السؤال رقم: " + str(i[0]))

    def setting(self):
        call(['python3.6', 'general.py'])

    def reset_question_Img(self):
        self.qusetion_img_lable.setPixmap(QPixmap("/"))
        self.qusetion_img_lable.setText("يمكنك أن تضيف صورة بالضغط علي الزر أدناه")

    def my_facebook(self):
        open("https://www.facebook.com/marwanmo7amed8", new=2)

    def my_instagram(self):
        open('https://www.instagram.com/marwan_mohamed_0_0/', new=2)

    def my_twitter(self):
        pass


def main():
    app = QApplication(sys.argv)
    Mainwindow = mainApp()
    Mainwindow.show()
    app.exec_()


if __name__ == '__main__':
    main()
