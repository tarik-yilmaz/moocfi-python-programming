# Write your solution here

def list_twice():
    item_list = []

    while True:
        item = int(input("New item: "))

        if item == 0:
            print("Bye!")
            break

        item_list.append(item)
        print(f"The list now: {item_list}")
        print(f"The list in order: {sorted(item_list)}")


list_twice()