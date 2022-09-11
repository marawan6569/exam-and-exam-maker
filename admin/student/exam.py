import sys
from os import path

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5.QtGui import QPixmap
from subprocess import call
import sqlite3
from time import sleep
from threading import Thread

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "exam_form.ui"))


class mainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.index = 2
        self.Aindex = 1
        self.final_result = []
        self.set_exam()
        self.Handel_UI()
        self.Handel_Buttons()
        self.th_timer = Thread(target=self.start_timer)
        self.th_timer.start()
        self.label.setPixmap(QPixmap('pannar.jpg'))


    def db_connecton(self):
        self.con = sqlite3.connect("exam")
        self.cur = self.con.cursor()

    def Handel_UI(self):
        self.setFixedSize(750, 560)

    def Handel_Buttons(self):
        self.next_btn.clicked.connect(self.set_question)
        self.next_btn.setEnabled(False)
        self.finish_btn.clicked.connect(self.check_answer)
        self.end_exam_btn.clicked.connect(self.end_exam)

    def start_timer(self):
        try:
            self.get_time_sql = "SELECT exam_time FROM general WHERE id = 1"
            self.db_connecton()
            self.cur.execute(self.get_time_sql)
            self.gitTime = self.cur.fetchall()
            self.time = self.gitTime[0][0]
            self.con.close()
            while self.time > 0:
                self.timer_label.setText(str(self.time))
                self.time -= 1
                sleep(59)
                try:
                    if self.isActiveWindow() == False:
                        pass
                except Exception as e:
                    try:
                        self.th_timer.join()
                    except:
                        pass
            self.end_exam_btn.click()
        except:
            pass

    def set_exam(self):
        self.set_exam_sql = "SELECT exam_name FROM general WHERE id = 1;"
        self.set_FQ_sql = "SELECT question,correctAnswer,questionType,questionIMG FROM questions WHERE questionId = 1;"
        self.set_FA_sql = "SELECT answer_1,answer_2,answer_3,answer_4 FROM Answers WHERE AnswerId = 1;"
        self.db_connecton()
        self.cur.execute(self.set_exam_sql)
        self.Gres = self.cur.fetchall()
        self.exam_name_label.setText(self.Gres[0][0])
        #######
        self.cur.execute(self.set_FQ_sql)
        self.FQres = self.cur.fetchall()
        self.q = self.FQres[0][0]
        self.cAnswer = self.FQres[0][1]
        self.qType = self.FQres[0][2]
        self.qIMG = self.FQres[0][3]
        self.q_img.setPixmap(QPixmap(self.qIMG))
        self.question_label.setText(self.q)
        #######
        if self.qType == 0:
            self.cur.execute(self.set_FA_sql)
            self.FAres = self.cur.fetchall()
            self.A1 = self.FAres[0][0]
            self.A2 = self.FAres[0][1]
            self.A3 = self.FAres[0][2]
            self.A4 = self.FAres[0][3]
            self.answer_1.setText(self.A1)
            self.answer_2.setText(self.A2)
            self.answer_3.setText(self.A3)
            self.answer_4.setText(self.A4)
        elif self.qType == 1:
            self.cur.execute(self.set_FA_sql)
            self.FAres = self.cur.fetchall()
            self.A1 = self.FAres[0][0]
            self.A2 = self.FAres[0][1]
            print(self.A1)
            print(self.A2)
            self.answer_1.setText(self.A1)
            self.answer_2.setText(self.A2)
            self.answer_3.hide()
            self.answer_4.hide()
        #######
        self.con.close()

    def check_answer(self):
        try:
            self.db_connecton()
            self.correct_answer_sql = "SELECT correctAnswer FROM questions WHERE questionId = {};".format(self.Aindex)
            self.cur.execute(self.correct_answer_sql)
            self.CA = self.cur.fetchall()
            self.correct_answer = self.CA[0][0]
            self.con.close()
            if self.answer_1.isChecked():
                if self.correct_answer == "answer_1":
                    self.final_result.append(1)
                else:
                    self.final_result.append(0)

            elif self.answer_2.isChecked():
                if self.correct_answer == "answer_2":
                    self.final_result.append(1)
                else:
                    self.final_result.append(0)

            elif self.answer_3.isChecked():
                if self.correct_answer == "answer_3":
                    self.final_result.append(1)
                else:
                    self.final_result.append(0)


            elif self.answer_4.isChecked():
                if self.correct_answer == "answer_4":
                    self.final_result.append(1)
                else:
                    self.final_result.append(0)

            self.next_btn.setEnabled(True)
            self.finish_btn.setEnabled(False)

            self.Aindex += 1
        except:
            self.end_exam()

    def set_question(self):
        try:
            self.set_Question_sql = "SELECT question,questionType,questionIMG FROM questions WHERE questionId = {};".format(self.index)
            self.set_Answer_sql = "SELECT answer_1,answer_2,answer_3,answer_4 FROM Answers WHERE AnswerId = {};".format(self.index)
            self.db_connecton()
            self.cur.execute(self.set_Question_sql)
            self.question_res = self.cur.fetchall()
            self.question = self.question_res[0][0]
            self.question_type = self.question_res[0][1]
            self.qusetion_img = self.question_res[0][2]
            self.q_img.setPixmap(QPixmap(self.qusetion_img))
            self.question_label.setText(self.question)
            ########
            self.cur.execute(self.set_Answer_sql)
            self.answer_res = self.cur.fetchall()
            self.first_answer = self.answer_res[0][0]
            self.second_answer = self.answer_res[0][1]
            self.third_answer = self.answer_res[0][2]
            self.fourth_answer = self.answer_res[0][3]
            if self.question_type == 0:
                self.answer_1.setText(self.first_answer)
                self.answer_2.setText(self.second_answer)
                self.answer_3.setText(self.third_answer)
                self.answer_4.setText(self.fourth_answer)
                self.answer_3.show()
                self.answer_4.show()
            elif self.question_type == 1:
                self.answer_1.setText(self.first_answer)
                self.answer_2.setText(self.second_answer)
                self.answer_3.hide()
                self.answer_4.hide()
            ########
            self.index += 1
            self.finish_btn.setEnabled(True)
            self.next_btn.setEnabled(False)
        except:
            self.end_exam()

    def end_exam(self):
        self.get_result()
        self.close()
        call(['python3.6', 'print.py'])

    def get_result(self):
        self.student_res = []
        for i in self.final_result:
            if i == 1:
                self.student_res.append(1)
            else:
                pass

        self.student_result = len(self.student_res)
        self.percent = self.student_result / len(self.final_result) * 100

        self.update_data_sql = "UPDATE studentInfo SET degree ={}, percent ={} WHERE id = 1;".format(self.student_result, self.percent)
        self.db_connecton()
        self.cur.execute(self.update_data_sql)
        self.con.commit()
        self.con.close()
        print(self.percent)
        print("you got : ", len(self.student_res), "of ", len(self.final_result))


def main():
    app = QApplication(sys.argv)
    Mainwindow = mainApp()
    Mainwindow.show()
    app.exec_()


if __name__ == '__main__':
    main()
