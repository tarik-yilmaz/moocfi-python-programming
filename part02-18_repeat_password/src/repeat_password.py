# Write your solution here

password = input("Password: ")

while True:
    verification = input("Repeat password: ")
    
    if password == verification:
        print("User account created!")
        break
    
    print("They do not match!")