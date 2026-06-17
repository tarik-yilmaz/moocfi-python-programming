# write your solution here

def read_fruits() -> dict:
    dictionary = {}

    with open("src/fruits.csv") as new_file:
        
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            
            key = parts[0]
            value = float(parts[1])

            dictionary[key] = value

    return dictionary



if __name__ == "__main__":
    output = read_fruits()

    print(output)