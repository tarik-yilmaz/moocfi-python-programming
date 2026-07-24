# Write your solution here

def smallest_average(person1:  dict, person2:  dict, person3:  dict) -> dict:
    persons = [person1, person2, person3]
    person_sums = []
    

    for person in person1.values(), person2.values(), person3.values():
        sum_of_result = 0

        for value in person:
            try:
                value =  int(value)
                sum_of_result += value
            except (TypeError, ValueError):
                pass
        person_sums.append(sum_of_result)


    index = person_sums.index(min(person_sums))

    return persons[index]

'''
An alternative from LLM:
def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    persons = [person1, person2, person3]

    smallest_person = persons[0]
    smallest_sum = (
        persons[0]["result1"]
        + persons[0]["result2"]
        + persons[0]["result3"]
    )

    for person in persons[1:]:
        result_sum = (
            person["result1"]
            + person["result2"]
            + person["result3"]
        )

        if result_sum < smallest_sum:
            smallest_sum = result_sum
            smallest_person = person

    return smallest_person
'''


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))