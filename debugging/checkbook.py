#!/usr/bin/python3

class Checkbook:
    """
    A simple Checkbook class that allows deposits, withdrawals,
    and checking the account balance.
    """
    def __init__(self):
        """Initialize a checkbook with a balance of 0.0."""
        self.balance = 0.0

    def deposit(self, amount):
        """Deposit a given amount into the checkbook."""
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Withdraw a given amount from the checkbook if funds are sufficient."""
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Display the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))


def get_valid_amount(prompt):
    """
    Prompt the user for a valid numeric amount.
    Repeats until a valid float is entered.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    """
    Main program loop:
    - Allows the user to deposit, withdraw, check balance, or exit.
    - Handles invalid inputs gracefully.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            print("Thank you for using the checkbook. Goodbye!")
            break
        elif action == 'deposit':
            amount = get_valid_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
