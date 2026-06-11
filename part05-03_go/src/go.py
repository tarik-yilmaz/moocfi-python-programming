# Write your solution here

def who_won(game_board: list) -> int:
    player1_count = 0
    player2_count = 0

    for row in game_board:
        for column in row:
            if column == 1:
                player1_count += 1
            elif column ==  2:
                player2_count += 1

    if player2_count == player1_count:
        return 0
    elif player1_count > player2_count:
        return 1
    else:
        return 2