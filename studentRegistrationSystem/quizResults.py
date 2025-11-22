import consoleMod as Con
import student_db as sdb

def quiz_results():
    Con.clear()
    Con.write("Enrollment No.   Category    Marks/Total    Datetime")
    for profile in sdb.student_db.values():
        enrollment = profile["enrollment"]
        for category, details in profile["quiz"].items():
            if(details[1]):
                print(f"{enrollment}\t {category}\t\t {details[0]}\t    {details[1]}")
    input("\nPress enter to go back.")