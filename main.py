print("=" * 50)
print("         PREPTRACK APPLICATION")
print("=" * 50)
while True:
    student_name = input("Enter student name: ")

    if student_name != "":
        break
    else:
        print("Student name cannot be empty.")
registration_number = input("Enter registration number: ")
graduation_year = int(input("Enter graduation year: "))
while True:
    attendance = float(input("Enter attendance percentage: "))

    if attendance >= 0 and attendance <= 100:
        print("Attendance accepted.")
        break
    else:
        print("Invalid attendance. Enter a value between 0 and 100.")
while True:
    project_input = input("Has the student completed the required project? (yes/no): ")

    if project_input == "yes":
        project_completed = True
        break
    elif project_input == "no":
        project_completed = False
        break
    else:
        print("Invalid input. Enter only yes or no.")
while True:
    profile_input = input("Is the student profile verified? (yes/no): ")

    if profile_input == "yes":
        profile_verified = True
        break
    elif profile_input == "no":
        profile_verified = False
        break
    else:
        print("Invalid input. Enter only yes or no.")   
total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0                  