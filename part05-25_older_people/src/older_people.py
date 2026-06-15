# Write your solution here

def older_people(people: list, year: int):
    new_list = []

    for p in people:
        if p[1] < year:
            new_list.append(p[0]) 

    return new_list
