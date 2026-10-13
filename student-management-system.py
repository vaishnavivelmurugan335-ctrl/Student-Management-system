import json
import os

filename = "students.json"

# Load saved student records
if os.path.exists(filename):
    with open(filename, "r") as file:
        students = json.load(file)
else:
    students = []

# Save student records
def save_students():
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        roll = input("Enter Roll Number: ")
        dept = input("Enter Department: ")

        if any(s["Roll"] == roll for s in students):
            print("Roll Number Already Exists!")
        else:
            students.append({
                "Name": name,
                "Roll": roll,
                "Department": dept
            })
            save_students()
            print("Student Added Successfully!")

    elif choice == "2":
        if not students:
            print("No Students Available!")
        else:
            for student in students:
                print(student)

    elif choice == "3":
        roll = input("Enter Roll Number: ")

        for student in students:
            if student["Roll"] == roll:
                print("Student Found:", student)
                break
        else:
            print("Student Not Found!")

    elif choice == "4":
        roll = input("Enter Roll Number: ")

        for student in students:
            if student["Roll"] == roll:
                student["Department"] = input(
                    "Enter New Department: "
                )
                save_students()
                print("Student Updated!")
                break
        else:
            print("Student Not Found!")

    elif choice == "5":
        roll = input("Enter Roll Number: ")

        for student in students:
            if student["Roll"] == roll:
                students.remove(student)
                save_students()
                print("Student Deleted!")
                break
        else:
            print("Student Not Found!")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")