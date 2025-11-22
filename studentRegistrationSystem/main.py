from menu import menu
import student_db as sdb
import dbManager as dbmg
import consoleMod as Con

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        Con.write("\nProgram interrupted by user. Terminating...")
    finally:
        Con.write("\nSaving database...")
        dbmg.db_write(sdb.student_db)
        Con.write("Save complete. Goodbye.")