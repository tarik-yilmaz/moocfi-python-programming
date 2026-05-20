# Write your solution here

word = input("Please type in a string: ")

length = len(word) - 1
next = -1
while next >= -len(word):
    print(word[next:])
    next -= 1
    