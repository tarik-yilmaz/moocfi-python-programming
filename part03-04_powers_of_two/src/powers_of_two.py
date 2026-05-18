# Write your solution here

upper_limit = int(input("Upper limit: "))
running_number = 0
num = 0

while num <= upper_limit:

    print(2 ** running_number)
    running_number += 1
    num = 2 ** running_number