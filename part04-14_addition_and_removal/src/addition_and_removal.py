# Write your solution here

my_list = []
add_number = 1

while True:
    
    print(f"The list is now {my_list}")

    choice = input("a(d)d, (r)emove or e(x)it: ")

    if choice == "d":
        my_list.append(add_number)
        add_number += 1
    
    elif choice == "r":
        if len(my_list) > 0:
            my_list.pop()
            add_number -= 1
    
    elif choice == "x":
        print("Bye!")
        break
    else:
        continue
