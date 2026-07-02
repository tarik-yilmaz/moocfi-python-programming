# Write your solution here
import random

def roll(die: str) -> int:
    a_die = [3, 3, 3, 3, 3, 6]
    b_die = [2, 2, 2, 5, 5, 5]
    c_die = [1, 4, 4, 4, 4, 4]

    if die == "A":
        return random.choice(a_die)
    if die == "B":
        return random.choice(b_die)
    if die == "C":
        return random.choice(c_die)


def play(die1: str, die2: str, times: int) -> tuple:
    wincount_die1 = 0
    wincount_die2 = 0
    ties = 0

    while times > 0:
        player1 = roll(die1)
        player2 = roll(die2)

        if player1 > player2:
            wincount_die1 += 1
        elif player2 > player1:
            wincount_die2 += 1
        else:
            ties += 1
        
        times -= 1
    
    return (wincount_die1, wincount_die2, ties)

if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")

    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)