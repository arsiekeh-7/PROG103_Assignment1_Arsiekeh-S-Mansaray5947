student_names = []
student_averages = []
student_grades = []
student_statuses = []


def get_grade(average):
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
    return grade


# -- Function 2: Add a new student --
def add_student():
    print("ADD STUDENT RECORD")


    name = input("Enter student name: ")

    print("Enter marks out of 100:")
    math = float(input("  Math: "))
    english = float(input("  English: "))
    science = float(input("  Science: "))
    ict = float(input("  ICT: "))

    # Calculate total and average
    total = math + english + science + ict
    average = total / 4

    # Get grade
    grade = get_grade(average)

    # Check pass or fail
    if average >= 50:
        status = "PASS"
    else:
        status = "FAIL"

    # Save to lists
    student_names.append(name)
    student_averages.append(average)
    student_grades.append(grade)
    student_statuses.append(status)

    print("")
    print("Student added successfully!")
    print("Name:    " + name)
    print("Average: " + str(round(average, 1)) + "%")
    print("Grade:   " + grade)
    print("Status:  " + status)


# -- Function 3: View all students --
def view_students():
    print("ALL STUDENT RECORDS")

    if len(student_names) == 0:
        print("No records found. Please add a student first.")
        return

    for i in range(len(student_names)):
        print(str(i + 1) + ". " + student_names[i] +
              "  |  Avg: " + str(round(student_averages[i], 1)) +
              "%  |  Grade: " + student_grades[i] +
              "  |  " + student_statuses[i])

    print("Total students: " + str(len(student_names)))


# -- Function 4: Show class summary --
def show_summary():
    print("CLASS SUMMARY")


    if len(student_names) == 0:
        print("No records found. Please add a student first.")
        return

    total = 0
    passed = 0
    top_name = student_names[0]
    top_avg = student_averages[0]

    for i in range(len(student_names)):
        total = total + student_averages[i]
        if student_statuses[i] == "PASS":
            passed = passed + 1
        if student_averages[i] > top_avg:
            top_avg = student_averages[i]
            top_name = student_names[i]

    class_avg = total / len(student_names)

    print("Total Students : " + str(len(student_names)))
    print("Class Average  : " + str(round(class_avg, 1)) + "%")
    print("Students Passed: " + str(passed))
    print("Top Student    : " + top_name + " (" + str(round(top_avg, 1)) + "%)")



# MAIN PROGRAM

print("Welcome to SRMTS")
print("Student Result Management Terminal System")
print("Limkokwing University - Sierra Leone")


choice = ""

while choice != "0":

    print("MAIN MENU")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Class Summary")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        show_summary()
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 0.")