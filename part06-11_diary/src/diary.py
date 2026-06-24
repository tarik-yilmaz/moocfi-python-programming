# Write your solution here

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")

    choice = int(input("Function: "))


    if choice == 1:
        with open("diary.txt", "a") as new_file:
            entry = input("Diary entry: ")
            new_file.write(f"{entry}\n")
            print("Diary saved")

    elif choice == 2:
        print("Entries:")
        with open("diary.txt") as new_file:
            
            for line in new_file:
                line = line.replace("\n", "")
                print(line)

    elif choice == 0:
        print("Bye now!")
        break
    
