# Write your solution here

def add_student(database: dict, name: str):
    database[name] = []

def add_course(database: dict, name: str, course: tuple):
    if name not in database:
        return
    
    course_name = course[0]
    grade = course[1]

    if grade == 0:
        return
    
    courses = database[name]

    for i in range(len(courses)):
        existing_course_name = courses[i][0]
        existing_grade = courses[i][1]

        if existing_course_name == course_name:
            if grade > existing_grade:
                courses[i] = course
            return
        
    courses.append(course)

def print_student(database: dict, name: str):
    if name not in database:
        print(f"{name}: no such person in the database")
        return
    
    print(f"{name}:")

    courses  = database[name]

    if len(courses) == 0:
        print(" no completed courses")
        return
    
    print(f" {len(courses)} completed courses:")

    grade_sum = 0

    for course in courses:
        course_name = course[0]
        grade = course[1]

        print(f"  {course_name} {grade}")
        grade_sum += grade

    average = grade_sum / len(courses)
    print(f" average grade {average}")


def summary(database: dict):
    student_count = len(database)

    most_courses = 0
    most_courses_students = ""

    best_average = 0
    best_average_student = ""

    for student in database:
        courses = database[student]

        course_count = len(courses)

        if course_count > most_courses:
            most_courses = course_count
            most_courses_students = student

        if course_count > 0:
            grade_sum = 0

            for course in courses:
                grade = course[1]
                grade_sum += grade

            average = grade_sum / course_count

            if average > best_average:
                best_average = average
                best_average_student = student
    
    print(f"students {student_count}")
    print(f"most courses completed {most_courses} {most_courses_students}")
    print(f"best average grade {best_average} {best_average_student}")