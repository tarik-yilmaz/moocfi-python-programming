# Write your solution here

def grade_statistics():
    points_sum = 0
    student_count = 0
    passed_count = 0

    grade_0 = 0
    grade_1 = 0
    grade_2 = 0
    grade_3 = 0
    grade_4 = 0
    grade_5 = 0

    while True:
        user_input = input("Exam points and exercises completed: ")
        
        if user_input == "":
            break
        
        parts = user_input.split(" ")

        exam_points = int(parts[0])
        exercises = int(parts[1])

        exercise_points = exercises // 10
        total_points = exam_points + exercise_points

        points_sum += total_points
        student_count += 1

        if exam_points < 10:
            grade = 0
        elif total_points <= 14:
            grade = 0
        elif total_points <= 17:
            grade = 1
        elif total_points <= 20:
            grade = 2
        elif total_points <= 23:
            grade = 3
        elif total_points <= 27:
            grade = 4
        else:
            grade =  5

        if grade > 0:
            passed_count += 1

        if grade == 0:
            grade_0 += 1
        elif grade == 1:
            grade_1 += 1
        elif grade == 2:
            grade_2 += 1
        elif grade == 3:
            grade_3 += 1
        elif grade == 4:
            grade_4 += 1
        elif grade == 5:
            grade_5 += 1

    points_average = points_sum / student_count
    pass_percentage = passed_count / student_count * 100

    print("Statistics:")
    print(f"Points average: {points_average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    print(f"  5: {'*' * grade_5}")
    print(f"  4: {'*' * grade_4}")
    print(f"  3: {'*' * grade_3}")
    print(f"  2: {'*' * grade_2}")
    print(f"  1: {'*' * grade_1}")
    print(f"  0: {'*' * grade_0}")






grade_statistics()
