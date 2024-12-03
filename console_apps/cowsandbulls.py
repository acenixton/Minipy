# 17.11.2024, 18.11.2024, 19.11.2024
# cows and bulls is a bit like mastermind, player has to guess a code and will get "x cows, y bulls" back as hints
# cow means the digit is in the sequence but not in the correct spot
# bull means the digit is in the correct spot

import random
import time

# creates code with amount of digits provided by player (unique digits)
def moocode(length=4):
    code = set()
    while len(code) < length:
        code.add(random.randint(0,9))
    code = list(code)
    random.shuffle(code)
    return code

# counting correct digits
def testingcode(code):
    bovines = []
    bullpos = []
    for j in range(0,len(code)):
        # digit position correct?
        if code[j] == gamecode[j]:
            bovines.append("bull")
            bullpos.append(j)
    for i in code:
        # digit correct?
        if i in gamecode:   
            if code.index(i) not in bullpos:
                bovines.append("cow")
    return bovines

# set up new game
def startup():
    global gamecode
    global codelength
    codelength = input("How many digits should the code have?: ")        
    setlength = False
    # making sure user enters number
    while not setlength:
        try:
            codelength = int(codelength)
            if 0 < codelength <= 9:
                setlength = True
            else:
                raise 
        except:
            print("Please enter a number between 1 and 9!\n")
            codelength = input("\nHow many digits should the code have?: ")   
    gamecode = moocode(codelength) 

# gameplay loop
def gameplay():
    turn = 0
    wincon = False
    while not wincon:
        turn += 1
        usercode = [int(x) for x in input(f"Enter a {codelength} digit code to test: ")]
        # player has to enter correct amount of digits
        correct = False
        while not correct:
            if len(usercode) != codelength:
                usercode = [int(x) for x in input(f"Wrong length! Code should have {codelength} digits.\nTry again: ")]
            else:
                correct = True
        # wincon
        if usercode == gamecode:
            print(f"\nCongrats! You figured it out in {turn} tries.\nThe code was: {"".join([str(x) for x in gamecode])}\n")
            wincon = True
        # checking for hints
        else:
            bovines = testingcode(usercode) 
            print(f"\n cows: {bovines.count("cow")}\n bulls: {bovines.count("bull")}\n")

# main function
print(f"\n{"Cows and Bulls":>20}\n{"The fun code-breaking game":<20}\n")    
startup()
gameplay()

# make repeatable
while True:
    keeplaying = input("Wanna play again? (y/n): ")
    if keeplaying == "y":
        wincon = False
        startup()
        gameplay()
    else:
        print("\nOkay, bye (° - °)ﾉ\n")
        time.sleep(5)
        break
    
    
    



