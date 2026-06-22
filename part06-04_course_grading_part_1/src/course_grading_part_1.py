# write your solution here

## Note: to get things running with the current folder structure
## change the path in the open function to (f"/src{...})"

# Read input from the user
student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")

# Create empty dictionaries for students and exercises
students = {}
exercises = {}

# Read the file for students
with open(f"{student_file}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")

        parts = line.split(";")

        if parts[0] == "id":
            continue
        
        # Add the id as a key and concatenate the name of the student as the value
        students[parts[0].strip()] = parts[1].strip() + " " + parts[2].strip()

# Read the file for the exercises
with open(f"{exercise_file}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")

        parts = line.split(";")

        if parts[0] == "id":
            continue
        
        # Add the id as a key and all other parts till newline as the value
        exercises[parts[0].strip()] = parts[1:]

sum_of_exercises = 0

# Loop through the dictionariy of exercises
for key, value in exercises.items():
        
        # For every item in the list of the id (key), convert to int and add to the variable
        for i in value:
            i = int(i)
            sum_of_exercises += i
        
        # Add the sum to the specific id in the exercises dictionary
        exercises[key] = sum_of_exercises
        
        # Reset the sum
        sum_of_exercises = 0
    
# Print the output
for id, name in students.items():
    if id in exercises:
        total = exercises[id]
        print(f"{name} {total}")
