import time, os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def write(string):
    for char in string:
        print(char, end="", flush=True)
        time.sleep(0.015)
    print()