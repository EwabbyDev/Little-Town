import time, sys, os, random
from termcolor import colored

# Clears console before start
os.system('clear')

# Erases previous line
def erase():
    ERASE_LINE = '\x1b[2K'
    CURSOR_UP_ONE = '\x1b[1A'

    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)


# Function for colored text
def write(text, color):
    print(colored(text, color))

cards = [
	f"A fire is spreading across the city. If Fire Security isn't higher than 40, \npay 200 for damage caused",
	f"The crime rate is rising. If Police Security is lower than 100, \npay 500 to reduce it",
	f"Your town has been awarded the 'Tidy Towns Award'! \n+800",
	f"A virus is spreading across the country. If Medical Care isn't higher than 150, \npay 1000 to get help.",
	f"Good town. \n+500",
	f"Earthquake! \nPay 2000 to repair damage caused",
	f"Town reputation increases. \n+500 Population",
	f"Town reputation increases. \n+100 Population",
	f"Increase in investors. \n+15 Industry",
	f"Town advertising increases. \n+500 Tourism",
	f"Teachers improve. \n+15 Education",
	f"Nothing happenned this year",
	f"Nothing happenned this year",
	f"a fire is spreading across the city. If Fire Security is lower than 20, \npay 200 for damage caused",
	f"Citizen hapinness increases. \n+100 population",
	f"Increase in investors. \n+20 Industry",
	f"Lack of teachers. \n-50 Education",
	f"More job opportunities. \n+100 Population",
	"Town reputation decreases after dumb tweet. \n-10 Population",
	"Roads upgraded. \n+20 Tourism",
	"Change tax to 100 this year",
	"Town's economy increases. \n+30 Industry",
	"Nothing happenned this year",
	"Good town. \n+50",
	"Roads need maintaining. \nClose 20 road tiles",
	"A virus has entered the city. If Medical Care is lower than 500, \nPay 2000 to get help",
	"New pet ban. \n-500 Population",
	"New smoking ban. \n+50 Medical Care",
	"Increase in doctors. \n+10 Medical Care",
	"Wheelbarrow sold. \n+3",
	"Economic crisis. \nReset Industry",
	"More investors. \n+100 Economy",
	"Your town has been featured in \'A Town Under the Sun\'! \n+300 Tourism",
	"Town reputation increases. \n+50 Population",
	"Firefighters' salary increases. \nFire Security +20",
	"Bob the Builder upgrades buildings. \nTourism +10",
	"Not enough funding. \nSkip this year",
	"Not enough funding. \nSkip this year",
	"Not enough funding. \nSkip this year",
	"Nothing happenned this year.",
	"Harsher prison sentences. \n+50 Police Security",
	"Smoke detector distribution. \n+100 Fire Security",
	"More park funding. \n+50 Population",
	"More funding for greener energy. \n+20 Tourism",
	"Free education. \n+20 Education",
	"Bad town. \n-20 Population",
	"Merry Christmas! \n+50 Tourism",
	"If Education isn't higher than 100, \nReset Education",
	"Your town has been featured in the Weekly Town magazine. \n+20 Tourism",
	"Extra military units have been donated to your town. \nPolice Security +50",
	"Sewer leak. \n-300",
	"A tornado has caused huge destruction. \n-5000",
	"unemployment rate is increasing. If Education is lower than 200,\n pay 500",
	"Better city policies have been introduced. \n+50 Population",
	"Increase in homeless rate. \n-20 Population",
	"Rent is high. \n-100 Population",
	"The flu is being passes around. If Medical Care is lower than 100, \nPay 500",
	""
]

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

year = 2020
townname = ""
card = 0
players = []

def nextTurn(turn, playerAmount):
    # Resets the turn to zero if needed
    if turn >= playerAmount:
        turn = 0
        players[0].card = random.randint(0, len(cards))
        players[0].year += 1


# Tax :'(
    if turn != 0:
        # Decreases hunger and stress by .5
        players[turn].hunger += 0.25
        players[turn].stress += 0.25

        # Tax
        players[turn].balance -= players[turn].owned * players[0].tax
        players[0].balance += players[turn].owned * players[0].tax

        # Income
        players[turn].balance += players[turn].owned * ((players[0].population + players[0].tourism + players[0].education + players[0].industry) / 2)

    if turn == 0:
        printGovOptions(0)
        players[0].card = random.randint(0, len(cards))
    else:
        printOptions(turn)


def testAnswer(turn):
    # Response for each option
    optionAnswer = input("\n")
    futherAnswer = ""
    if optionAnswer == "1":
        print("\nHow much should be deducted from",
              colored(players[turn].name, "green") + "'s balance? ")
        futherAnswer = input()
        if futherAnswer.isnumeric():
            futherAnswer = int(futherAnswer)
            players[turn].balance -= futherAnswer
            time.sleep(2)
            printOptions(turn)
        else:
            printOptions(turn)
    elif optionAnswer == "2":
        print("\nHow much should be added to",
              colored(players[turn].name, "green") + "'s balance? ")
        futherAnswer = input()
        if futherAnswer.isnumeric():
            futherAnswer = int(futherAnswer)
            players[turn].balance += futherAnswer
            time.sleep(2)
            printOptions(turn)
        else:
            printOptions(turn)
    elif optionAnswer == "3":
        print("\nHow much BM does", colored(players[turn].name, "green"),
              "own? ")
        futherAnswer = input()
        if futherAnswer.isnumeric():
            futherAnswer = int(futherAnswer)
            players[turn].bm = futherAnswer
            time.sleep(2)
            printOptions(turn)
        else:
            printOptions(turn)
    elif optionAnswer == "4":
        print("\nHow many squares does", colored(players[turn].name, "green"),
              "own? ") 
        futherAnswer = input()
        oldAmount = players[turn].owned
        if futherAnswer.isnumeric():
            futherAnswer = int(futherAnswer)
            players[turn].owned = futherAnswer
            time.sleep(2)
            if oldAmount < futherAnswer:
            	players[turn].bm -= futherAnswer - oldAmount
            printOptions(turn)
        else:
            printOptions(turn)
    elif optionAnswer == "5":
        print("How much hunger does", colored(players[turn].name, "green"),
              "have?")
        futherAnswer = input()
        if futherAnswer.isnumeric():
            futherAnswer = float(futherAnswer)
            players[turn].hunger = futherAnswer
            time.sleep(2)
            printOptions(turn)
        else:
            printOptions(turn)
    elif optionAnswer == "6":
        print("How much stress does", colored(players[turn].name, "green"),
              "have?")
        futherAnswer = input()
        if futherAnswer.isnumeric():
            futherAnswer = float(futherAnswer)
            players[turn].stress = futherAnswer
            time.sleep(2)
            printOptions(turn)
        else:
            printOptions(turn)
    elif optionAnswer == "7":
        turn += 1
        os.system('clear')
        nextTurn(turn, playerAmount)
    else:
        printOptions(turn)


# Response for each option
def testGovAnswers(turn):
    optionAnswer = input("\n")
    print("")
    futherAnswer = ""
    if optionAnswer == "1" or optionAnswer == "2" or optionAnswer == "3" or optionAnswer == "4" or optionAnswer == "5" or optionAnswer == "6" or optionAnswer == "7" or optionAnswer == "8" or optionAnswer == "9" or optionAnswer == "10" or optionAnswer == "11" or optionAnswer == "12":
        if optionAnswer == "1":
            print("How much should be deducted? ")
            futherAnswer = input()
            if futherAnswer.isnumeric():
                futherAnswer = int(futherAnswer)
                players[0].balance -= futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == "2":
            print("How much should be received? ")
            futherAnswer = input()
            if futherAnswer.isnumeric():
                futherAnswer = int(futherAnswer)
                players[0].balance += futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == "3":
            print("How much BM? ")
            futherAnswer = input()
            if futherAnswer.isnumeric():
                futherAnswer = int(futherAnswer)
                players[0].bm = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == "4":
            print("How much should the new tax be? ")
            futherAnswer = input()
            if futherAnswer.isnumeric():
                futherAnswer = int(futherAnswer)
                players[0].tax = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == "5":
            print("How many population points? ")
            futherAnswer = input()
            if futherAnswer.isnumeric():
                futherAnswer = int(futherAnswer)
                players[0].population = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == "6":
            print("How many fire security points? ")
            futherAnswer = input()
            if futherAnswer.isnumeric():
                futherAnswer = int(futherAnswer)
                players[0].fire = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == "7":
            print("How many police security points? ")
            futherAnswer = input()
            if futherAnswer.isnumeric():
                futherAnswer = int(futherAnswer)
                players[0].police = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == "8":
            print("How many tourism points? ")
            futherAnswer = input()
            if futherAnswer.isnumeric():
                futherAnswer = int(futherAnswer)
                players[0].tourism = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == "9":
            print("How many industry points? ")
            futherAnswer = input()
            if futherAnswer.isnumeric():
                futherAnswer = int(futherAnswer)
                players[0].industry = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == "10":
            print("How many medical care points? ")
            futherAnswer = input()
            if futherAnswer.isnumeric():
                futherAnswer = int(futherAnswer)
                players[0].medical = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == "11":
            print("How many Education points? ")
            futherAnswer = input()
            if futherAnswer.isnumeric():
                futherAnswer = int(futherAnswer)
                players[0].education = futherAnswer
                time.sleep(2)
                printGovOptions(turn)
            else:
                printGovOptions(turn)
        if optionAnswer == "12":
            turn += 1
            nextTurn(turn, playerAmount)
    else:
        printGovOptions(turn)


def printGovOptions(turn):
    # Clears screen
    os.system('clear')
    # Shows stats
    print("It is", colored(players[0].name, "green") + "'s turn.")
    print("\nYear:", players[0].year, "\n")

    print(colored(cards[players[0].card], "white"))

    print("\nBalance: $" + str(players[0].balance))
    print("BM: " + str(players[0].bm))
    print("Current Tax/sqr:", players[0].tax)
    print("Current Income/sqr:", (players[0].population + players[0].tourism + players[0].education + players[0].industry) / 2)
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
    def __init__(self, name, balance, bm, hunger, stress, medical, population, fire, police, tourism, industry, owned, tax, education, year, card):
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
        self.year = year
        self.card = card


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

# Sets game up
balance = 1200
bm = 25
hunger = 8
stress = 8
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
card = 0

# Government starts
turn = 0

# Main menu
for i in range (5):
    time.sleep(0.5)
    erase()
    print(" - WELCOME TO LITTLE TOWN - ")
    time.sleep(0.5)
    erase()
    print(colored(" - WELCOME TO LITTLE TOWN - ", "cyan"))

townname = input("\nTown Name: ")
time.sleep(2)

# How many players
playerAmount = 0
while playerAmount < 3 or playerAmount > 6:
    playerAmount = input("\nHow many players are playing? ")
    erase()
    while not(playerAmount.isnumeric()):
        playerAmount = input("How many players are playing? ")
        erase()
    playerAmount = int(playerAmount)
    erase()

print("\n")
erase()
for i in range(playerAmount):
    name = input(f"Name of Player {1 + i}: ")
    erase()
    players.append(
        Player(name, balance, bm, hunger, stress, medical, population, fire, police, tourism, industry, owned, tax, education, year, card))
    write(f"{players[i].name}", "green")

time.sleep(1)

players[0].year = int(input("\nYear: "))

input("\n\nSystem is ready! [ENTER] ")

# Removes usernames from screen
os.system("clear")

# Actual game starter
players[0].balance = 700
players[0].bm = 50

# The command that ACTUALLY starts it
nextTurn(turn, playerAmount)
