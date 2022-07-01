import random


pwin = 0
cwin = 0

key = ["rock","paper","scissors"]

print("You can enter either of the words i.e., stone, paper and scissors. If you want to view score or exit the game press 'q'")
while True:

    userpick = input("Enter your choice: ").lower()


    if userpick == "q":
        break
    compinp = random.randint(0,2)

    compick = key[compinp]   
    if(userpick == "rock" and compick == "scissors"):
        pwin += 1
        print("You won and computer chose",compick)
    elif(userpick == "paper" and compick == "rock"):
        pwin += 1
        print("You won and computer chose",compick)
    elif(userpick == "scissors" and compick == "paper"):
        pwin += 1
        print("You won and computer chose",compick)
    elif(compick == "rock" and userpick == "scissors"):
        cwin +=1
        print("Computer won and computer chose",compick)
    elif(compick == "paper" and userpick == "rock"):
        cwin +=1
        print("Computer won and computer chose",compick)

    elif(compick == "scissors" and userpick == "paper"):
        cwin +=1
        print("Computer won and computer chose",compick)
    elif(compick == userpick):
        print("This round is tie, computer chose",compick,"continue to next pick")
        pwin += 1
        cwin += 1
    else:
        print("Unknown key entered, redirecting to score")
        break

print("The user won",pwin,"times.")
print("The computer won",cwin,"times.")
    
