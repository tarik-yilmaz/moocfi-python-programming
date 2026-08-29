# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return 0

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def vowel_count(self, word):
        count = 0

        for letter in word:
                if letter in "aeiou":
                    count += 1
        return count

    def round_winner(self, player1_word: str, player2_word: str):

        player1_vowel_count = self.vowel_count(player1_word)
        player2_vowel_count = self.vowel_count(player2_word)

        if player1_vowel_count > player2_vowel_count:
            return 1
        elif player2_vowel_count > player1_vowel_count:
            return 2
        else:
            return 0


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        valid_list = ["rock", "paper", "scissors"]

        if player1_word.lower() not in valid_list and player2_word.lower() not in valid_list:
            return 0
        elif player1_word.lower() == player2_word.lower():
            return 0
        elif player1_word.lower() in valid_list and player2_word. lower() not in valid_list:
            return 1
        elif player1_word.lower() == "rock" and player2_word.lower() == "scissors":
            return 1
        elif player1_word.lower() == "scissors" and player2_word.lower() == "paper":
            return 1
        elif player1_word.lower() == "paper" and player2_word.lower() == "rock":
            return 1
        else:
            return 2

if __name__ == "__main__":
    p = RockPaperScissors(4)
    p.play()