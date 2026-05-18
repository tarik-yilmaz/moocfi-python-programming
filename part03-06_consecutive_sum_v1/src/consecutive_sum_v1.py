# Write your solution here

limit = int(input("Limit: "))
total = 0
value = 1

while total  + 1 <= limit:
    
    total += value
    value += 1

print(total)