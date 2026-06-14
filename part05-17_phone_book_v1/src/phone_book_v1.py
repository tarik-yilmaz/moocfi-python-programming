# Write your solution here
def usage():
    command = int(input("command (1 search, 2 add, 3 quit): "))

    if  type(command) != int or command < 1 or command > 3:
        return
    
    return command

def search(book: dict):
    name = input("name: ").strip()
            
    if name in book:
        print(book[name])
    else:
        print("no number")


def add(book: dict):
    name = input("name: ").strip()
    number = input("number: ").strip()

    if type(name) == str and type(number) == str:
        book[name] = number
        print("ok!")
        

def main():
    book = {}

    while True:
        command = usage()

        if command == 1:
            search(book)
            
        elif command == 2:
            add(book)
            
        elif command == 3:
            print("quitting...")
            return


main()