from operator import indexOf
import random

def sol(x):

    a = random.randint(0,10)
    if x < a:
        print("Low value, given input is {} and chosen number is {}".format(x,a))
        
    
    elif x > a:
        print("High value, given input is {} and chosen number is {}".format(x,a))
    
    else:
        print("Both the values are equal, the assigned value is {}".format(a))

print("If you want to check the answer give input of any integer and want exit press 'ctrl+C'\n")


print("###############################\n")

f = True
while f == True:
    try:
        val = int(input("Enter a value: "))
        sol(val)
    except KeyboardInterrupt:
        print("\nExited")
        f = False