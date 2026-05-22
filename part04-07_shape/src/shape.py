# Copy here code of line function from previous exercise and use it in your solution

def line(times, text):
    if text == "":
        print(times * "*")
    elif len(text) > 0:
        print(times * text[0])


def shape(width, tri_character, rectangle, rec_character):
    
    triangle_height = 1

    while triangle_height <= width:
        line(triangle_height, tri_character)    
        triangle_height += 1
    
    rectangle_height = 1

    while rectangle_height <= rectangle:
        line(width, rec_character)
        rectangle_height += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")