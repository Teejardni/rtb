from app.game import get_bet_cap, play_hand
from app.ui import get_bet, print_welcome, print_cards, print_balance, ask_replay



def main():
    balance = 500
    
    while balance >= 10:
        print_balance(balance)
        max_bet = min(get_bet_cap(balance), balance)
        print_welcome(max_bet)

        bet = get_bet(balance, max_bet)
        if bet is None:
            break
        balance, winnings = play_hand(balance, bet)
        print_balance(balance)
        if not ask_replay():
            break
    
    print(f"Game Over! Final Balance: ${balance}")

if __name__ == "__main__":
    main()
