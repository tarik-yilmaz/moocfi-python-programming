# Write your solution here

def spruce(height):

    spaces = height - 1

    start = 1
    stars = 1

    print("a spruce!")

    while start <= height:
        print(spaces * " " + stars * "*")
        spaces -= 1
        start += 1
        stars += 2

    print((height - 1) * " " + "*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)