import random
direction=["left","middle","right"]
totalScore=0
userTeamScore=0
computerTeamScore=0
print("------WELCOME TO THE MONEY  SHUFFLING  GAME------")
print("The options you can choose are left,right or middle")

def UserGlassSelect():
    global totalScore
    global userTeamScore
    totalScore+=1
    playerSelectGlass=input("Please select  your glass:").lower()
    ComputerSelect=random.choice(direction)
    print("The Computer Put the money in  "+ ComputerSelect.upper()+" glass")
    if playerSelectGlass=="left" and ComputerSelect=="right":
        print ( "Oops!!! Its not the orginal glass")
    elif playerSelectGlass=="right" and ComputerSelect=="left":
        print ("Oops!!! Its not the orginal glass")
    elif playerSelectGlass=="middle" and ComputerSelect=="left":
        print ("Oops!!! Its not the orginal glass")
    elif playerSelectGlass=="middle" and ComputerSelect=="right":
        print ("Oops!!! Its not the orginal glass")
    elif playerSelectGlass=="left" and ComputerSelect=="middle":
        print ("Oops!!! Its not the orginal glass")
    elif playerSelectGlass=="right" and ComputerSelect=="middle":
        print ("Oops!!! Its not the orginal glass")
    else:
        print("You select the orginal glass")
        userTeamScore+=1
        
def ComputerGlassSelect():
    global totalScore
    global computerTeamScore
    totalScore+=1
    UserSelect=input("Which glass do you want to put your money:").lower()
    computerSelect=random.choice(direction)
    print ("The computer selects the  "+computerSelect+" glass")
    if computerSelect=="left" and UserSelect=="right":
        print ( "Oops!!! Its not the orginal glass")
    elif computerSelect=="right" and UserSelect=="left":
        print ("Oops!!! Its not the orginal glass")
    elif computerSelect=="middle" and UserSelect=="left":
        print ("Oops!!! Its not the orginal glass")
    elif computerSelect=="middle" and UserSelect=="right":
        print ("Oops!!! Its not the orginal glass")
    elif computerSelect=="right" and UserSelect=="middle":
        print ("Oops!!! Its not the orginal glass")
    elif computerSelect=="left" and UserSelect=="middle":
        print ("Oops!!! Its not the orginal glass")
    else:
        print("Computer selects the right glass")
        computerTeamScore+=1

def printScores():
    print("The score is now YOU:"+str(userTeamScore)+" "+"COMPUTER:"+str(computerTeamScore))

def finalScore():
    print("FINAL SCORE "+str(userTeamScore) +"-" +str(computerTeamScore)) 
    if userTeamScore>computerTeamScore:
        print ("Well done you won")
    elif userTeamScore==computerTeamScore:
        print("A draw")
    else:
        print("You Lose")
while totalScore<10:
    UserGlassSelect()
    ComputerGlassSelect()
    printScores()
finalScore()
