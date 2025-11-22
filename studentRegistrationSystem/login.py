import time
import student_db as sdb
import consoleMod as Con

logged_user = ""
logged = False

def login():
    global logged_user, logged
    print("-"*20)
    Con.write("Enter credentials.")
    log_uname = input("Username: ").lower()
    if(log_uname in sdb.student_db):
        log_password = input("Password: ")
        if(log_password == sdb.student_db[log_uname]["password"]):
            logged_user = log_uname
            logged = True
            print("Logging in..")
        else:
            print("Wrong Password!")
    elif(log_uname == "admin"):
        log_password = input("Password: ")
        if(log_password == "1234"):
            logged_user = log_uname
            logged = True
            print("Logging in..")
        else:
            print("Wrong Password!")
    else:
        print("User does not exist!")
    time.sleep(2)