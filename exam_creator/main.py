# -*- coding: utf-8 -*-
import os
import shutil
import sqlite3
import sys
from distutils.dir_util import copy_tree, remove_tree
from os import path
from shutil import rmtree
from webbrowser import open
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from main_form import Ui_MainWindow
from setting_form import Setting_Ui_Form
from exporting_form import Exporting_Ui_Form

# * exam creator class * #

class mainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.id = 1
        self.index = 1
        self.exitQuestionList = []
        self.Handel_UI()
        self.Handel_Buttons()
        self.hide_answer_fields()
        self.disable_all_fields()
        self.enable_add_question_btn()
        self.update_btn.hide()
        self.question_IMG_path = ""

    def db_connection(self, sql):
        self.con = sqlite3.connect(os.getcwd()+"/student/exam")
        self.cur = self.con.cursor()
        self.cur.execute(sql)

    def Handel_UI(self):
        self.setFixedSize(940, 630)

    def Handel_Buttons(self):
        self.open_exam_btn.clicked.connect(self.open_exam)
        self.New_exam_btn.clicked.connect(self.new_exam)
        self.true_or_false_Rbtn.clicked.connect(self.true_or_false_question)
        self.choose_Rbtn.clicked.connect(self.choose_question)
        self.add_question_btn.clicked.connect(self.add_question)
        self.setting_btn.clicked.connect(self.setting)
        self.add_img_btn.clicked.connect(self.questionIMG)
        self.add_question_btn.clicked.connect(self.reset_question_Img)
        self.clear_img_btn.clicked.connect(self.reset_question_Img)

        self.first_answer_Rbtn.clicked.connect(self.enable_add_question_btn)
        self.second_answer_Rbtn.clicked.connect(self.enable_add_question_btn)
        self.third_answer_Rbtn.clicked.connect(self.enable_add_question_btn)
        self.fourth_answer_Rbtn.clicked.connect(self.enable_add_question_btn)

        self.export_btn.clicked.connect(self.export)
        self.setting_btn.clicked.connect(self.setting)

        self.question_list.clicked.connect(self.get_old_question_id)

        # * connect menus to function * #
        self.action_new.triggered.connect(self.new_exam)
        self.action_open.triggered.connect(self.open_exam)
        self.action_export.triggered.connect(self.export)
        self.action_setting.triggered.connect(self.setting)
        self.action_close.triggered.connect(self.close)
        self.action_about.triggered.connect(self.my_facebook)
        self.about_btn.clicked.connect(self.my_facebook)

        self.action_facebook.triggered.connect(self.my_facebook)
        self.action_twitter.triggered.connect(self.my_twitter)
        self.action_instagram.triggered.connect(self.my_instagram)

    def Handel_browes(self):
        self.saveLocation = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

    def set_all_fields_null(self):
        self.qusetion_textEdit_field.setText("")
        self.first_answer_lineEdit.setText("")
        self.second_answer_lineEdit.setText("")
        self.third_answer_lineEdit.setText("")
        self.fourth_answer_lineEdit.setText("")
        self.true_or_false_Rbtn.setChecked(False)
        self.choose_Rbtn.setChecked(False)
        self.qusetion_img_lable.setPixmap(QPixmap(""))

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
        self.setting_btn.setEnabled(True)
        self.qusetion_textEdit_field.setEnabled(True)
        self.true_or_false_Rbtn.setEnabled(True)
        self.choose_Rbtn.setEnabled(True)
        self.add_img_btn.setEnabled(True)
        self.action_export.setEnabled(True)
        self.action_export_nodataBase.setEnabled(True)
        self.action_setting.setEnabled(True)

    def new_exam_script(self):
        fName = "/student"
        fPass = os.getcwd() + "/student"
        try:
            rmtree(os.getcwd() + "/student")
        except:
            pass
        try:
            os.makedirs(os.getcwd() + fName)
            os.makedirs(os.getcwd() + fName + "/IMG")
        except:
            pass

    def new_exam(self):
        self.new_exam_script()
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
                `question_num`	INTEGER NOT NULL
            ); """
        self.question_table_sql = """ CREATE TABLE IF NOT EXISTS `questions` (
                `questionId`	INTEGER PRIMARY KEY AUTOINCREMENT,
                `question`	TEXT NOT NULL,
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
        self.set_gneral_sql = "INSERT INTO general VALUES(1,' ',1,1,1)"
        self.set_student_info_sql = "INSERT INTO studentInfo VALUES(1,' ',1,' ',1,1)"

        try:
            self.db_connection(self.answer_table_sql)
            self.con.commit()
            self.con.close()
        except Exception as AE:
            pass
        try:
            self.db_connection(self.genral_table_sql)
            self.con.commit()
            self.con.close()
        except Exception as GE:
            pass
        try:
            self.db_connection(self.question_table_sql)
            self.con.commit()
            self.con.close()
        except Exception as QE:
            pass
        try:
            self.db_connection(self.studentInfo_table_sql)
            self.con.commit()
            self.con.close()
        except Exception as SE:
            pass
        try:
            self.db_connection(self.set_gneral_sql)
            self.con.commit()
            self.con.close()
        except Exception as ge2:
            pass
        try:
            self.db_connection(self.set_student_info_sql)
            self.con.commit()
            self.con.close()
        except Exception as se2:
            pass

        self.enabal_all_fields()

    def open_exam(self):
        try:
            try:
                rmtree(os.getcwd()+"/student")
            except:
                pass
            try:
                os.makedirs(os.getcwd()+"/student")
                os.makedirs(os.getcwd() + "/student/IMG")
            except:
                pass
            text = QFileDialog.getExistingDirectory(self, "select the exam")
            if text != '':
                database_path = text +"/exam"
                img_path = text + "/IMG"
                if os.path.isfile(database_path) and os.path.isdir(img_path):
                    try:
                        shutil.copy(database_path, os.getcwd()+"/student")
                        copy_tree(img_path, os.getcwd()+"/student/IMG")
                    except:
                        pass
                    try:
                        sql = "SELECT questionId FROM questions "
                        self.db_connection(sql)
                        data = self.cur.fetchall()
                        for i in range(len(data)):
                            self.question_list.addItem("السؤال رقم: " + str(i+1))

                    except Exception as e:
                        QMessageBox.warning(self, 'خطأ', str(e))
                    self.enabal_all_fields()
                else:
                    QMessageBox.warning(self, 'خطأ', 'هذا المجلد لا يحتوي علي امتحان تم انشاءه مسبقا أو ربما هناك بعص الملفات المفقودة')
                    self.disable_all_fields()
            else:
                QMessageBox.warning(self, 'خطأ', 'من فضلك اختر الامتحان الذي تريد فتحه او قم بانشاء امتحان جديد')
                self.disable_all_fields()
        except:
            pass

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
            self.text = str(self.img_place[0])

            a = shutil.copy(self.text, os.getcwd()+"/student/IMG")
            self.name = (self.text[2:].split(',')[0].replace("'", ""))
        except:
            pass

    def questionIMG(self):
        try:
            self.Handel_Browse()
            self.question_IMG_path = self.name
            self.question_IMG_path = list(self.question_IMG_path.split('/'))
            self.question_IMG_path = str("./IMG/" + self.question_IMG_path[-1])
            self.img_path_label.setText(self.question_IMG_path)
            self.qusetion_img_lable.setText("")
            self.qusetion_img_lable.setPixmap(QPixmap(self.text))
        except:
            pass

    def add_question(self):
        self.question_IMG =str(self.question_IMG_path)
        self.queston_text = self.qusetion_textEdit_field.toPlainText()
        self.first_answer_text = self.first_answer_lineEdit.text()
        self.second_answer_text = self.second_answer_lineEdit.text()
        self.third_answer_text = self.third_answer_lineEdit.text()
        self.fourth_answer_text = self.fourth_answer_lineEdit.text()
        self.question_type = 0
        self.correct_answer = 0

        if self.queston_text == "":
            QMessageBox.information(self, "خطأ", "please enter question")

        if not self.true_or_false_Rbtn.isChecked() and not self.choose_Rbtn.isChecked():
            QMessageBox.information(self, "خطأ", "please choose question type")

        elif self.choose_Rbtn.isChecked():
            self.question_type = 0

        elif self.true_or_false_Rbtn.isChecked():
            self.question_type = 1

        else:
            QMessageBox.information(self, "خطأ", "please choose question type")

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
                            pass
        # * getting previous questions text * #
        prevQuestionSQL = "SELECT question FROM questions;"
        self.db_connection(prevQuestionSQL)
        prevQuestionData = self.cur.fetchall()
        self.con.close()

        self.index += 1
        if self.index == self.id:
            self.add_question_btn.setEnabled(False)
            self.question_list.addItem("السؤال رقم: " + str(self.id - 1))
        else:
            self.index = self.id


        self.question_IMG_path = ""

        self.set_all_fields_null()

    def setting(self):
        self.window2 = setting_App()
        self.window2.show()
        self.export_btn.setEnabled(True)

    def export(self):
        self.window3 = exporting_App()
        self.window3.show()

    def reset_question_Img(self):
        self.qusetion_img_lable.setPixmap(QPixmap("/"))
        self.qusetion_img_lable.setText("يمكنك أن تضيف صورة بالضغط علي الزر أدناه")
        self.img_path_label.setText('')

    def get_old_question_id(self, qmodelindex):
        # * getting question id * #
        item = self.question_list.currentRow()
        self.questionID = item + 1

        # * calling getting old question data function * #
        self.get_old_question_data()

    def get_old_question_data(self):
        # * connecting to database and get (question data and correct answer) from questions table * #
        questionSQL = f"""
                                SELECT question,questionType,questionIMG,correctAnswer
                                FROM questions 
                                WHERE questionId = {self.questionID};
                               """
        self.db_connection(questionSQL)
        question_data = self.cur.fetchall()
        self.con.close()

        # *  assign question data to variables * #
        self.old_question_text = question_data[0][0]
        self.old_question_type = question_data[0][1]
        self.old_question_IMG = question_data[0][2]
        self.old_correct_answer = question_data[0][3]



        # * editing question img path to be shown * #
        self.showen_img = str(self.old_question_IMG).replace('./', './student/')

        # * connect to database and get answers from Answers table * #
        answerSQL = f"""
                        SELECT answer_1,answer_2,answer_3,answer_4 
                        FROM Answers
                        WHERE AnswerId = {self.questionID};
                     """
        self.db_connection(answerSQL)
        answer_data = self.cur.fetchall()
        self.con.close()

        # * assign answers data to variables * #
        self.old_first_answer = answer_data[0][0]
        self.old_second_answer = answer_data[0][1]
        self.old_third_answer = answer_data[0][2]
        self.old_fourth_answer = answer_data[0][3]

        # * calling setup form function * #
        self.setup_form_for_old_question()

    def setup_form_for_old_question(self):
        # * setup question text and question img and question img path * #
        self.qusetion_textEdit_field.setText(self.old_question_text)
        self.qusetion_img_lable.setPixmap(QPixmap(self.showen_img))
        self.img_path_label.setText(str(self.old_question_IMG))
        # * setup question type * #
        if 1 == 1:
            if self.old_question_type == 0:
                self.choose_Rbtn.click()
            elif self.old_question_type == 1:
                self.true_or_false_Rbtn.click()

        # * setup correct answer * #
        if 1 == 1:
            if self.old_correct_answer == 'answer_1':
                self.first_answer_Rbtn.click()
            elif self.old_correct_answer == 'answer_2':
                self.second_answer_Rbtn.click()
            elif self.old_correct_answer == 'answer_3':
                self.third_answer_Rbtn.click()
            elif self.old_correct_answer == 'answer_4':
                self.fourth_answer_Rbtn.click()

        # * setup answers * #
        self.first_answer_lineEdit.setText(self.old_first_answer)
        self.second_answer_lineEdit.setText(self.old_second_answer)
        self.third_answer_lineEdit.setText(self.old_third_answer)
        self.fourth_answer_lineEdit.setText(self.old_fourth_answer)

        # * show update_btn and connect it to updating function * #
        self.update_btn.show()
        self.update_btn.clicked.connect(self.update_question)

    def get_updated_question_new_data(self):
        # * assign new question text and answers and question img  to variables * #
        self.new_question_text = self.qusetion_textEdit_field.toPlainText()
        self.new_question_IMG = self.img_path_label.text()

        self.new_first_answer = self.first_answer_lineEdit.text()
        self.new_second_answer = self.second_answer_lineEdit.text()
        self.new_third_answer = self.third_answer_lineEdit.text()
        self.new_fourth_answer = self.fourth_answer_lineEdit.text()

        # * setup the correct answer * #
        self.new_correct_answer = self.old_correct_answer
        if True:
            if self.first_answer_Rbtn.isChecked():
                self.new_correct_answer = 'answer_1'

            elif self.second_answer_Rbtn.isChecked():
                self.new_correct_answer = 'answer_2'

            elif self.third_answer_Rbtn.isChecked():
                self.new_correct_answer = 'answer_3'

            elif self.fourth_answer_Rbtn.isChecked():
                self.new_correct_answer = 'answer_4'

        # * setup the question type * #
        self.new_question_type = self.old_question_type
        if True:
            if self.true_or_false_Rbtn.isChecked():
                self.new_question_type = 1

            elif self.choose_Rbtn.isChecked():
                self.new_question_type = 0

    def update_question(self):
        # * hide update_btn *
        self.update_btn.hide()

        # * calling getting data function * #
        self.get_updated_question_new_data()

        # * send updated question's data to dataBase * #
        updateQuestionDataSQL = f"""
                                UPDATE questions 
                                SET question = '{self.new_question_text}',
                                    correctAnswer = '{self.new_correct_answer}',
                                    questionType = '{self.new_question_type}',
                                    questionIMG = '{self.new_question_IMG}'         
                                WHERE questionId = {self.questionID};
                              """
        self.db_connection(updateQuestionDataSQL)
        self.con.commit()
        self.con.close()

        # * send updated question's answers to database * #
        updateQuestionAnswerSQL = f"""
                                    UPDATE Answers
                                    SET answer_1 = '{self.new_first_answer}',
                                        answer_2 = '{self.new_second_answer}',
                                        answer_3 = '{self.new_third_answer}',
                                        answer_4 = '{self.new_fourth_answer}'
                                    WHERE AnswerId = {self.questionID};
                                   """
        self.db_connection(updateQuestionAnswerSQL)
        self.con.commit()
        self.con.close()

    def my_facebook(self):
        open("https://www.facebook.com/marwanmo7amed8", new=2)

    def my_instagram(self):
        open('https://www.instagram.com/marwan_mohamed_0_0/', new=2)

    def my_twitter(self):
        pass


# * setting class * #

class setting_App(QMainWindow, Setting_Ui_Form):
    def __init__(self, parent=None):
        super(setting_App, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()

    def Handel_UI(self):
        self.setFixedSize(470, 200)

    def Handel_Buttons(self):
        self.save_btn.clicked.connect(self.send_data)

    def db_connection(self, sql):
        self.con = sqlite3.connect("./student/exam")
        self.cur = self.con.cursor()
        self.cur.execute(sql)

    def send_data(self):
        self.exam_name = self.exam_name_LD.text()
        self.question_num = self.question_num_sp.value()
        self.degree = self.degree_sp.value()
        self.exam_time = self.exam_time_sp.value()
        self.send_data_sql = f"""
                                UPDATE general  
                                  SET  exam_Name = '{self.exam_name}',
                                       exam_time = {self.exam_time},
                                       total_degrees = {self.degree},
                                       question_num = {self.question_num}
                                  WHERE id = 1;
                             """
        if self.exam_name != "":
            self.db_connection(self.send_data_sql)
            self.con.commit()
            self.con.close()
            self.close()
        else:
            QMessageBox.information(self, "خطأ", "برجأء إدخال البيانات")

# * exporting class * #

class exporting_App(QMainWindow, Exporting_Ui_Form):
    def __init__(self, parent=None):
        super(exporting_App, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()

    def db_connection(self):
        self.exam_name_sql = "SELECT exam_Name FROM general WHERE id = 1;"

        self.con = sqlite3.connect("./student/exam")
        self.cur = self.con.cursor()
        self.cur.execute(self.exam_name_sql)

        self.data = self.cur.fetchall()
        self.con.close()
        self.data = self.data[0][0]

    def Handel_UI(self):
        self.setFixedSize(415, 300)

    def Handel_Buttons(self):
        self.browes_btn.clicked.connect(self.Handel_Browes)
        self.export_btn.clicked.connect(self.copy_files)

    def Handel_Browes(self):
        self.savePass = str(QFileDialog.getExistingDirectory(self, "اختر مكان الحفظ"))
        self.save_location_LD.setText(self.savePass)
        self.savePass = self.save_location_LD.text()

    def copy_files(self):
        self.srcPass  = os.getcwd()+"/studentT"
        self.dstPass = os.getcwd()+"/student"
        self.db_connection()
        try:
            os.rename(self.dstPass, self.data)
            copy_tree(os.getcwd()+"/"+self.data, self.savePass+"/"+self.data)
            remove_tree(os.getcwd()+"/"+self.data)
            QMessageBox.information(self, "تم", "تمت العملية بنجاح")

        except Exception  as e:
            QMessageBox.information(self, "فشل", str(e))


def main():
    app = QApplication(sys.argv)
    Mainwindow = mainApp()
    Mainwindow.show()
    app.exec_()


if __name__ == '__main__':
    main()
