# Write your solution here

upper_limit = int(input("Upper limit: "))
base = int(input("Base: "))

power = 0
value = 1

while value <= upper_limit:
    print(value)
    power += 1
    value = base ** power
