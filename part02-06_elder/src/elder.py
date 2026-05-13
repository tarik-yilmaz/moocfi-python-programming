# Write your solution here

print("Person 1:")
p1_name = input("Name: ")
p1_age = int(input("Age: "))

print("Person 2:")
p2_name = input("Name: ")
p2_age = int(input("Age: "))

if p1_age > p2_age:
    print(f"The elder is {p1_name}")
elif p2_age > p1_age:
    print(f"The elder is {p2_name}")
else:
    print(f"{p1_name} and {p2_name} are the same age")
