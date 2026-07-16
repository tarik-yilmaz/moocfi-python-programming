# Write your solution here

import urllib.request,  json, math

def retrieve_all() -> tuple:
    try:
        my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    except Exception:
        print("Error! Couldn't connect to URL.")
        raise

    course_list = []

    #  Store data from the url to a variable
    data = my_request.read()
    
    # Convert it to a json format
    converted_data = json.loads(data)

    # Iterate through the data in the and assign variables when the condition applies
    for data in converted_data:
            if data["enabled"] == True:
                course_name = data["fullName"]
                name = data["name"]
                year = data["year"]
                
                # Inner loop for accessing the elements of a json property
                for exercise in data["exercises"]:
                     sum_of_exercises += int(exercise)
                
                # Add tuple to the list
                course_list.append((course_name, name, year, sum_of_exercises))
            
            # Reset sum
            sum_of_exercises = 0
    
    # Return the course list
    return course_list

def retrieve_course(course_name: str) -> dict:
    
    # Retrieve data through the parameter and throw exception if there is a connection error
    try:
        my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    except Exception:
        print("Error! Couldn't connect to URL.")
        raise

    # Create an empty dictionary
    stats_dictionary = {}

    data = my_request.read()

    converted_data = json.loads(data)

    # Create variables for stats
    weeks = 0
    students = 0
    hours = 0
    exercises = 0

    # Iterate through the data as json.loads() return a dictionary
    for value  in converted_data.values():
        # Increment weekly counter for every key
        weeks += 1

        # Update for every key the number of students if it's greater
        if value["students"] > students:
            students = value["students"]

        hours += value["hour_total"]
        exercises += value["exercise_total"]

    
    hours_average = math.floor(hours / students)
    exercise_average = math.floor(exercises / students)

    stats_dictionary["weeks"] = weeks
    stats_dictionary["students"] = students
    stats_dictionary["hours"] = hours
    stats_dictionary["hours_average"] = hours_average
    stats_dictionary["exercises"] = exercises
    stats_dictionary["exercises_average"] = exercise_average

    # Alternatively, the return statement could return the dict directly
    # without the helper variable `stats_dictionary`
    return stats_dictionary


if __name__ == "__main__": 
    print(retrieve_all())
    print(retrieve_course("docker2019"))
    