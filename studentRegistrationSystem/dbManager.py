import pickle

def db_load():
    try:
        with open("student_db", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def db_write(student_db):
    with open("student_db", "wb") as f:
        pickle.dump(student_db, f)