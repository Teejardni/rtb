from card import rank_values, shuffle_deck, create_deck
from ui import print_cards, get_round_1_guess, get_round_2_guess, get_round_3_guess, get_round_4_guess

def get_bet_cap(balance):
    if balance <= 1000:
        return 100
    elif balance <= 5000:
        return 500
    elif balance <= 10000:
        return 750
    else:
        return 1000

def play_round_1(bet, card):
    print("\n--- Round 1: Red or Black? ---")
    print_cards([card])
    guess = get_round_1_guess()
    is_red = card['suit'] in ['♥', '♦']
    correct = (guess == 'r' and is_red) or (guess == 'b' and not is_red)
    if correct:
        print(f"Correct! Card is {card['rank']}{card['suit']}. Bet doubled to ${bet * 2}.")
        return bet * 2
    else:
        print(f"Wrong! Card is {card['rank']}{card['suit']}. You lose ${bet}.")
        return 0

def play_round_2(winnings, prev_card, card):
    print("\n--- Round 2: Higher or Lower? ---")
    print("Previous card:")
    print_cards([prev_card])
    print("New card:")
    print_cards([card])
    guess = get_round_2_guess()
    prev_value = rank_values[prev_card['rank']]
    curr_value = rank_values[card['rank']]
    correct = (guess == 'h' and curr_value > prev_value) or (guess == 'l' and curr_value < prev_value)
    if correct:
        print(f"Correct! Card is {card['rank']}{card['suit']}. Winnings tripled to ${winnings * 3}.")
        return winnings * 3
    else:
        print(f"Wrong! Card is {card['rank']}{card['suit']}. You lose your bet.")
        return 0

def play_round_3(winnings, card1, card2, card):
    print("\n--- Round 3: In Between or Outside? ---")
    print("Previous cards:")
    print_cards([card1, card2])
    print("New card:")
    print_cards([card])
    guess = get_round_3_guess()
    val1, val2 = rank_values[card1['rank']], rank_values[card2['rank']]
    curr_value = rank_values[card['rank']]
    min_val, max_val = min(val1, val2), max(val1, val2)
    correct = (guess == 'i' and min_val <= curr_value <= max_val) or (guess == 'o' and (curr_value < min_val or curr_value > max_val))
    if correct:
        print(f"Correct! Card is {card['rank']}{card['suit']}. Winnings quadrupled to ${winnings * 4}.")
        return winnings * 4
    else:
        print(f"Wrong! Card is {card['rank']}{card['suit']}. You lose your bet.")
        return 0

def play_round_4(winnings, card):
    print("\n--- Round 4: Guess the Suit ---")
    print_cards([card])
    guess = get_round_4_guess()
    suit_map = {'h': '♥', 'd': '♦', 'c': '♣', 's': '♠'}
    correct = suit_map[guess] == card['suit']
    if correct:
        print(f"Correct! Card is {card['rank']}{card['suit']}. Winnings multiplied by 20 to ${winnings * 20}!")
        return winnings * 20
    else:
        print(f"Wrong! Card is {card['rank']}{card['suit']}. You lose your bet.")
        return 0

def play_hand(balance, bet):
    deck = shuffle_deck(create_deck())
    drawn_cards = []
    
    # Deduct bet
    balance -= bet
    
    # Round 1
    card1 = deck.pop()
    drawn_cards.append(card1)
    winnings = play_round_1(bet, card1)
    if winnings == 0:
        return balance, winnings
    
    # Round 2
    card2 = deck.pop()
    drawn_cards.append(card2)
    winnings = play_round_2(winnings, card1, card2)
    if winnings == 0:
        return balance, winnings
    
    # Round 3
    card3 = deck.pop()
    drawn_cards.append(card3)
    winnings = play_round_3(winnings, card1, card2, card3)
    if winnings == 0:
        return balance, winnings
    
    # Round 4
    card4 = deck.pop()
    drawn_cards.append(card4)
    winnings = play_round_4(winnings, card4)
    balance += winnings
    return balance, winnings