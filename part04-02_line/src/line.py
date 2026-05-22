# Write your solution here

def line(times, text):
    if text == "":
        print(times * "*")
    elif len(text) > 0:
        print(times * text[0])

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")