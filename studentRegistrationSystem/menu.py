import consoleMod as Con
import student_db as sdb
from registration import register
import login
from showProfile import show_profile
from updateProfile import update_profile
from quiz import quiz
from quizResults import quiz_results
from logout import logout

def screen():
    Con.write("Welcome to LNCT")
    response = input("1. Registration\n2. Login\n3. Exit\nSelect option(1-3): ")
    if response == '1':
        register()
    elif response == '2':
        login.login() 
    elif response == '3':
        Con.write("Terminating..")
        exit()
    else:
        return "error"

def logged_in_screen():
    Con.write("Welcome to LNCT, " + sdb.student_db[login.logged_user]["first_name"])
    response = input("1. Profile\n2. Update profile\n3. Take Quiz\n4. Logout\n5. Exit\nSelect option(1-5): ")

    if response == '1':
        show_profile()
    elif response == '2':
        update_profile()
    elif response == '3':
        quiz()
    elif response == '4':
        logout()
    elif response == '5':
        Con.write("Terminating..")
        exit()
    else:
        return "error"

def admin_screen():
    Con.write("ADMIN MENU")
    response = input("1. Quiz Marks\n2. Logout\n3. Exit\nSelect option(1-3): ")

    if response == '1':
        quiz_results()
    elif response == '2':
        logout()
    elif response == '3':
        Con.write("Terminating..")
        exit()
    else:
        return "error"

def menu():
    while True:
        Con.clear()
        if(login.logged_user == "admin"):
            log = admin_screen()
        elif(login.logged):
            log = logged_in_screen()
        else:
            log = screen()
        if log == "error":
            continue