# Write your solution here

sentence = ""
same_word = ""

while True:
    next_word = input("Please type in a word: ")
    
    if  next_word == "end" or next_word == same_word:
        print(sentence)
        break

    same_word = next_word

    sentence += next_word + " "
