# Python Banking Program

# 1. Show balance
# 2. Deposit
# 3. Withdraw

# declare the function we need first

def show_balance(balance):
    print(f"Your balance is RM {balance:.02f}")

def deposit(balance):
    amount = float(input("Enter an amount to deposit: RM "))

    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("Enter an amount to withdraw: RM "))

    if amount < 0:
        print("Amount must be greater than 0.")
        return 0
    elif amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        print(f"You have drawn RM {amount:.02f} from you account.")
        return amount



def main():

    balance = 0
    is_running = True

    while is_running:
        print("****************")
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("****************")
        choice = input("Enter your choice (1-40): ")

        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit(balance)
            case "3":
                balance -= withdraw(balance)
            case "4":
                is_running = False
            case _ :
                print("\nThat is not a valid choice.\n")

    print("Thank you! Have a nice day.")

if __name__ == '__main__':
    main()