# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    valid_range = [0, 1, 2]

    if x not in valid_range or y not in valid_range:
        return False
    
    if game_board[y][x] != "":
        return False
    else:
        game_board[y][x] = piece
        return True
