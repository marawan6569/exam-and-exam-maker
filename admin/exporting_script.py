import sqlite3
import os
import shutil

Cpath = os.getcwd()

path_dic = {
    'dataBase_pass' : Cpath + "/student/exam",
    'pannar_pass': Cpath + "/student/pannar.jpg",
    'exam_form_pass': Cpath + "/student/exam_form.ui",
    'exam_pass': Cpath + "/student/exam.py",
    'login_form_pass': Cpath + "/student/login_form.ui",
    'login_pass': Cpath + "/student/login.py",
    'print_form_pass': Cpath + "/student/print_form.ui",
    'print_pass': Cpath + "/student/print.py"
}

def get_saveLocation():
    global saveLocation, examName
    get_location_sql = "SELECT newExamSaveLocation,exam_Name FROM general WHERE id = 1;"
    con = sqlite3.connect('./student/exam')
    cur = con.cursor()
    cur.execute(get_location_sql)
    data = cur.fetchall()
    saveLocation = data[0][0]
    examName = data[0][1]
    global folder
    folder = str(saveLocation + '/' + examName)
    con.close()

def copying_files():
    for key in path_dic:
        shutil.copy(path_dic[key], folder)

get_saveLocation()
copying_files()