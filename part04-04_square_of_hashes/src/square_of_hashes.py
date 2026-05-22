# Copy here code of line function from previous exercise

def line(times, text):
    if text == "":
        print(times * "*")
    elif len(text) > 0:
        print(times * text[0])

def square_of_hashes(size):
    # You should call function line here with proper parameters
    square = size

    while square > 0:
        line(size, "#")
        square  -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
