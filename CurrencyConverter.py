#needs to run this command on terminal to compile (pip install forex-python)



from forex_python.converter import *

solution = CurrencyRates()

def result(from_currency, to_currency, amount):
    answer = solution.convert(from_currency, to_currency, amount)
    return ("The amount {} is converted from {} to {} and it is {}".format(amount, from_currency, to_currency, round(answer, 2)))


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
