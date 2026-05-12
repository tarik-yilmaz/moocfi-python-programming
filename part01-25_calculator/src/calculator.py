# Write your solution here

first_operand = int(input("Number 1: "))
second_operand = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
    sum = first_operand + second_operand
    print(f"{first_operand} + {second_operand} = {sum}")

if operation == "multiply":
    sum = first_operand * second_operand
    print(f"{first_operand} * {second_operand} = {sum}")

if operation == "subtract":
    sum = first_operand - second_operand
    print(f"{first_operand} - {second_operand} = {sum}")
