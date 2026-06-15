# Write your solution here

def dict_of_numbers() -> dict:
    dictionary = {}

    units = [
        "zero", "one", "two", "three",
        "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens = [
        "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    for i in range(20):
        dictionary[i] = units[i]

    
    number = 20

    for ten in tens:
        dictionary[number] = ten

        for i in range(1, 10):
            dictionary[number + i] = ten + "-" + units[i]

        number += 10

    return dictionary
