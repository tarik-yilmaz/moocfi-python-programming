# write your solution here

student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam points: ")

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


# Print final grades
for student_id, name in students.items():
    exercise_score = exercises[student_id] // 4
    exam_score = exam_points[student_id]

    total_points = exercise_score + exam_score
    final_grade = grade(total_points)

    print(f"{name} {final_grade}")