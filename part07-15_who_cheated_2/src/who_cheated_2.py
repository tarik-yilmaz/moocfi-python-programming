# Write your solution here
from datetime import datetime, timedelta

def final_points() -> dict:
    students = {}
    submissions = {}

    # First open the file and save all students with their start times in a dictionary
    with open("src/start_times.csv") as start_file:
        for line in start_file:
            line = line.replace("\n", "")
            parts = line.split(";")

            students_name = parts[0]
            start_time = datetime.strptime(parts[1], "%H:%M")

            students[students_name] = start_time
        
    # Then open the submissions file
    with open("src/submissions.csv") as submission_file:
        for line in submission_file:
            line = line.replace("\n", "")

            parts = line.split(";")

            # Assign varibles from the file
            name = parts[0]
            task = int(parts[1])
            grade = int(parts[2])
            submission_time = datetime.strptime(parts[3], "%H:%M")

            # Calculate the difference: submission_time minus start_time
            delta = submission_time - students[name]

            # If submission is valid process the data
            if delta <= timedelta(hours=3):
                
                # Create an inner dictionary for every student
                if name not in submissions:
                    submissions[name] = {}

                # Add task the inner dict if it's not there
                if task not in submissions[name]:
                    submissions[name][task] = grade  
                # If the task where added before, compare the grade if it's higher
                # than the current one and update it respectively
                elif grade > submissions[name][task]:
                    submissions[name][task] = grade
    
    final_results = {}

    for name, tasks in submissions.items():
        final_results[name] = sum(tasks.values())

    return final_results

if __name__ == "__main__":
    print(final_points())