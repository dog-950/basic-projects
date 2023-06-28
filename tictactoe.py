#!/usr/bin/env python3


"""
Two player tic-tac-toe game

This is now finished!

"""


import sys
from typing import List
import random


START_BOARD = ["#"] + ["-"] * 9

WIN_SETS = [
    [1, 2, 3],  # top row
    [4, 5, 6],  # middle row
    [7, 8, 9],  # botom row
    [1, 4, 7],  # left column
    [2, 5, 8],  # middle column
    [3, 6, 9],  # right column
    [1, 5, 9],  # left to right diagonal
    [3, 5, 7],  # right to left diagonal
]

MARKERS = ("O", "X")


def main() -> int:
    """
    Main CLI routine

    Returns:+
        Exit status
    """
    while ready_to_play():
        game()

    return 0


def ready_to_play() -> bool:
    """
    Wait for the player to signal they are ready to play
    
    Returns:
        True if player is ready to play [again], False otherwise
    """
    choice = ''
    while choice not in ('Y', 'N'):
        choice = input('ready to play? Y or N ').upper()
    if choice == 'Y':
        return True
    else:
        return False


def game() -> None:
    """
    Play a tic-tac-toe game
    """
    board = START_BOARD.copy()
    o_turn = True
    
    decide_who_is_O()

    display_board(board=board)
    
    while not game_is_over(board=board):
        print(f"{'O' if o_turn else 'X'}'s turn")
        board = get_input(board=board, o_turn=o_turn)
        display_board(board=board)
        o_turn = not o_turn
        


def decide_who_is_O() -> None:
    """
    Decide and print who is O (and thus who should play first)
    """
    if random.randint(0,1) == 0:
        print("Player 1 starts")
    else:
        print("Player 2 starts")


def game_is_over(board: List[str]) -> bool:
    """
    Check if either player has won

    Args:
        board: Game board

    Returns:
        True if the game is over, False otherwise
    """
    # Check if anyone has won
    for marker in MARKERS:
        for combination in WIN_SETS:
            if all(board[position] == marker for position in combination):
                print(f"{marker} WINS")
                return True
    
    # Check if any vectors could still win
    for combination in WIN_SETS:
        vector = [board[position] for position in combination]
        if not all(marker in vector for marker in MARKERS):
            return False
    
    # Otherwise no winning moves are possible
    return True
    

def space_is_free(board:List[str], position) -> bool:
    """
    Checks whether a space on the board is freely available

    Args: 
        board: current game board
        position: An integer from 1 - 9

    Returns:
        True if the position is free, False if not
    """
    return board[position] == "-"

    
def get_input(board: List[str], o_turn: bool) -> List[str]:
    """
    Check where player wants to place their move, and that it is a valid move
    
    Args:
        board: Current game board
        o_turn: True if O's turn, False if X's turn
        
    Returns:
        Updated game board after new input from player
    """
    position = 0
    while position not in range(1,10) or not space_is_free(board,position):
        position = int(input("Pick a position between 1 and 9 "))
    board = place_marker(board=board, o_turn=o_turn, position=position)
    return board


def display_board(board: List[str]) -> None:
    """
    Print the game board

    Args:
        board: Game board
    """
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])


def place_marker(board: List[str], o_turn: bool, position: int) -> List[str]:
    """
    Place a marker at a given position on the board
    
    
    Args:
        board: Current game board
        o_turn: True if O's turn, False if X's turn
    
    """
    board[position] = "O" if o_turn else "X"
    return board


if __name__ == "__main__":
    sys.exit(main())
