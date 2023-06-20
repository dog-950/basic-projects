#!/usr/bin/env python3


"""
Two player tic-tac-toe game
"""


import sys
from typing import List


START_BOARD = ["#"] + ["-"] * 9

VECTOR_INDICES = [
    [1, 2, 3],  # top row
    [4, 5, 6],  # middle row
    [7, 8, 9],  # botom row
    [1, 4, 7],  # left column
    [2, 5, 8],  # middle column
    [3, 6, 9],  # right column
    [1, 5, 9],  # left to right diagonal
    [3, 5, 7],  # right to left diagonal
]

MARKERS = ("X", "O")


def main() -> int:
    """
    Main CLI routine

    Returns:
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
    # TODO


def game() -> None:
    """
    Play a tic-tac-toe game
    """
    board = START_BOARD
    o_turn = True
    
    decide_who_starts()
    
    while not game_is_over(board):
        board = get_input(board=board, o_turn=o_turn)
        display_board(board=board)
        o_turn = not o_turn


def decide_who_starts() -> None:
    """
    Decide and print who should play first (and thus who is O)
    """
    # TODO


def game_is_over(board: List[str]) -> bool:
    """
    Check if either player has won

    Args:
        board: Game board

    Returns:
        True if the game is over, Flase otherwise
    """
    # Check if anyone has won
    for marker in MARKERS:
        for combination in VECTOR_INDICES:
            if all(board[position] == marker for position in combination):
                print(f"{marker} WINS")
                return True
    
    # Check if any vectors could still win
    for combination in VECTOR_INDICES:
        vector = [board[position] for position in combination]
        if not all(marker in vector for marker in MARKERS):
            return False
    
    # Otherwise no winning moves are possible
    return True
    
    
def get_input(board: List[str], o_turn: bool) -> List[str]:
    """
    Check where player wants to place their move, and that it is a valid move
    
    Args:
        board: Current game board
        o_turn: True if O's turn, False if X's turn
        
    Returns:
        Updated game board after new input from player
    """
    # TODO
    # don't forget to `.upper()` the user's input


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


if __name__ == "__main__":
    sys.exit(main())
