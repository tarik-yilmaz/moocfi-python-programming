# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()

        persons = json.loads(data)

    for person in persons:
        print(f"{person["name"]} {person["age"]} years",  end="")
        
        counter = 0
        print(" (", end="")

        for hobby in person["hobbies"]:
            print(hobby, end="")
            
            counter += 1

            if counter < len(person["hobbies"]):
                print(", ", end="")
        print(")")

            
if __name__ == "__main__":
    print_persons("file1.json")