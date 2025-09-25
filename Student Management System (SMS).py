# Project Overview : 
# Creating a simple SMS(student management system) where users can:
# Add new student records.
# View all student details.
# Search for a student.
# Edit a student's record.
# Delete a record.

import sys

Students = dict()
Students_id = set()

def add_record():
    print("\n___Adding a Student Record___")
    s_name = input("Enter the name of the student : ")
    s_age = int(input("Enter the age fo the student : "))
    s_class = input("Enter the Class of the student : ")
    s_grade = input("Enter the grade of the previous class : ")
    s_id = int(input("Enter the student ID to proceed : "))
    if s_id not in Students_id:
        Students[s_id] = {
            "Name": s_name,
            "Age": s_age,
            "Class": s_class,
            "Grade": s_grade
        }
        Students_id.add(s_id)
        print("Successfully Added a new Student Record with ID :",s_id)
    else:
        print("Invalid Student ID ( The ID must not already present in the record , please make sure before adding a new record )!!!")

def view():
    print("\n___The Students Record___")
    if len(Students)==0:
        print("NO RECORD PRESENT (Please add a new record)!!!")
    else:
        print("-------DETAILS-------")
        for id,details in Students.items():
            print("ID".center(10),id)
            for ele in details:
                print(f"{ele}".center(10),details[ele])
            print("-"*21)

def edit():
    print("\n___Update a Record___")
    id_edit = int(input("Enter the ID of the record to update : "))
    if id_edit in Students_id:
        update = input("What do you want to update (Name | Age | Class | Grade) : ")
        match update.lower():
            case "name": 
                Students[id_edit]["Name"] = input("Enter the new name : ")
                print("Successfully Updated the Name in Record")
            case "age":
                Students[id_edit]["Age"] = int(input("Enter the new age : "))
                print("Successfully Updated the age in Record")
            case "class":
                Students[id_edit]["Class"] = input("Enter the new class : ")
                print("Successfully Updated the class in Record")
            case "grade":
                Students[id_edit]["Grade"] = input("Enter the new grade : ")
                print("Successfully Updated the grade in Record")
            case _:
                print("Invalid Input")
        print("-------Updated DETAILS-------")
        print("ID".center(10),id_edit)
        for ele in Students[id_edit]:
            print(f"{ele}".center(10),Students[id_edit][ele])
    else:
        print("No such ID is present in our Record!!!")

def search():
    print("\n___Search a Student Record___")
    id_search = int(input("Enter the student ID to search the record : "))
    if id_search in Students_id:
        print("-------Student DETAILS-------")
        print("ID".center(10),id_search)
        for ele in Students[id_search]:
            print(f"{ele}".center(10),Students[id_search][ele])
    else:
        print("There's no such Record in our app!!!")

def delete_record():
    print("\n___Delete a Record___")
    id_del = int(input("Enter the Student ID to delete his record : "))
    if id_del in Students_id:
        del Students[id_del]
        Students_id.remove(id_del)
        print("Successfully Deleted the Student Record :",id_del)
    else:
        print("There's no such ID present in our Record!!!")

def main():
    print("___Welcome to Student Management System App___")
    while 1 :
        print("\n1.Add a new Student Record")
        print("2.Update a Student Record")
        print("3.Search a Student Record")
        print("4.View all the Students Records")
        print("5.Delete a Student Record")
        print("6.Exit the app")
        ch = int(input("Enter your choice : "))
        match ch:
            case 1 : add_record()
            case 2 : edit()
            case 3 : search()
            case 4 : view()
            case 5 : delete_record()
            case 6 : 
                print("Thank you for visiting Our Student Management System App...")
                sys.exit()

main()