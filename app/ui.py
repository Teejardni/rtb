from card import suits, ranks

def display_card(card):
    rank, suit = card['rank'], card['suit']
    return [
        "┌─────────┐",
        f"│ {rank:<2}      │",
        "│         │",
        f"│    {suit}    │",
        "│         │",
        f"│      {rank:>2} │",
        "└─────────┘"
    ]

def print_cards(cards):
    if not cards:
        return
    card_lines = [display_card(card) for card in cards]
    for i in range(7):
        print('  '.join(lines[i] for lines in card_lines))

def print_welcome():
    print("Welcome to Ride the Bus!")
    print("Rules: Bet $10–max cap. Guess correctly to multiply your bet: 2x (Red/Black), 3x (Higher/Lower), 4x (In/Out), 20x (Suit).")
    print("One wrong guess loses your bet. Max bet depends on balance: ≤$1,000: $100, ≤$5,000: $500, ≤$10,000: $750, >$10,000: $1,000.")

def get_bet(balance, max_bet):
    if max_bet < 10:
        print("Balance too low to play ($10 minimum). Game Over.")
        return None
    while True:
        try:
            bet = int(input(f"Enter your bet ($10–${max_bet}): "))
            if 10 <= bet <= max_bet:
                return bet
            print(f"Bet must be between $10 and ${max_bet}.")
        except ValueError:
            print("Please enter a valid number.")

def get_round_1_guess():
    guess = input("Is the card red or black? [r/b]: ").lower()
    while guess not in ['r', 'b']:
        guess = input("Invalid input. Enter [r/b]: ").lower()
    return guess

def get_round_2_guess():
    guess = input("Higher or lower? [h/l]: ").lower()
    while guess not in ['h', 'l']:
        guess = input("Invalid input. Enter [h/l]: ").lower()
    return guess

def get_round_3_guess():
    guess = input("In between or outside? [i/o]: ").lower()
    while guess not in ['i', 'o']:
        guess = input("Invalid input. Enter [i/o]: ").lower()
    return guess

def get_round_4_guess():
    guess = input("Guess the suit [h/d/c/s]: ").lower()
    while guess not in ['h', 'd', 'c', 's']:
        guess = input("Invalid input. Enter [h/d/c/s]: ").lower()
    return guess

def print_balance(balance):
    print(f"Balance: ${balance}")

def ask_replay():
    return input("Play another hand? [y/n]: ").lower() == 'y'