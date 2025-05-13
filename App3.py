import random

# File paths
ACCOUNT_FILE = "account.txt"
CUSTOMER_FILE = "customer.txt"
TRANSACTION_FILE = "transaction.txt"
USER_FILE = "user.txt"
ADMIN_FILE = "admin.txt"

# Fixed Admin Password
ADMIN_PASSWORD = "AdminSecure123"

# Dictionary to store account details
accounts = {}

# Function to load accounts
def load_accounts():
    global accounts
    try:
        with open(ACCOUNT_FILE, "r") as file:
            for line in file:
                account_number, customer_id, balance = line.strip().split(",")
                accounts[account_number] = {"customer_id": customer_id, "balance": float(balance), "transactions": []}
    except FileNotFoundError:
        accounts = {}

# Function to save account data
def save_accounts():
    with open(ACCOUNT_FILE, "w") as file:
        for account_number, details in accounts.items():
            file.write(f"{account_number},{details['customer_id']},{details['balance']}\n")

# Function to generate a unique random account number
def generate_account_number():
    return str(random.randint(1000, 9999))  # 6-digit account number

# Function to create an account
def create_account():
    account_number = generate_account_number()
    while account_number in accounts:  # Ensure uniqueness
        account_number = generate_account_number()
    
    customer_id = input("Enter customer ID: ")
    balance = float(input("Enter initial balance: "))
    if balance < 0:
        print("Error: Initial balance must be non-negative!")
        return
    
    accounts[account_number] = {"customer_id": customer_id, "balance": balance, "transactions": []}
    
    # Save data to files
    save_accounts()
    with open(CUSTOMER_FILE, "a") as file:
        file.write(f"{customer_id},{account_number}\n")

    print(f"Account created successfully! Your account number is {account_number}")

# Function to deposit money
def deposit_money():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Error: Account does not exist!")
        return
    
    amount = float(input("Enter deposit amount: "))
    if amount <= 0:
        print("Error: Deposit amount must be positive!")
        return
    
    accounts[account_number]["balance"] += amount
    accounts[account_number]["transactions"].append(f"Deposit: {amount}")

    with open(TRANSACTION_FILE, "a") as file:
        file.write(f"{account_number},Deposit,{amount}\n")

    save_accounts()
    print("Deposit successful!")

# Function to withdraw money
def withdraw_money():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Error: Account does not exist!")
        return
    
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0 or amount > accounts[account_number]["balance"]:
        print("Error: Invalid withdrawal amount!")
        return
    
    accounts[account_number]["balance"] -= amount
    accounts[account_number]["transactions"].append(f"Withdrawal: {amount}")

    with open(TRANSACTION_FILE, "a") as file:
        file.write(f"{account_number},Withdrawal,{amount}\n")

    save_accounts()
    print("Withdrawal successful!")

# Function to check balance
def check_balance():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Error: Account does not exist!")
        return
    print(f"Current balance: {accounts[account_number]['balance']}")

# Function to view transaction history
def transaction_history():
    account_number = input("Enter account number: ")
    print("Transaction History:")
    try:
        with open(TRANSACTION_FILE, "r") as file:
            for line in file:
                acc_num, trans_type, amount = line.strip().split(",")
                if acc_num == account_number:
                    print(f"{trans_type}: {amount}")
    except FileNotFoundError:
        print("No transactions found.")

# Function to authenticate admin login
def admin_login():
    password = input("Enter admin password: ")
    if password == ADMIN_PASSWORD:
        print("Admin login successful!")
        return True
    else:
        print("Access denied! Incorrect password.")
        return False

# Main menu with login protection
def main_menu():
    load_accounts()
    
    print("\nWelcome to the Banking System")
    user_type = input("Are you an Admin or User? (A/U): ").strip().upper()
    
    if user_type == "A":
        if not admin_login():
            return

    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            transaction_history()
        elif choice == "6":
            save_accounts()
            print("Exiting system. Have a great day!")
            break
        else:
            print("Invalid choice! Please select again.")

# Run the program
if __name__ == "__main__":
    main_menu()
