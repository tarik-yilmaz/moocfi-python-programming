# Write your solution here


counter = 0
sum = 0
mean = 0
positive_numbers = 0
negative_numbers = 0
print("Please type in integer numbers. Type in 0 to finish.")

while True:
    number = int(input("Number: "))

    if number == 0:
        break

    counter += 1
    sum += number
    mean = sum / counter

    if number > 0:
        positive_numbers += 1
    else:
        negative_numbers += 1

print(f"Numbers typed in {counter}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive_numbers}")
print(f"Negative numbers {negative_numbers}")

