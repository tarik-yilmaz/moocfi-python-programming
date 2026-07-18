# Write your solution here
from datetime import datetime, timedelta

def cheaters() -> list:
    students = {}
    cheaters_list = []

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

            # Save name and the to a datetime converted time to variables
            name = parts[0]
            submission_time = datetime.strptime(parts[3], "%H:%M")

            # If the name from the submissions file is in dictionary
            if name in students:
                    # Calculate the difference: submission_time minus start_time
                    delta = submission_time - students[name]
                    
                    # If the difference greater as specified, add the student to the cheater list
                    if delta > timedelta(hours=3):
                        if name not in cheaters_list:
                            cheaters_list.append(name)
    
    return cheaters_list

if __name__ == "__main__":
    print(cheaters())
            
                
