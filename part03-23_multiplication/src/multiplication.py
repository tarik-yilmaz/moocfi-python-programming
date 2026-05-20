# Write your solution here

end = int(input("Please type in a number: "))
first_factor = 1

while first_factor <= end:
    second_factor = 1

    while second_factor <= end:
        print(f"{first_factor} x {second_factor} = {first_factor * second_factor}")
        second_factor += 1
        
    first_factor += 1