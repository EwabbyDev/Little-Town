import time, sys, os
from termcolor import colored


# Erases previous line
def erase():
    ERASE_LINE = '\x1b[2K'
    CURSOR_UP_ONE = '\x1b[1A'

    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)


# Function for colored text
def write(text, color):
    print(colored(text, color))


# Prints options every turn for player
def printOptions(turn):
    # Clears screen
    os.system('clear')

    # Shows who's turn it is and displays their options (see function)
    print("It is", colored(players[turn].name, "green") + "'s turn.")
    print("Balance: $" + str(players[turn].balance))
    print("BM: " + str(players[turn].bm))
    print("Owned Squares: " + str(players[turn].owned))
    print("Hunger: " + str(players[turn].hunger))
    print("Stress: " + str(players[turn].stress), "\n")

    write("[1] Pay", "yellow")
    write("[2] Receive", "yellow")
    write("[3] Adjust BM", "yellow")
    write("[4] Adjust Owned Squares", "yellow")
    write("[5] Adjust Hunger", "yellow")
    write("[6] Adjust Stress", "yellow")
    write("[7] Next Turn", "yellow")
    testAnswer(turn)


def nextTurn(turn, playerAmount):
    # Resets the turn to zero if needed
    if turn >= playerAmount:
        turn = 0

# Tax :'(
    if turn != 0:
        # Decreases hunger and stress by .5
        players[turn].hunger += 0.5
        players[turn].stress += 0.5

        # Tax
        players[turn].balance -= players[turn].owned * players[0].tax

        # Income
        players[turn].balance += players[turn].owned * (players[0].population + players[0].tourism + players[0].education + players[0].industry)

    if turn == 0:
        printGovOptions(0)
    else:
        printOptions(turn)


def testAnswer(turn):
    # Response for each option
    optionAnswer = input("\n")
    futherAnswer = ""
    if optionAnswer == "1":
        print("\nHow much should be deducted from",
              colored(players[turn].name, "green") + "'s balance? ")
        futherAnswer = int(input())
        if isinstance(futherAnswer, int):
            players[turn].balance -= futherAnswer
            time.sleep(2)
            printOptions(turn)
        else:
            printOptions(turn)
    if optionAnswer == "2":
        print("\nHow much should be added to",
              colored(players[turn].name, "green") + "'s balance? ")
        futherAnswer = int(input())
        if isinstance(futherAnswer, int):
            players[turn].balance += futherAnswer
            time.sleep(2)
            printOptions(turn)
        else:
            printOptions()
    if optionAnswer == "3":
        print("\nHow much BM does", colored(players[turn].name, "green"),
              "own? ")
        futherAnswer = int(input())
        if isinstance(futherAnswer, int):
            players[turn].bm = futherAnswer
            time.sleep(2)
            printOptions(turn)
        else:
            printOptions(turn)
    if optionAnswer == "4":
        print("\nHow many squares does", colored(players[turn].name, "green"),
              "own? ") 
        futherAnswer = int(input())
        oldAmount = players[turn].owned
        if isinstance(futherAnswer, int):
            players[turn].owned = futherAnswer
            time.sleep(2)
            if oldAmount < futherAnswer:
            	players[turn].bm -= futherAnswer - oldAmount
            printOptions(turn)
        else:
            printOptions(turn)
    if optionAnswer == "5":
        print("How much hunger does", colored(players[turn].name, "green"),
              "have?")
        futherAnswer = float(input())
        if isinstance(futherAnswer, float or int):
            players[turn].hunger = futherAnswer
            time.sleep(2)
            printOptions(turn)
        else:
            printOptions(turn)

    if optionAnswer == "6":
        print("How much stress does", colored(players[turn].name, "green"),
              "have?")
        futherAnswer = float(input())
        if isinstance(futherAnswer, float or int):
            players[turn].stress = futherAnswer
            time.sleep(2)
            printOptions(turn)
        else:
            printOptions(turn)

    if optionAnswer == "7":
        turn += 1
        os.system('clear')
        nextTurn(turn, playerAmount)


# Response for each option
def testGovAnswers(turn):
    optionAnswer = int(input("\n"))
    print("")
    futherAnswer = ""
    if isinstance(optionAnswer, int):
        if optionAnswer == 1:
            print("How much should be deducted? ")
            futherAnswer = int(input())
            if isinstance(futherAnswer, int):
                players[0].balance -= futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == 2:
            print("How much should be received? ")
            futherAnswer = int(input())
            if isinstance(futherAnswer, int):
                players[0].balance += futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == 3:
            print("How much BM? ")
            futherAnswer = int(input())
            if isinstance(futherAnswer, int):
                players[0].bm = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == 4:
            print("How much should the new tax be? ")
            futherAnswer = int(input())
            if isinstance(futherAnswer, int):
                players[0].tax = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == 5:
            print("How many population points? ")
            futherAnswer = int(input())
            if isinstance(futherAnswer, int):
                players[0].population = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == 6:
            print("How many fire security points? ")
            futherAnswer = int(input())
            if isinstance(futherAnswer, int):
                players[0].fire = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == 7:
            print("How many police security points? ")
            futherAnswer = int(input())
            if isinstance(futherAnswer, int):
                players[0].police = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == 8:
            print("How many tourism points? ")
            futherAnswer = int(input())
            if isinstance(futherAnswer, int):
                players[0].tourism = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == 9:
            print("How many industry points? ")
            futherAnswer = int(input())
            if isinstance(futherAnswer, int):
                players[0].industry = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == 10:
            print("How many medical care points? ")
            futherAnswer = int(input())
            if isinstance(futherAnswer, int):
                players[0].medical = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == 11:
            print("How many Education points? ")
            futherAnswer = int(input())
            if isinstance(futherAnswer, int):
                players[0].education = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == 12:
            turn += 1
            nextTurn(turn, playerAmount)
    else:
        printGovOptions(turn)


def printGovOptions(turn):
    # Clears screen
    os.system('clear')
    # Shows stats
    print("It is", colored(players[0].name, "green") + "'s turn.")
    print("Balance: $" + str(players[0].balance))
    print("BM: " + str(players[0].bm))
    print("Current Tax/sqr:", players[0].tax)
    print("Current Income/sqr:", players[0].population + players[0].tourism + players[0].education + players[0].industry)
    print("Population: " + str(players[0].population))
    print("Tourism: " + str(players[0].tourism))
    print("Industry: " + str(players[0].industry))
    print("Fire Security: " + str(players[0].fire))
    print("Police Security: " + str(players[0].police))
    print("Medical Care: " + str(players[0].medical))
    print("Education: " + str(players[0].education))

    # Displays options
    write("\n[1] Pay", "yellow")
    write("[2] Receive", "yellow")
    write("[3] Adjust BM", "yellow")
    write("[4] Change Tax", "yellow")
    write("[5] Adjust Population", "yellow")
    write("[6] Adjust Fire Security", "yellow")
    write("[7] Adjust Police Security", "yellow")
    write("[8] Adjust Tourism", "yellow")
    write("[9] Adjust Industry", "yellow")
    write("[10] Adjust Medical Care", "yellow")
    write("[11] Adjust Education", "yellow")
    write("[12] Next Turn", "yellow")

    testGovAnswers(turn)


# Player class
class Player:
    def __init__(self, name, balance, bm, hunger, stress, medical, population,
                 fire, police, tourism, industry, owned, tax, education):
        self.name = name
        self.balance = balance
        self.bm = bm
        self.hunger = hunger
        self.stress = stress
        self.owned = owned

        # Exclusively for government player
        self.medical = medical
        self.population = population
        self.fire = fire
        self.police = police
        self.tourism = tourism
        self.industry = industry
        self.tax = tax
        self.education = education


# # City name
# print("Hello.")
# time.sleep(4)
# print("I know what happenned.")
# time.sleep(5)
# print("It all went wrong.")
# time.sleep(3)
# print("But we know more now.")
# time.sleep(7)
# write("It will work this time.", "red")
# time.sleep(10)
# os.system('clear')
# time.sleep(4)

townname = input()
os.system('clear')
time.sleep(4)

# Intro
write(f"WELCOME TO {townname.upper()}", "magenta")
time.sleep(2)

# How many players
playerAmount = 0
while playerAmount < 3 or playerAmount > 6:
    playerAmount = int(input("\nHow many players are playing? "))
    print("\n\n")
    erase()
    erase()

# Sets game up
balance = 1200
bm = 25
hunger = 12.5
stress = 12.5
owned = 0
tax = 0

# Government variables
medical = 0
population = 30
fire = 0
police = 0
tourism = 0
industry = 0
education = 0

# Government starts
turn = 0

# Takes usernames
players = []
for i in range(playerAmount):
    name = input(f"Name of Player {1 + i}: ")
    erase()
    players.append(
        Player(name, balance, bm, hunger, stress, medical, population, fire, police, tourism, industry, owned, tax, education))
    write(f"{players[i].name}", "green")

time.sleep(2)

# Removes usernames from screen
os.system('clear')

# Actual game starter
players[0].balance = 700
players[0].bm = 50

nextTurn(turn, playerAmount)
