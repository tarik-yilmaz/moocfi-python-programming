# Write your solution here
while True:
    editor = input("Editor: ").lower()

    if editor == "visual studio code":
        print("an excellent choice!")
        break
    elif editor == "notepad" or editor == "word":
        print("awful")
    else:
        print("not good")
