# Write your solution here

def first_word(sentence):
    first_word = ""
    index = 0

    while  index < len(sentence) and sentence[index] != " ": 
        first_word += sentence[index]
        index += 1 

    return first_word

def second_word(sentence):
    second_word = ""
    second_index = len(first_word(sentence)) + 1

    while second_index < len(sentence) and sentence[second_index] != " " :
        second_word += sentence[second_index]
        second_index += 1

    return second_word

def last_word(sentence):
    last_word = ""
    last_index = len(sentence) - 1

    while last_index >= 0  and  sentence[last_index] != " ":
        last_index -= 1

    last_index += 1

    while last_index  <= len(sentence) - 1:
        last_word += sentence[last_index]
        last_index += 1

    return last_word


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))