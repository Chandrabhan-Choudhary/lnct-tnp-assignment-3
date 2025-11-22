import time
import student_db as sdb
import consoleMod as Con
import login
from student_db import format

def show_profile():
    if(login.logged):
        Con.clear()
        temp = list(sdb.student_db[login.logged_user].values())
        Con.write(temp[1]+"'s Profile")
        print("-"*20)
        for i in range(1, 11):
            print(f"{format[i]}: {temp[i]}")
        input("Press enter to go back.")
    else:
        print("User not logged in.")
        time.sleep(2)