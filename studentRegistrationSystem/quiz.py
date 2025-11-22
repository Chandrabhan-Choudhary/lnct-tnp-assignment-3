import time
import consoleMod as Con
import quizMod as q
import dbManager as dbmg
import student_db as sdb
import login

def quiz():
    category, score, time_string = q.start_quiz()

    Con.clear()
    current_highscore = sdb.student_db[login.logged_user]["quiz"][category][0]

    if(score > current_highscore):
        sdb.student_db[login.logged_user]["quiz"][category] = [score, time_string]
        dbmg.db_write(sdb.student_db)
        Con.write("Quiz Completed. New Highscore("+str(score)+")")
    else:
        Con.write(f"Quiz Completed. Your score: {score} (Highscore: {current_highscore})")
    time.sleep(2)