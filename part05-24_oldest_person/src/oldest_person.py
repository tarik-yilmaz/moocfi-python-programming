# Write your solution here

def oldest_person(people: list):
    oldest = people[0]

    for p in people:
        if p[1] < oldest[1]:
            oldest = p
    
    return oldest[0]
