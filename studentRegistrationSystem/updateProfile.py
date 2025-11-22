import time
import consoleMod as Con
import login
import dbManager as dbmg
from student_db import student_db, format

def update_profile():
    if(login.logged):
        Con.clear()

        temp = list(student_db[login.logged_user].values())
        keys = list(student_db[login.logged_user].keys())
        Con.write("Select entry you want to update.")
        
        for i in range(1, 11):
            print(f"{format[i]}: {temp[i]}")
            
        option_str = input("Select option(1-10): ")
        print("-"*20)
        
        if(option_str.isdigit()):
            option = int(option_str)
        else:
            Con.write('Invalid Option. Please enter a number.')
            time.sleep(2)
            return

        if(option in [1, 2, 3, 8, 9]):
            temp_str = input(f"Enter {format[option]}: ")
            student_db[login.logged_user][keys[option]] = temp_str
            Con.write("Updated.")
        elif(option == 4):
            temp_str = input("Enter Branch (CS|EC|AD|ME|CE): ")
            if(temp_str not in ["CS", "EC", "AD", "ME", "CE"]):
                Con.write("Invalid Branch.")
            else:
                student_db[login.logged_user][keys[option]] = temp_str
                Con.write("Updated Branch.")
        elif(option == 5):
            temp_str = input("Enter Enrollment No: ")
            current_branch = student_db[login.logged_user]["branch"]
            if(current_branch not in temp_str):
                Con.write("Branch does not match based on enrollment. Update Branch first.")
            else:
                student_db[login.logged_user][keys[option]] = temp_str
                Con.write("Updated Enrollment No.")
        elif(option in [6, 7, 10]):
            try:
                temp_int = int(input(f"Enter {format[option]}: "))
                student_db[login.logged_user][keys[option]] = temp_int
                Con.write("Updated.")
            except ValueError:
                Con.write("Invalid input. Please enter a number.")
        else:
            Con.write('Invalid Option.')
            
        dbmg.db_write(student_db)
    else:
        print("User not logged in.")
    time.sleep(2)