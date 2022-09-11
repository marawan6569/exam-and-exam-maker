# -*- coding: utf-8 -*-
import sys
from os import path
import os
import shutil
from distutils.dir_util import copy_tree
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sqlite3
import datetime
import xlsxwriter
from time import sleep
from threading import Thread
from exam_form import Ui_exam
from login_form import login_Form
from print_form import print_Form


 # * Log in class *#

class mainApp(QMainWindow, login_Form):
    def __init__(self, parent=None):
        super(mainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()

    def Handel_UI(self):
        self.setFixedSize(440, 235)

    def Handel_Buttons(self):
        self.start_exam_btn.clicked.connect(self.start_exam)

    def save_data(self, name, num, sec):
        with open('data.txt', 'w', encoding='utf-8') as opend_file:
            opend_file.write(f"{name}\n{num}\n{sec}")

    def start_exam(self):
        self.Sname = self.name_lineEdit.text()
        self.idNum = self.idNum_lineEdit.text()
        self.section = self.section_lineEdit.text()
        if self.Sname and self.idNum and self.section != "":
            self.save_data(name=self.Sname, num=self.idNum, sec=self.section)
            self.window2 = exam_mainApp()
            self.close()
            self.window2.show()


        else:
            QMessageBox.information(self, "خطأ", "من فضلك ادخل بياناتك كاملة")

 # * Exam class *#

class exam_mainApp(QMainWindow, Ui_exam):
    def __init__(self, parent=None):
        super(exam_mainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ws2_row_num = 4
        self.row_num = 8
        self.final_result = []
        self.result_dict = {}
        self.Handel_UI()
        self.Handel_Buttons()
        self.disable_all_fields()
        self.label.setPixmap(QPixmap('pannar.jpg'))

    def db_connecton(self):
        self.con = sqlite3.connect("exam")
        self.cur = self.con.cursor()

    def Handel_UI(self):
        self.setFixedSize(950, 670)

    def Handel_Buttons(self):
        self.end_exam_btn.clicked.connect(self.end_exam)
        self.skiped_question_listWidget.clicked.connect(self.set_question)
        self.start_exam_btn.clicked.connect(self.handel_browes)
        self.finish_btn.clicked.connect(self.check_Answer)

        # * send an answer to check_answer finction *#
        self.answer_1.clicked.connect(self.check_sender)
        self.answer_2.clicked.connect(self.check_sender)
        self.answer_3.clicked.connect(self.check_sender)
        self.answer_4.clicked.connect(self.check_sender)

    def start_timer(self):
        try:
            self.get_time_sql = "SELECT exam_time FROM general WHERE id = 1"
            self.db_connecton()
            self.cur.execute(self.get_time_sql)
            self.gitTime = self.cur.fetchall()
            self.time = self.gitTime[0][0]
            self.con.close()
            l1 = list(range(self.time))
            l2 = list(range(60))
            while self.time > 0:
                for i in reversed(l1):
                    for x in reversed(l2):
                        full_time = str(i) + ":" + str(x)
                        self.timer_label.setText(full_time)
                        sleep(1)
                    self.time -= 1
            self.end_exam_btn.click()
        except Exception as e:
            pass

    def set_question_list(self):
        sql = "SELECT question_num FROM general WHERE  id = 1"
        self.db_connecton()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        self.con.close()
        self.question_num = data[0][0]
        for i in range(1, self.question_num + 1):
            self.skiped_question_listWidget.addItem("السؤال رقم: " + str(i))

    def end_exam(self):
        self.get_result()
        self.end_exel()
        self.window3 = print_mainApp()
        self.close()
        self.window3.show()

    def get_result(self):
        # * adding student answers to final list * #
        for value in self.result_dict.values():
            self.final_result.append(value)


        self.student_res = []
        for i in self.final_result:
            if i == 1:
                self.student_res.append(1)
            else:
                pass

        self.student_result = len(self.student_res)
        self.percent = self.student_result / self.question_num * 100

        self.update_data_sql = "UPDATE studentInfo SET degree ={}, percent ={} WHERE id = 1;".format(
            self.student_result, self.percent)
        self.db_connecton()
        self.cur.execute(self.update_data_sql)
        self.con.commit()
        self.con.close()

    def disable_all_fields(self):
        self.finish_btn.setEnabled(False)
        self.end_exam_btn.setEnabled(False)
        self.answer_1.setEnabled(False)
        self.answer_2.setEnabled(False)
        self.answer_3.setEnabled(False)
        self.answer_4.setEnabled(False)

    def handel_browes(self):
        try:
            try:
                os.rename(os.getcwd() + "/exam")
            except:
                pass
                text = QFileDialog.getExistingDirectory(self, "selec the exam")
            try:
                shutil.copy(text + "/exam", os.getcwd())
            except:
                pass
            try:
                copy_tree(text + "/IMG", os.getcwd() + "/IMG")
            except:
                pass
            self.set_question_list()
            self.enable_all_fields()

        except  Exception as e:
           pass

    def enable_all_fields(self):
        self.end_exam_btn.setEnabled(True)
        self.answer_1.setEnabled(True)
        self.answer_2.setEnabled(True)
        self.answer_3.setEnabled(True)
        self.answer_4.setEnabled(True)

        self.start_exam_btn.hide()
        self.openFile()
        th = Thread(target=self.start_timer)
        th.start()

    def set_question(self, qmodelindex):
        self.finish_btn.setEnabled(False)
        # * get question id #
        self.item = self.skiped_question_listWidget.currentRow()
        self.questionID = int(self.item) + 1

        # * get question and question type  and correct answer from sql *#
        questionSQL = f"""SELECT  question,questionType,correctAnswer,questionIMG
                          FROM questions
                          WHERE  questionId ={self.questionID}
                       """
        self.db_connecton()
        self.cur.execute(questionSQL)
        data = self.cur.fetchall()
        self.con.close()
        self.question = data[0][0]
        self.questionType = data[0][1]
        self.corretAnswer = data[0][2]
        self.questionIMG = data[0][3]

        # * set question in form *#
        self.question_label.setText(self.question)
        self.q_img.setPixmap(QPixmap(self.questionIMG))

        # * calling function to setup answers *#
        self.set_answer()
        self.enable_answer_btns()

    def disable_answer_btns(self):
        self.answer_1.setEnabled(False)
        self.answer_2.setEnabled(False)
        self.answer_3.setEnabled(False)
        self.answer_4.setEnabled(False)

    def enable_answer_btns(self):
        self.answer_1.setEnabled(True)
        self.answer_2.setEnabled(True)
        self.answer_3.setEnabled(True)
        self.answer_4.setEnabled(True)

    def empty_fields(self):
        self.question_label.setText("")
        self.answer_1.setText("")
        self.answer_2.setText("")
        self.answer_3.setText("")
        self.answer_4.setText("")
        self.q_img.setPixmap(QPixmap(""))

    def set_answer(self):
        # * setup fields to match question type *#
        if self.questionType == 1:
            self.answer_3.hide()
            self.answer_4.hide()
        elif self.questionType == 0:
            self.answer_3.show()
            self.answer_4.show()

        answerSQL = f"""
                        SELECT answer_1,answer_2,answer_3,answer_4
                        FROM Answers 
                        WHERE AnswerId = {self.questionID}

                     """
        # * get answers from dataBase *#
        self.db_connecton()
        self.cur.execute(answerSQL)
        data = self.cur.fetchall()
        self.con.close()
        self.fistAnswer = data[0][0]
        self.secondAnswer = data[0][1]
        self.thirdAnswer = data[0][2]
        self.fourthAnswer = data[0][3]

        # * show answers in form *#
        self.answer_1.setText(self.fistAnswer)
        self.answer_2.setText(self.secondAnswer)
        self.answer_3.setText(self.thirdAnswer)
        self.answer_4.setText(self.fourthAnswer)

    def updete_exel_sheet(self):

        # * checking correct answer * #
        try:
            if self.corretAnswer == 'answer_1':
                self.corretAnswer_text = self.answer_1.text()
            elif self.corretAnswer == 'answer_2':
                self.corretAnswer_text = self.answer_2.text()
            elif self.corretAnswer == 'answer_3':
                self.corretAnswer_text = self.answer_3.text()
            elif self.corretAnswer == 'answer_4':
                self.corretAnswer_text = self.answer_4.text()
        except:
            pass
        # * defining  row numbers
        A = f'A{self.row_num}' # ==> question number
        B = f'B{self.row_num}' # ==> student answer
        C = f'C{self.row_num}' # ==> correct answer
        D = f'D{self.row_num}' # ==> answering time
        E = f'E{self.row_num}' # ==>

        ws2_A = f'A{self.ws2_row_num}'
        ws2_B = f'B{self.ws2_row_num}'

        # * write data in exel sheet * #
        self.format = self.wb.add_format({'align': 'center', 'bold': False, 'border': 2})

        self.ws1.write(A, self.questionID, self.format)
        self.ws1.write(B, self.student_answer_text, self.format)
        self.ws1.write(C, self.corretAnswer_text, self.format)
        # * setup date format * #
        self.answer_time = str(datetime.datetime.now())
        self.answer_time = list(self.answer_time.split('.'))
        self.answer_time = self.answer_time[0]
        self.ws1.write(D, self.answer_time, self.format)

        self.ws2.write(ws2_A, self.questionID, self.format)
        self.ws2.write(ws2_B, self.question, self.format)

        self.row_num += 1
        self.ws2_row_num += 1

    def check_sender(self):
        radioButton = self.sender()
        self.student_answer = radioButton.objectName()
        self.student_answer_text = radioButton.text()
        self.finish_btn.setEnabled(True)

    def check_Answer(self):
        # * disable a previous question *#
        items = self.skiped_question_listWidget.selectedItems()
        for i in items:
            i.setFlags(Qt.NoItemFlags)

        # * enable and disable buttons *#
        self.skiped_question_listWidget.setEnabled(True)
        self.finish_btn.setEnabled(False)

        # * adding result to dictionary * # and  # * check answer *#

        if self.questionID in self.result_dict:
            QMessageBox.information(self, "خطأ", "لقد أجبت هذا السؤال مسبقاّ\n من فضلك أختر سؤالا أخر")
        else:
            if self.student_answer == self.corretAnswer:
                self.result_dict[self.questionID] = 1
            else:
                self.result_dict[self.questionID] = 0

            # * calling update_exel_sheet function * #
            self.updete_exel_sheet()

        # * disable answers buttons *#
        self.disable_answer_btns()


        # * Empty fields *#
        self.empty_fields()

        # * unCheck answer *#
        self.uncheck_answer()

    def uncheck_answer(self):
        self.answer_1.setChecked(False)
        self.answer_2.setChecked(False)
        self.answer_3.setChecked(False)
        self.answer_4.setChecked(False)

    def create_exel_sheet(self):
        self.wb = xlsxwriter.Workbook("degree.xlsx",{'default_date_format': 'dd/mm/yy hh:mm:ss'})
        self.ws1 = self.wb.add_worksheet()
        self.ws2 = self.wb.add_worksheet()

        self.merge_format = self.wb.add_format({'align': 'center', 'bold': True, 'border': 2})
        self.header_format = self.wb.add_format({'align': 'center', 'bold': True, 'border': 2})

        #self.ws2.write('A1', "الاسم:", self.header_format)
        self.ws2.write('B1', self.name, self.header_format)
        self.ws2.write('A3', "رقم السؤال", self.header_format)
        self.ws2.write('B3', "السؤال", self.header_format)

        self.ws2.set_column('A:A', 15)
        self.ws2.set_column('B:B', 70)

        self.ws1.set_column('A:A', 10)
        self.ws1.set_column('B:B', 27)
        self.ws1.set_column('C:C', 27)
        self.ws1.set_column('D:D', 22)


        self.ws1.write('A1', "الاسم :", self.header_format)
        self.ws1.merge_range('B1:D1', self.name, self.merge_format)

        self.ws1.write('A2', "الرقم :", self.header_format)
        self.ws1.merge_range('B2:D2', self.num, self.merge_format)

        self.ws1.write('A3', "التخصص :", self.header_format)
        self.ws1.merge_range('B3:D3', self.sec, self.merge_format)

        self.ws1.write('A4', "الدرجة :", self.header_format)
        self.ws1.merge_range('B4:D4', '', self.merge_format)

        self.ws1.write('A5', "النسبة :", self.header_format)
        self.ws1.merge_range('B5:D5', '', self.merge_format)

        self.ws1.write('A7', "رقم السؤال", self.header_format)
        self.ws1.write('B7', "إجابة الطالب", self.header_format)
        self.ws1.write('C7', "الإجابة الصحيحة", self.header_format)
        self.ws1.write('D7', "وقت الإجابةالسؤال", self.header_format)

    def end_exel(self):
        self.get_total_degree = "SELECT total_degrees FROM general WHERE id = 1;"
        self.db_connecton()
        self.cur.execute(self.get_total_degree)
        self.data = self.cur.fetchall()
        self.total_degree = int(self.data[0][0])
        self.degree_for_eche_question = self.total_degree / self.question_num
        self.student_degree = self.degree_for_eche_question * len(self.student_res)
        self.con.close()

        self.copyRight_format = self.wb.add_format({'align': 'center','font_name': 'Cambria', 'font_size': 12, 'bold': False, 'border': 1})
        self.ws1.write('B4', self.student_degree, self.header_format)
        self.ws1.write('B5', str(self.percent)+"%", self.header_format)
        self.ws1.merge_range(f'A{self.row_num}:D{self.row_num}', "جميع الحقوق محفوظة للهيئة القومية لسكك حديد مصر ©", self.header_format)
        self.ws2.merge_range(f'A{self.ws2_row_num}:B{self.ws2_row_num}', "جميع الحقوق محفوظة للهيئة القومية لسكك حديد مصر©", self.header_format)

        self.ws1.merge_range(f'B{self.row_num+2}:D{self.row_num+2}', " <-- MarwanMohamed-AbShafi -->", self.copyRight_format)
        self.ws1.write(f'A{self.row_num+2}', "created by", self.header_format)
        self.ws2.write(f'B{self.ws2_row_num+2}', " <-- MarwanMohamed-AbShafi -->", self.copyRight_format)
        self.ws2.write(f'A{self.ws2_row_num+2}', "created by", self.header_format)
        self.wb.close()

    def openFile(self):
        with open('data.txt', 'r', encoding='utf-8') as opened_file:
            data = [line.rstrip() for line in opened_file]
        self.name = data[0]
        self.num = data[1]
        self.sec = data[2]
        self.db_connecton()
        sql = f"""UPDATE studentInfo
         set studentName = '{self.name}',
             studentNum = '{self.num}',
             section = '{self.sec}'
         WHERE id = 1; """
        self.cur.execute(sql)
        self.con.commit()
        self.con.close()
        self.create_exel_sheet()

 # * printing class *#

class print_mainApp(QMainWindow, print_Form):
    def __init__(self, parent=None):
        super(print_mainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()
        self.show_data()

    def db_connecton(self):
        self.con = sqlite3.connect("exam")
        self.cur = self.con.cursor()

    def Handel_UI(self):
        self.setFixedSize(510, 595)

    def Handel_Buttons(self):
        self.print_btn.clicked.connect(self.printing)

    def show_data(self):
        self.get_exam_name_sql = "SELECT exam_name,total_degrees FROM general WHERE id = 1;"
        self.get_data_sql = " SELECT * FROM studentInfo WHERE id = 1;"
        self.total_questions_sql = "SELECT question_num FROM general WHERE id = 1;"
        self.db_connecton()
        self.cur.execute(self.get_exam_name_sql)
        general = self.cur.fetchall()
        examName = general[0][0]
        self.con.close()
        self.exam_name_label.setText(str(examName))
        self.total_degree = general[0][1]

        self.db_connecton()
        self.cur.execute(self.get_data_sql)
        self.data = self.cur.fetchall()
        self.con.close()
        self.db_connecton()
        self.cur.execute(self.total_questions_sql)
        self.datat = self.cur.fetchall()
        self.con.close()
        self.total_questions = self.datat[0][0]
        self.full_name = self.data[0][1]
        self.student_num = str(self.data[0][2])
        self.section = self.data[0][3]

        self.degree_for_eche_question = self.total_degree/self.total_questions

        self.degree = str(self.data[0][4] * self.degree_for_eche_question)
        self.percent = round(self.data[0][5], 2)
        self.percent = str(self.percent)+" %"

        self.name_lablel.setText(self.full_name)
        self.idNum_label.setText(self.student_num)
        self.section_label.setText(self.section)
        self.degree_label.setText(self.degree)
        self.percent_label.setText(self.percent)

    def printing(self):
        os.startfile("degree.xlsx", "print")
        self.close()



def main():
    app = QApplication(sys.argv)
    Mainwindow = mainApp()
    Mainwindow.show()
    app.exec_()


if __name__ == '__main__':
    main()


