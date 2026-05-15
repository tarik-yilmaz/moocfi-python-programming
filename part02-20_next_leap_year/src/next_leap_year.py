# Write your solution here

user_input = int(input("Year: "))
find_next_leap = user_input + 1

while True:
    

    if find_next_leap % 4 == 0:
        
        if find_next_leap % 100  == 0:    

            if find_next_leap % 400 == 0:
                print(f"The next leap year after {user_input} is {find_next_leap}")
                break
            
            else:
                find_next_leap += 1
        
        else:
            print(f"The next leap year after {user_input} is {find_next_leap}")
            break
    
    else:
        find_next_leap += 1
    
        