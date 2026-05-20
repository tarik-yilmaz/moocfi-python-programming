# Write your solution here

sentence = input("Please type in a sentence: ")

while True:
    print(sentence[0])

    index_of_space = sentence.find(" ")

    if index_of_space == -1:
        break

    sentence = sentence[index_of_space + 1:]