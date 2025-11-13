# Guillermo Montiel              11-13-2025
# Lab #9 - Unit Tests for fourInSequence.py
# Tests critical game logic: winner, draw, adjacency, next-move win.

import pytest
from fourInSequence import (
    checkWinner, checkDraw, checkAdjacent, checkForNextMoveWin,
    createBoard, placePiece, getPlayerPiece
)

def setup_board(rows, cols):
    return createBoard(cols, rows)

def test_check_winner_horizontal():
    board = setup_board(6, 7)
    for i in range(4):
        placePiece(board, 5, i, "X")
    assert checkWinner(board, 1) is True

def test_check_winner_vertical():
    board = setup_board(6, 7)
    for r in range(4):
        placePiece(board, 5 - r, 0, "O")
    assert checkWinner(board, 2) is True

def test_check_winner_diagonal_down():
    board = setup_board(6, 7)
    placePiece(board, 5, 0, "X")
    placePiece(board, 4, 1, "X")
    placePiece(board, 3, 2, "X")
    placePiece(board, 2, 3, "X")
    assert checkWinner(board, 1) is True

def test_check_winner_diagonal_up():
    board = setup_board(6, 7)
    placePiece(board, 2, 0, "O")
    placePiece(board, 3, 1, "O")
    placePiece(board, 4, 2, "O")
    placePiece(board, 5, 3, "O")
    assert checkWinner(board, 2) is True

def test_check_draw():
    board = setup_board(6, 7)
    for r in range(6):
        for c in range(7):
            placePiece(board, r, c, "X")
    assert checkDraw(board) is True

def test_check_adjacent():
    board = setup_board(6, 7)
    placePiece(board, 5, 3, "X")
    result = checkAdjacent(board, 1)
    assert result in [2, 3, 4]

def test_check_for_next_move_win():
    board = setup_board(6, 7)
    placePiece(board, 5, 0, "X")
    placePiece(board, 5, 1, "X")
    placePiece(board, 5, 2, "X")
    assert checkForNextMoveWin(board, 1) == 3
