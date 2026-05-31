# Write your solution here

def shortest(mylist: list[str]) -> int:
    length = mylist[0]

    for i in mylist:
        if len(i)  <= len(length):
            length = i

    return length