# COUNT TOTAL CUSTOMERS 

customers ={
    "name":"Roy","email":"roy2gmail.com",
    "name":"john","email":"john@gmail.com",
    "name":"peter","email":"peter@gmail.com"

}
      

def count_customers(customers):
    return len(customers)

def display_menu():
    print("\nMenu")
    print("1.Count total customers")
    print("2.Exit")

def main():
    while True:
        display_menu()
        choice=(input("Enter the Choice: "))

        if choice == "1":
            total=count_customers(customers)
            print("Totall Customers:{total}")
        elif choice == "2":
            print("Exiting prgramme")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

        

# SIMPLE BALANCE WARNING 

accounts ={
    101 : {"customer_id : 1" ,"Balance : 4000"},
    102 : {"customer id : 2" ,"Balance : 5000"}
}

def withdraw_money(accounts,account_number,amount):
    if account_number >= accounts:
        print("Account not found")
        return

    if amount <= 0:
        print("Withdraw amount correct one!")
        return

    if accounts[account_number]['Balance']<amount:
        print("insufficents balance")
        return

    accounts[account_number]["Balance"]-=amount
    print(f"withdraw succesfully. New balance:Rs.{accounts[account_number]["Balance"]}")

    if accounts[account_number]['Balance']<5000:
        print("Warning: Balance below Rs.5000")

withdraw_money(accounts,account_number,amount)




Customers account list

bank_app_menu.py

def withdraw_money(accounts, account_number, amount):
    if account_number not in accounts:
        print("Account not found.")
        return

    current_balance = accounts[account_number]['balance']
    
    if current_balance < amount:
        print("Insufficient funds.")
        return

    accounts[account_number]['balance'] -= amount
    new_balance = accounts[account_number]['balance']
    
    print(f"Withdrawal successful. Rs. {amount} withdrawn.")
    print(f"New balance: Rs. {new_balance}")

    if new_balance < 5000:
        print("Warning: Balance below Rs. 5000!")


def display_customer_accounts(customer_id, customers, accounts):
    if customer_id not in customers:
        print("Customer ID not found.")
        return

    found = False
    print(f"\nAccounts for {customers[customer_id]['name']} (Customer ID: {customer_id}):")
    
    for acc_num, acc_data in accounts.items():
        if acc_data['customer_id'] == customer_id:
            print(f"Account {acc_num}: Rs {acc_data['balance']:.2f}")
            found = True
    
    if not found:
        print("This customer has no accounts.")


def display_all_customers(customers):
    print("\nList of Customers:")
    for cust_id, data in customers.items():
        print(f"{cust_id}: {data['name']}")


def main():
    # Sample customer and account data
    customers = {
        "C001": {"name": "Alice"},
        "C002": {"name": "Bob"},
        "C003": {"name": "Charlie"}
    }

    accounts = {
        "1001": {"customer_id": "C001", "balance": 50000},
        "1002": {"customer_id": "C001", "balance": 12000},
        "1003": {"customer_id": "C002", "balance": 8000}
    }

    while True:
        print("\n--- Banking Application Menu ---")
        print("1. Withdraw Money")
        print("2. Display Customer Accounts")
        print("3. List All Customers")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            acc_no = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            withdraw_money(accounts, acc_no, amount)

        elif choice == "2":
            cust_id = input("Enter customer ID: ")
            display_customer_accounts(cust_id, customers, accounts)

        elif choice == "3":
            display_all_customers(customers)

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()






