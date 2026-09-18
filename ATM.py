def check_balance(balance):
    print(f"Your current balance is: ₹{balance:.2f}")


def deposit(balance):
    amount = float(input("Enter deposit amount: ₹"))

    if amount > 0:
        balance += amount
        print(f"₹{amount:.2f} deposited successfully!")
    else:
        print("Invalid deposit amount.")

    return balance


def withdraw(balance):
    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully!")

    return balance


def main():
    correct_pin = "1234"
    balance = 5000.0

    print("===== Welcome to Simple ATM =====")

    # PIN Login
    pin = input("Enter your PIN: ")

    if pin != correct_pin:
        print("Incorrect PIN. Access Denied.")
        return

    print("Login Successful!")

    # ATM Menu
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit(balance)

        elif choice == "3":
            balance = withdraw(balance)

        elif choice == "4":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice. Please try again.")


main()