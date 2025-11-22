import time
import login 

def logout():
    print("-"*20)
    choice = input("Do you really want to logout?[y]: ").lower()
    if(choice == "y"):
        login.logged_user = ""
        login.logged = False
        print("Logging out..")
    else:
        print("Going back to main menu.")
    time.sleep(2)