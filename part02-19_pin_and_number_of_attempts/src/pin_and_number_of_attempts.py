# Write your solution here

attempts = 0
pin = 4321

while True:
    user_input  = int(input("PIN: "))
    
    if  user_input == pin:
        if attempts == 0:
            print("Correct! It only took you one single attempt!")
            break
        else:
            attempts += 1
            print(f"Correct! It took you {attempts} attempts")
            break
    else:
        attempts += 1
        print("Wrong")
        