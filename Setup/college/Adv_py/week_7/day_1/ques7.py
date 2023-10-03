import logging
import re

# Configure the logging module
logging.basicConfig(
    filename="bank_transactions.log",
    level=logging.INFO,
    format="[%(asctime)s] Customer: %(customer)s, Transaction Type: %(transaction_type)s, Amount: %(transaction_amount)s"
)

# Function to validate user input
def is_valid_transaction_type(transaction_type):
    return transaction_type.lower() in ["deposit", "withdrawal"]

def is_valid_transaction_amount(transaction_amount):
    return re.match(r'^\d+(\.\d+)?$', transaction_amount) is not None

# Function to get valid user input
def get_valid_input(prompt, validation_func, error_message):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print(error_message)

# Main loop to log bank transactions
while True:
    print("\nBank Transaction Logger")
    customer_name = input("Enter customer's name (or 'quit' to exit): ")
    if customer_name.lower() == 'quit':
        break

    transaction_type = get_valid_input(
        "Enter transaction type (deposit/withdrawal): ",
        is_valid_transaction_type,
        "Invalid transaction type. Please enter 'deposit' or 'withdrawal'."
    )

    transaction_amount = get_valid_input(
        "Enter transaction amount: ",
        is_valid_transaction_amount,
        "Invalid transaction amount. Please enter a numeric value."
    )

    # Log the transaction
    logging.info("", extra={
        'customer': customer_name
        'transaction_type': transaction_type,
        'transaction_amount': transaction_amount
    })

    print("Transaction recorded successfully.")

print("Exiting the program.")
