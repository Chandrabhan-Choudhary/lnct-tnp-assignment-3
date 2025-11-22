import consoleMod as Con
import student_db as sdb
import dbManager as dbmg

def register():
    while True:
        uname = input("Username: ").lower()
        if(uname in sdb.student_db.keys()):
            Con.write("This user name already exists. Try Again.")
            continue

        password = input("Password: ")
        break
    
    while True:
        Con.clear()
        Con.write("Enter details for "+uname)
        first_name = input("First name: ")
        middle_name = input("Middle Name: ")
        last_name = input("Last Name: ")
        
        branch = input("Branch (CS|EC|AD|ME|CE): ") 
        
        if(branch not in ["CS", "EC", "AD", "ME", "CE"]):
            Con.write("Invalid Branch.")
            continue
        
        enrollment = input("Enrollment No: ")
        if(branch not in enrollment):
            Con.write("Branch does not match based on enrollment.")
            continue

        try:
            roll = int(input("Roll No: "))
            phone_no = int(input("Phone No: "))
            pincode = int(input("Pincode: "))
        except ValueError:
            Con.write("Roll No, Phone No, and Pincode must be numbers.")
            continue

        email = input("Email: ")
        address = input("Address: ")

        choice = input("Are these details correct?[y]: ").lower()
        if(choice == "y"):
            sdb.student_db[uname] = {
                "password": password,
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "branch": branch,
                "enrollment": enrollment,
                "roll": roll,
                "phone_no": phone_no,
                "email": email,
                "address": address,
                "pincode": pincode,
                "quiz": {
                    "DSA": [0, ""],  
                    "DBMS": [0, ""],
                    "Python": [0, ""]
                }
            }
            dbmg.db_write(sdb.student_db)
            break