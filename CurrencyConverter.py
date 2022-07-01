#needs to run this command on terminal to compile (pip install forex-python)

from forex_python.converter import CurrencyRates

solution = CurrencyRates()

def result(from_currency, to_currency, amount):
    answer = solution.convert(from_currency, to_currency, amount)
    return (f"The amount {amount} is converted from {from_currency} to {to_currency} and it is {answer}")


try:
    f = True
    while f:
        print("\n*********************************************************************************************************\n")
        amount = int(input("Enter the amount: "))
        x = input(f"Enter the type for the amount {amount}: ").upper()
        y = input(f"Enter the currency type to which you want to convert {amount}: ").upper()
        print("\n*********************************************************************************************************\n")

        print(result(x,y,amount))
except KeyboardInterrupt:
    print("\nInvalid Strokes!!!")
except ValueError:
    print("Should use desired type for the every input")
