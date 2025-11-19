# Simple Banking System using if/else statements with input validation

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = float(balance)

    def display_balance(self):
        print(f"{self.owner}, your current balance is: NGN {self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"NGN {amount:.2f} deposited successfully.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"NGN {amount:.2f} withdrawn successfully.")

def read_amount(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            amount = float(raw)
            return amount
        except ValueError:
            print("Please enter a valid number (e.g., 2500 or 2500.50).")

def main():
    print("Welcome to the Banking System")
    name = input("Enter your name: ").strip() or "Customer"
    # Optional: start with a custom opening balance
    opening = read_amount("Enter opening balance (default 5000): ")
    if opening <= 0:
        opening = 5000.0
        print("Using default opening balance: NGN 5000.00")

    account = BankAccount(name, opening)

    while True:
        print("\nChoose an option:")
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            account.display_balance()
        elif choice == "2":
            amount = read_amount("Enter amount to deposit: ")
            account.deposit(amount)
        elif choice == "3":
            amount = read_amount("Enter amount to withdraw: ")
            account.withdraw(amount)
        elif choice == "4":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
