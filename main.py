from models import subject
from config import db_connection
import pyfiglet
import os
from dotenv import load_dotenv

#Load Environment variables
load_dotenv()

def create_banner(text, font="standard"):
    banner = pyfiglet.figlet_format(text, font=font)
    print(banner)

mydb = db_connection.connect_to_database()
dbcursor = mydb.cursor()

def main():

    campus_subjects = subject.subjects(mydb, dbcursor)
    create_banner("OUSL Tool")
    while True:
        print("\n")
        print("1. All Subjects")
        print("2. Lookup Subject")
        print("3. Add Subject")
        print("4. Delete Subject")
        print("5. Quit")

        choice = input("Enter a choice : ")

        if (choice == '1'):
            campus_subjects.all_subjects()
        elif(choice == '2'):
            code = input("Enter Code : ")
            campus_subjects.lookup_subject(code)
        elif(choice == '3'):
            code = input("Enter Code : ")
            name = input("Enter name : ")
            campus_subjects.add_subject(code, name)
        elif(choice == '4'):
            code = input("Enter a code : ")
            campus_subjects.delete_subject(code)
        elif(choice == '5'):
            print("Bye!")
            break
        else:
            print("Please Enter a valid choice")

main()
