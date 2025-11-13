# Guillermo Montiel 10-07-2025
# COM S 1270
#
# This program is a Python version of the classic game NIM, called "NIMGRAB!".
# Players take turns removing items from a row. The player who takes the last item loses.
# The game can be played against another human or against the computer.

import random

MIN_TAKE = 1
MAX_TAKE = 3

def print_header():
    print("NIMGRAB!")
    print("By: Guillermo Montiel")
    print("[COM S 1270 1]")

def show_rules():
    print("\nRules of NIMGRAB!")
    print("1. The game starts with a row of items (typically 20-25).")
    print(f"2. Players take turns removing between {MIN_TAKE} and {MAX_TAKE} items.")
    print("3. You cannot take more items than remain in the row.")
    print("4. The player who takes the last item loses.")
    print("5. You can play against another human or the computer.\n")

def display_items(count):
    print("Items left:", count)
    print("| " * count)

def player_move(name, items_left):
    while True:
        try:
            take = int(input(f"{name}, how many items do you want to take [{MIN_TAKE}-{MAX_TAKE}]?: "))
            if take < MIN_TAKE or take > MAX_TAKE or take > items_left:
                print("ERROR: Invalid choice. Please choose again.")
            else:
                return take
        except ValueError:
            print("ERROR: Invalid input. Please enter an integer.")

def computer_move(items_left):
    if items_left <= MAX_TAKE:
        if items_left == 1:
            take = 1
        else:
            take = items_left - 1
    else:
        take = random.randint(MIN_TAKE, MAX_TAKE)
    print(f"Computer takes: {take}")
    return take

def play_game():
    total_items = random.randint(20, 25)
    items_left = total_items

    while True:
        mode = input("Do you want to play against [h]uman or [c]omputer?: ").lower()
        if mode in ['h', 'c']:
            break

    if mode == 'h':
        player1 = input("Enter Player 1 name: ")
        player2 = input("Enter Player 2 name: ")
        human_vs_computer = False
    else:
        player1 = input("Enter your name: ")
        player2 = "Computer"
        human_vs_computer = True

    current_player = player1

    while items_left > 0:
        display_items(items_left)
        if current_player != "Computer":
            take = player_move(current_player, items_left)
        else:
            take = computer_move(items_left)
        items_left -= take

        if items_left == 0:
            if current_player == "Computer":
                print(f"{current_player} took the last item. {player1} wins!")
            else:
                print(f"{current_player} took the last item. {player2} wins!")
            break

        current_player = player2 if current_player == player1 else player1

def main():
    print_header()
    while True:
        choice = input("Do you want to [p]lay, read the [r]ules, or [q]uit?: ").lower()
        if choice == 'p':
            play_game()
        elif choice == 'r':
            show_rules()
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            continue

if __name__ == "__main__":
    main()
