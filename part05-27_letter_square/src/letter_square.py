# Write your solution here

def main():
    layer = int(input("Layers: "))

    if layer < 1:
        return
    
    grid_size = layer * 2 - 1

    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", 
                           "X", "Y", "Z"]
    
    for row in range(0, grid_size):
        for column in range(0, grid_size):
            top = row
            left = column
            bottom = grid_size - 1 - row
            right = grid_size - 1 - column

            distance = min(top, left, bottom, right)

            letter = layer - 1 - distance

            print(f"{alphabet[letter]}", end="")
            distance = 0
        print()        

main()