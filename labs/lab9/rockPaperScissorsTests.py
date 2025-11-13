# Guillermo Montiel             11-13-2025
# Lab #9 - Tests for Rock Paper Scissors (TDD)

import pytest
from rockPaperScissors import generateComputerMove, determineWinner, playRound

def test_generate_computer_move():
    for _ in range(50):
        assert generateComputerMove() in ["Rock", "Paper", "Scissors"]

def test_determine_winner():
    assert determineWinner("Rock", "Scissors") == "Rock"
    assert determineWinner("Scissors", "Paper") == "Scissors"
    assert determineWinner("Paper", "Rock") == "Paper"
    assert determineWinner("Rock", "Paper") == "Paper"
    assert determineWinner("Paper", "Scissors") == "Scissors"
    assert determineWinner("Scissors", "Rock") == "Rock"
    assert determineWinner("Rock", "Rock") == "Draw"

def test_play_round():
    result = playRound("Rock")
    assert "Wins" in result or result == "Draw!"
