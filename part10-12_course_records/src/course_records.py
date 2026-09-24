# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__grade

    def get_credits(self):
        return self.__credits

    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"

class CourseApplication:
    def __init__(self):
        self.__course_list = []

    def usage(self):
            print("1 add course")
            print("2 get course data")
            print("3 statistics")
            print("0 exit")
    
    def add_course(self):
        course_name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credit: "))

        new_course = Course(course_name, grade, credits)
        
        for course in self.__course_list:
            if course.get_name() == course_name:
                if grade > course.get_grade():
                    self.__course_list.remove(course)    
                    self.__course_list.append(new_course)
                return

        self.__course_list.append(new_course)

    def get_course_data(self):
        course_name = input("course: ")

        for course in self.__course_list:
            if course.get_name() == course_name:
                print(course)
            else:
                print("no entry for this course")

    def print_statistics(self):
        course_count = len(self.__course_list)

        credits_count = 0
        grades = []

        for course in self.__course_list:
            credits_count += course.get_credits()
            grades.append(course.get_grade())

        mean = sum(grades) / len(grades)

        print(f"{course_count} completed courses, a total of {credits_count} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")

        for grade in range(5, 0, -1):
            print(f"{grade}: {'x' * grades.count(grade)}")
            

    def execute(self):
        self.usage()

        while True:
            command = input("command: ")

            if command == "0":
                break

            if command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.print_statistics()

            
test = CourseApplication()
test.execute()