class PINCodeError(Exception):
    pass


class MoneyNotEnoughError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


def send_money(balance, age, pin_code, amount, entered_pin_code):
    if entered_pin_code != pin_code:
        raise PINCodeError("Invalid PIN code")
    if age < 18:
        raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
    if amount > balance:
        raise MoneyNotEnoughError ("Insufficient funds for the requested transaction")

    balance -= amount
    print(f"Successfully sent {amount:.2f} money to a friend")
    print(f"There is {balance:.2f} money left in the bank account")

    return balance


def receive_money(balance, amount):
    if amount < 0:
        raise MoneyIsNegativeError("The amount of money cannot be a negative number")

    balance += amount / 2
    print(f"{amount / 2:.2f} money went straight into the bank account")

    return balance



# Read initial input
data = input().split(', ')
pin_code = data[0]
balance = float(data[1])
age = int(data[2])

# Process commands
while True:
    command = input()
    if command == "End":
        break

    action, amount_str, *pin_code_str = command.split('#')
    amount = float(amount_str)

    if action == "Send Money":
        entered_pin_code = pin_code_str[0] if pin_code_str else None
        balance = send_money(balance, age, pin_code, amount, entered_pin_code)

    elif action == "Receive Money":
        balance = receive_money(balance, amount)
