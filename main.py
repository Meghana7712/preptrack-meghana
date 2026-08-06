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

for day in range(1, 8):
    while True:
        score = int(input(f"Enter Day {day} score (-1 for absent): "))
        if score == -1 or (0 <= score <= 100):
            break
        else:
            print("Invalid score. Enter -1 or a value between 0 and 100.")

    if score == -1:
        absent_days += 1
        print(f"Day {day} Result : Absent")
    else:
        attempted_days += 1
        total_score += score

        if score >= 75:
            print(f"Day {day} Result : Strong")
            strong_days += 1
        elif score >= 60:
            print(f"Day {day} Result : Satisfactory")
            satisfactory_days += 1
        elif score >= 40:
            print(f"Day {day} Result : Needs Improvement")
            improvement_days += 1
        else:
            print(f"Day {day} Result : Critical")
            critical_days += 1

        if score >= 60:
            passed_days += 1
        else:
            failed_days += 1

        if not first_attempt_found:
            highest_score = score
            lowest_score = score
            highest_score_day = day
            lowest_score_day = day
            first_attempt_found = True
        else:
            if score > highest_score:
                highest_score = score
                highest_score_day = day
            if score < lowest_score:
                lowest_score = score
                lowest_score_day = day

        if score < 40:
            if not critical_score_found:
                critical_score_found = True
                first_critical_day = day
                first_critical_score = score

if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0

graduation_eligible = 2025 <= graduation_year <= 2027
attendance_eligible = attendance >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4

placement_ready = (
    graduation_eligible and
    attendance_eligible and
    practice_count_eligible and
    average_eligible and
    critical_score_clear and
    passed_days_eligible and
    project_completed and
    profile_verified
)

if attempted_days == 0:
    status = "Practice Not Evaluated"
elif critical_score_found:
    status = "Critical Support Required"
elif attempted_days < 6:
    status = "Practice Incomplete"
elif passed_days < 4:
    status = "Insufficient Passed Practices"
elif average_score < 70:
    status = "Practice Improvement Required"
elif attendance < 75:
    status = "Attendance Improvement Required"
elif not graduation_eligible:
    status = "Graduation Criteria Not Met"
elif not project_completed:
    status = "Application On Hold"
elif not profile_verified:
    status = "Application On Hold"
else:
    status = "Ready for Mock Interview"

print("\n" + "=" * 50)
print("         STUDENT PERFORMANCE REPORT")
print("=" * 50)
print(f"Student Name        : {student_name}")
print(f"Registration Number : {registration_number}")
print(f"Graduation Year     : {graduation_year}")
print(f"Attendance          : {attendance:.1f}%")
print(f"Project Completed   : {'Yes' if project_completed else 'No'}")
print(f"Profile Verified    : {'Yes' if profile_verified else 'No'}")
print("-" * 50)
print(f"Attempted Days      : {attempted_days}")
print(f"Absent Days         : {absent_days}")
print(f"Passed Days         : {passed_days}")
print(f"Failed Days         : {failed_days}")
print(f"Average Score       : {average_score:.2f}")
if first_attempt_found:
    print(f"Highest Score       : {highest_score} (Day {highest_score_day})")
    print(f"Lowest Score        : {lowest_score} (Day {lowest_score_day})")
if critical_score_found:
    print(f"First Critical Score: {first_critical_score} (Day {first_critical_day})")
print("-" * 50)
print(f"Placement Ready     : {placement_ready}")
print(f"Status              : {status}")
print("=" * 50)