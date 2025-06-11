import json
import os

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def enroll_student(data):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    department = input("Enter department: ")
    student = {
        "name": name,
        "roll": roll,
        "department": department,
        "attendance": [],
        "grades": {}
    }
    data.append(student)
    save_data(data)
    print("✅ Student enrolled successfully.\n")

def mark_attendance(data):
    roll = input("Enter student roll number: ")
    date = input("Enter date (DD-MM-YYYY): ")
    for student in data:
        if student['roll'] == roll:
            student['attendance'].append(date)
            save_data(data)
            print(f"✅ Attendance marked for {student['name']} on {date}.\n")
            return
    print("❌ Student not found.\n")

def add_grades(data):
    roll = input("Enter student roll number: ")
    subject = input("Enter subject: ")
    marks = input("Enter marks: ")
    for student in data:
        if student['roll'] == roll:
            student['grades'][subject] = marks
            save_data(data)
            print(f"✅ Grade added for {student['name']} in {subject}.\n")
            return
    print("❌ Student not found.\n")

def view_student(data):
    roll = input("Enter roll number to view details: ")
    for student in data:
        if student['roll'] == roll:
            print(f"\n📄 Student Info:")
            print(f"Name: {student['name']}")
            print(f"Roll: {student['roll']}")
            print(f"Department: {student['department']}")
            print(f"Attendance: {student['attendance']}")
            print("Grades:")
            for subject, marks in student['grades'].items():
                print(f"  {subject}: {marks}")
            print()
            return
    print("❌ Student not found.\n")

def main():
    data = load_data()
    while True:
        print("=== Student Management System ===")
        print("1. Enroll Student")
        print("2. Mark Attendance")
        print("3. Add Grades")
        print("4. View Student Info")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            enroll_student(data)
        elif choice == '2':
            mark_attendance(data)
        elif choice == '3':
            add_grades(data)
        elif choice == '4':
            view_student(data)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
