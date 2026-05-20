# Write your solution here

def squared(text, times):
    index = 0
    row = 0

    while row < times:
        column = 0
        line = ""

        while column < times:
            line += text[index % len(text)]
            index += 1
            column += 1

        print(line)
        row += 1

if __name__ == "__main__":
    squared("aybabtu", 5)