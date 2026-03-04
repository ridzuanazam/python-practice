# Python Slot Machine

# continue vs break vs pass

# continue: Skip this turn, keep re-looping back.
# break: Stop the loop entirely.
# pass: Do nothing (a placeholder statement).

import random, time

def spin_row():
    symbols = [ '🍒', '🍉', '🍋', '🔔', '⭐']

    """
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results
    """
    # list comprehension
    return [random.choice(symbols) for symbol in range(3)]


def print_row(row):
    time.sleep(3)
    print("***********************")
    print(" | ".join(row))
    print("***********************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 6
        else:
            return bet * 7
    return 0
    

def main():
    balance = 100

    print("***********************")
    print("Welcome to Python Slot")
    print("Symbol : 🍒 🍉 🍋 🔔 ⭐")
    print("***********************")

    while balance > 0:
        print(f"Current balance: RM {balance}")

        bet = input("Place your bet amount: RM ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insuffcient fund.")
            continue

        if bet <= 0:
            print("That must be greater than 0.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won RM{payout}")
        else:
            print("Sorry you lost this round.")
        
        balance += payout

        play_again = input("Do you want to spin again? (Y/N) : ").upper()

        if play_again != 'Y':
            break
    print("**********************************************")
    print(f"Game over! Your final balance is RM {balance:.0f}")
    print("**********************************************")

if __name__ == '__main__':
    main()