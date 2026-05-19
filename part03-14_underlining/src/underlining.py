# Write your solution here


while True: 
    
    user_input = input("Please type in a string: ")
    
    if len(user_input) == 0:
        break

    lines = len(user_input)

    print(user_input)
    print("-" * lines)