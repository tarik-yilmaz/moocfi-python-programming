# Write your solution here

positive_number = int(input("Please type in a positive integer: "))

for n in range(-positive_number, positive_number + 1):
    if n == 0:
        continue
    
    print(n)