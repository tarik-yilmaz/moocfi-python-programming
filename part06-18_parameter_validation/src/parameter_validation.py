# Write your solution here

def new_person(name: str, age: int) -> tuple:
    if len(name) < 0:
        raise ValueError("Name cannot be empty")
    
    parts = name.split(" ")
    
    if len(parts) < 2:
        raise ValueError("Name must contain two words")
    
    if len(name) > 40:
        raise ValueError("Name cannot be longer than 40 characters")

    if age < 0:
        raise ValueError(f"Age was negative: " + str(age))

    if age > 150:
        raise ValueError("Age was greater than 150: " + str(age))

    return (name, age)