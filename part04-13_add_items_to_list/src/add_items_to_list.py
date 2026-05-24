# Write your solution here

my_list = []

items = int(input("How many items: "))
start = 1

while start <= items:

    item = int(input(f"Item {start}: "))
    my_list.append(item)
    start += 1

print(my_list)
