# Guillermo Montiel 11-27-2025
# Assignment #6 - Candy Realm!
# This program is a simple Candy Land-style game for up to four players.
# Humans and computers move along a colored path by drawing cards from a deck.

import random

COLORS = ["M", "R", "B", "C", "G", "Y"]

BOARD_COLORS = [
    "M", "R", "B", "M", "C", "G", "B", "Y", "C",
    "B", "G", "Y", "G", "C", "Y", "R", "M", "R"
]

def safe_int_input(prompt, min_val, max_val):
    while True:
        user = input(prompt)
        try:
            value = int(user)
            if value < min_val or value > max_val:
                print(f"ERROR: Please enter an integer between {min_val} and {max_val}.")
            else:
                return value
        except ValueError:
            print("ERROR: Please enter an integer value.")

def print_header():
    print("Candy Realm!")
    print("By: Guillermo Montiel")
    print("[COM S 127 1]")

def print_menu_separator():
    print("-" * 65)

def show_instructions():
    print("#### HOW TO PLAY CANDY REALM! ####")
    print("- Up to 4 players race along a path of colored spaces.")
    print("- Each turn, a player draws a color card or shuffles the deck.")
    print("- When a card is drawn, the player moves forward to the next space of that color.")
    print("- If there is no matching color ahead, the player does not move.")
    print("- The first player to reach the last space on the path reaches the GOAL and wins.")
    print("- Humans choose whether to draw or shuffle; computers decide automatically.")
    print("- You can mix humans and computer players in any order (1-4 humans total).")
    print()

def create_deck(copies_per_color):
    deck = []
    for color in COLORS:
        for _ in range(copies_per_color):
            deck.append(color)
    random.shuffle(deck)
    return deck

def display_board_and_deck(players, deck):
    for i in range(1, 5):
        print(i)
    path = "START " + " ".join(BOARD_COLORS) + " GOAL!"
    print(path)
    if deck:
        print("CARDS " + " ".join(deck))
    else:
        print("CARDS (empty)")
    print()
    for p in players:
        pos = p["position"]
        if pos < 0:
            where = "START"
        elif pos >= len(BOARD_COLORS) - 1:
            where = "GOAL"
        else:
            where = f"space {pos + 1} ({BOARD_COLORS[pos]})"
        print(f"Player {p['id']} ({p['type']}): {where}")
    print()

def move_player_to_color(player, color):
    start_pos = player["position"]
    new_pos = start_pos
    for idx in range(start_pos + 1, len(BOARD_COLORS)):
        if BOARD_COLORS[idx] == color:
            new_pos = idx
            break
    steps = new_pos - start_pos
    if steps < 0:
        steps = 0
    player["position"] = new_pos
    return steps

def check_victory(player):
    return player["position"] >= len(BOARD_COLORS) - 1

def reshuffle_if_empty(deck, copies_per_color):
    if not deck:
        new_deck = create_deck(copies_per_color)
        deck.extend(new_deck)

def human_turn(player, deck, copies_per_color):
    reshuffle_if_empty(deck, copies_per_color)
    top_card = deck[0]
    while True:
        choice = input(
            f"Player {player['id']}: Would you like to [d]raw a {top_card} card, "
            f"[s]huffle the deck, or [q]uit?: "
        ).strip().lower()
        if choice in ("d", "s", "q"):
            break
        print("ERROR: Please enter 'd', 's', or 'q'.")
    if choice == "s":
        random.shuffle(deck)
        print(f"Player {player['id']} (HUMAN) has shuffled the deck!")
        input("Press [ENTER] To Continue...")
        return "continue"
    if choice == "q":
        print("Returning to MAIN MENU...")
        input("Press [ENTER] To Continue...")
        return "quit"
    card = deck.pop(0)
    reshuffle_if_empty(deck, copies_per_color)
    print(f"Player {player['id']} (HUMAN) has drawn: {card}")
    steps = move_player_to_color(player, card)
    if steps > 0:
        print(f"Player {player['id']} (HUMAN) moves forward {steps} spaces!")
    else:
        print(f"Player {player['id']} (HUMAN) does not move.")
    if check_victory(player):
        print(f"Player {player['id']} (HUMAN) has reached the GOAL!")
        input("Press [ENTER] To Continue...")
        return "win"
    input("Press [ENTER] To Continue...")
    return "continue"

def computer_turn(player, deck, copies_per_color):
    reshuffle_if_empty(deck, copies_per_color)
    action = "d"
    if random.random() < 0.25:
        action = "s"
    if action == "s":
        random.shuffle(deck)
        print(f"Player {player['id']} ({player['type']}) has shuffled the deck!")
        input("Press [ENTER] To Continue...")
        return "continue"
    card = deck.pop(0)
    reshuffle_if_empty(deck, copies_per_color)
    print(f"Player {player['id']} ({player['type']}) has drawn: {card}")
    steps = move_player_to_color(player, card)
    if steps > 0:
        print(f"Player {player['id']} ({player['type']}) moves forward {steps} spaces!")
    else:
        print(f"Player {player['id']} ({player['type']}) does not move.")
    if check_victory(player):
        print(f"Player {player['id']} ({player['type']}) has reached the GOAL!")
        input("Press [ENTER] To Continue...")
        return "win"
    input("Press [ENTER] To Continue...")
    return "continue"

def setup_players(num_humans):
    players = []
    for i in range(4):
        if i < num_humans:
            p_type = "HUMAN"
        else:
            p_type = "COMPUTER"
        players.append({"id": i + 1, "type": p_type, "position": -1})
    return players

def play_game():
    num_humans = safe_int_input("How Many Human Players [1] - [4]?: ", 1, 4)
    copies = safe_int_input("How Many Copies Of Each Card [1] - [5]?: ", 1, 5)
    players = setup_players(num_humans)
    deck = create_deck(copies)
    current_index = 0
    winner = None
    game_over = False
    while not game_over:
        print_menu_separator()
        display_board_and_deck(players, deck)
        player = players[current_index]
        if player["type"] == "HUMAN":
            result = human_turn(player, deck, copies)
        else:
            result = computer_turn(player, deck, copies)
        if result == "win":
            winner = player
            game_over = True
        elif result == "quit":
            return
        else:
            current_index = (current_index + 1) % len(players)
    print_menu_separator()
    print(f"Game Over! Player {winner['id']} ({winner['type']}) wins Candy Realm!")
    print()
    input("Press [ENTER] To Return To MAIN MENU...")

def main():
    running = True
    print_header()
    while running:
        print_menu_separator()
        choice = input("MAIN MENU: [p]lay game, [i]nstructions, or [q]uit?: ").strip().lower()
        if choice == "p":
            play_game()
        elif choice == "i":
            show_instructions()
        elif choice == "q":
            print("Goodbye!")
            running = False
        else:
            print("ERROR: Please enter 'p', 'i', or 'q'.")

if __name__ == "__main__":
    main()
