# Write your solution here

limit = int(input("Limit: "))
total = 0
value = 1
value_to_string = ''

while total  + 1 <= limit:
    
    value_to_string += str(value)

    total += value
    value += 1
    
    if total + 1 <= limit:
        value_to_string += ' + '    

print(f"The consecutive sum: {value_to_string} = {total}")