students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = float(input("Enter marks: "))

        student = {
            "name": name,
            "roll": roll,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        for student in students:
            print("\nName:", student["name"])
            print("Roll Number:", student["roll"])
            print("Marks:", student["marks"])

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
