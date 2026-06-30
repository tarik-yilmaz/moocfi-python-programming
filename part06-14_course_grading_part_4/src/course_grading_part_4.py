# tee ratkaisu tänne

# write your solution here

student_file = input("Student information: ")
exercise_file =  input("Exercises completed: ")
exam_file =  input("Exam points: ")
course_file = input("Course information: ")
students = {}
exercises = {}
exam_points = {}


def grade(total_points):
    if total_points < 15:
        return 0
    elif total_points < 18:
        return 1
    elif total_points < 21:
        return 2
    elif total_points < 24:
        return 3
    elif total_points < 28:
        return 4
    else:
        return 5

# Read course information
with open(f"src/{course_file}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")

        parts = line.split(":")

        if parts[0] == "name":
            course_name = parts[1].strip()
        elif parts[0] == "study credits":
            course_credits = parts[1].strip()

# Read student information
with open(student_file) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")

        if parts[0] == "id":
            continue

        student_id = parts[0]
        name = parts[1] + " " + parts[2]

        students[student_id] = name


# Read completed exercises
with open(exercise_file) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")

        if parts[0] == "id":
            continue

        student_id = parts[0]
        total_exercises = 0

        for exercise in parts[1:]:
            total_exercises += int(exercise)

        exercises[student_id] = total_exercises


# Read exam points
with open(exam_file) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")

        if parts[0] == "id":
            continue

        student_id = parts[0]
        total_exam_points = 0

        for point in parts[1:]:
            total_exam_points += int(point)

        exam_points[student_id] = total_exam_points


# Write results to files
title = f"{course_name}, {course_credits} credits"

with open("results.txt", "w") as result_file, open("results.csv", "w") as csv_file:
    result_file.write(title + "\n")
    result_file.write("=" * len(title) + "\n")
    result_file.write(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}\n")

    for student_id, name in students.items():
        exercise_score = exercises[student_id] // 4
        exam_score = exam_points[student_id]

        total_points = exercise_score + exam_score
        final_grade = grade(total_points)

        result_file.write(f"{name:<30}{exercises[student_id]:<10}{exercise_score:<10}{exam_score:<10}{total_points:<10}{final_grade}\n")
        csv_file.write(f"{student_id};{name};{final_grade}\n")


print("Results written to files results.txt and results.csv")