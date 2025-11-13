# Guillermo Montiel             11-13-2025
# Lab #9 - Rock Paper Scissors Game
# Implements the classic game using Test Driven Development.

import random

def generateComputerMove():
    return random.choice(["Rock", "Paper", "Scissors"])

def determineWinner(human, cpu):
    if human == cpu:
        return "Draw"
    wins = {
        ("Rock", "Scissors"),
        ("Scissors", "Paper"),
        ("Paper", "Rock")
    }
    return human if (human, cpu) in wins else cpu

def playRound(humanMove):
    cpuMove = generateComputerMove()
    winner = determineWinner(humanMove, cpuMove)
    if winner == "Draw":
        return "Draw!"
    elif winner == humanMove:
        return "Human Wins!"
    else:
        return "Computer Wins!"

def main():
    print("Rock Paper Scissors!")
    rounds = int(input("How many rounds? (Must be an odd number): "))
    while rounds % 2 == 0:
        rounds = int(input("ERROR: Must be odd. Try again: "))

    humanWins = 0
    cpuWins = 0
    needed = rounds // 2 + 1

    while humanWins < needed and cpuWins < needed:
        move = input("Choose Rock, Paper, or Scissors: ")
        while move not in ["Rock", "Paper", "Scissors"]:
            move = input("ERROR: Enter Rock, Paper, or Scissors: ")

        result = playRound(move)

        if result == "Human Wins!":
            humanWins += 1
        elif result == "Computer Wins!":
            cpuWins += 1

        print(result)
        print(f"Score: Human {humanWins} - CPU {cpuWins}")

    if humanWins > cpuWins:
        print("You win the match!")
    else:
        print("Computer wins the match!")

if __name__ == "__main__":
    main()
