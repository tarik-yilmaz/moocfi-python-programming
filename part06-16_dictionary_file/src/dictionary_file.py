# Write your solution here

# Get input


while True:

    print("1 - Add word, 2 - Search, 3 - Quit")
    task = int(input("Function: "))
    
    if task == 1:
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")
        with open("dictionary.txt", "a") as file:
            file.write(f"{finnish_word} - {english_word}\n")
            print("Dictionary entry added")
    
    elif task == 2:
         search_term = input("Search term: ")
         output_list = []
         with open("dictionary.txt") as file:
            for line in file:
                line = line.replace("\n", "")
                
                if search_term in line:
                    output_list.append(line)
         for words in output_list:
            print(words)
                   
    elif task == 3:
        print("Bye!")
        break
    else:
        continue