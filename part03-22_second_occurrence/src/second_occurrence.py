# Write your solution here

input_string = input("Please type in a string: ")
part = input("Please type in a substring: ")

first_index = input_string.find(part)
    
if first_index == -1:
     print("The substring does not occur twice in the string.")
else: 
    rest = input_string[first_index + len(part):]
    second_index = rest.find(part)

    if second_index != -1:
        real_second_index = first_index + len(part) + second_index
        print(f"The second occurrence of the substring is at index {real_second_index}.")
    else:
        print("The substring does not occur twice in the string.")
   

