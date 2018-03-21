#!/usr/bin/env python3

"""
Eight queens - print/return all valid boards.

Completion time: 30 minutes.

Examples:

Notes
- Got to reducing the problem by one row each time, and tries all combos.
- Data structure of result makes it difficult to think about.
- Did not account for diagonal!
- Trick: simplify greatly using data structure columns[r] = int, vs coords.
- Trick: diagonal check - if r2-r1 == c2-c1
- Trick: printing is often easier than returning results.
"""


def queens(n, board=None):
    board = board or list()
    if len(board) == n:
        print_board(n, board)
        return
    for col in range(n):
        if is_valid(board, col):
            new_board = board[:]  # copy
            new_board.append(col)
            queens(n, new_board)


def is_valid(board, new_col):
    new_row = len(board)
    if new_col in board:
        return False
    for row, col in enumerate(board):
        if new_row - row == abs(new_col - col):
            return False  # diagonal
    return True


def print_board(n, board):
    columns = board
    for i in range(n):
        for j in range(n):
            if i < len(columns) and columns[i] == j:
                print('Q', end='')
            else:
                print('.', end='')
        print()
    print('='*n)


if __name__ == '__main__':
    queens(4)
