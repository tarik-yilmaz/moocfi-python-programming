# Write your solution here

def same_word_twice():
    different_words = 0
    word_list = []

    while True:
        word = input("Word: ")

        if word in word_list:
            print(f"You typed in {different_words} different words")
            break
        else:
            word_list.append(word)
            different_words += 1

same_word_twice()