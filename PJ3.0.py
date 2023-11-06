import random

coin = 0
choice = None
minimum = 1000
maximum = 2000
Win_Multiply = 1
lose_Multipay = 1
def hint():
    print ("+------------------------------------------------------------------------------------------+")
    print ("|                      Welcome to the head or tails guessing game.                         |")
    print ("|   How to play                                                                            |")
    print ("|  1.You can predict heads or tails when you start playing.                                |")
    print ("|  2.You have coins starting 1500$.                                                        |")
    print ("|  3.You can bet any amount. without exceeding the number of coins you have                |")
    print ("|  4.You can go back and select new predict by typing 'return'.                            |")
    print ("|  5.When you win or lose a bet A message and the number of remaining coins will appear.   |")
    print ("|  6.You can quit the game by typing 'quit'.                                               |")
    print ("|  7.You can get a hint by typing 'hint'.                                                  |")
    print ("|  8.You can select difficulty level by typing 'OP'.                                       |")
    print ("|                                                                                          |")
    print ("|                         Good luck, have fun with the game.                               |")
    print ("+------------------------------------------------------------------------------------------+\n")
def play():
        print ("\n\n-------------------------------")
        print ("-        heads or tails       -")
        print ("-------------------------------\n\n")
        print ('coins you have : ',coin,"$\n")
def LV():
    print ('\n\nPlease select a difficulty level.')
    print ('1. Easy')
    print ('2. Medium')
    print ('3. Hard')
    print ("4. Don't make mistakes.")
    print ("Type anything to play the original game.")
def TY():
    print ( "\n\n+----------------------------------+")
    print ( "|     Thank you for playing...     |")
    print ( "+----------------------------------+\n\n")
def HEAD():
    print("  //======\\\\")
    print(" ||  $  $  ||")
    print(" ||  $$$$  ||")
    print(" ||  $  $  ||")
    print("  \\\\======//")
def TAIL():
    print("  //======\\\\")
    print(" || $$$$$$ ||")
    print(" ||   $$   ||")
    print(" ||   $$   ||")
    print("  \\\\======//")
def LV_Detil():
    print ("+-------------------------------------------------------------------------------------------------------------+")
    print ("|                                               Level Detil                                                   |")
    print ("|                                                                                                             |")
    print ("|           Different level                |  Win_Multiply  |  lose_Multipay  | Coin maximum  | Coin minimum  |")
    print ("|  IN A Original             Game.         |        1       |        1        |      2000     |     1000      |")
    print ("|  IN A Easy                 Game.         |        2       |       0.5       |      2000     |     1000      |")
    print ("|  IN A Medium               Game.         |        1       |        1        |      3000     |     1000      |")
    print ("|  IN A Hard                 Game.         |        1       |        2        |      3000     |     1000      |")
    print ("|  IN A Don't make mistakes  Game.         |        1       |       10        |     10000     |     1000      |")
    print ("|                                                                                                             |")
    print ("|                                    Good luck, have fun with the game.                                       |")
    print ("+-------------------------------------------------------------------------------------------------------------+\n")
print ("\n\nWelcome to the head or tails guessing game.\n")

while coin == 0 :
    Play = input(f'Do you want to play the game? y/n : ')
    if Play == "y":
        coin = 1500
        play()

        while coin > minimum and coin < maximum :
            correct = random.choice(["heads", "tails"])
            if choice is None:
                choice = input(f'Guess heads or tails using "heads" or "tails". : ')
            if choice == "heads" or choice == "tails":
                try:
                    bet = input(f'Price to bet : ')
                    if str(bet) == "stop" :
                        print ( "ty for palying")
                        break
                    elif str(bet) == ("return") :
                        choice = None
                        continue
                    elif str(bet) == ("hint") :
                        hint()
                        continue
                    bet = int(bet)
                    print()
                    if bet <= coin :
                        if correct == "heads":
                            HEAD()
                        if correct == "tails":
                            TAIL()
                        if correct == choice :
                            print ("\n★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")
                            print ("★   ℂ 𝕆 ℝ ℝ 𝔼 ℂ 𝕋   ★")
                            print ("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★\n")
                            coin =  coin + (bet * Win_Multiply)
                            print ('coins you have : ',coin,"$\n")
                            choice = None
                        elif correct != choice :
                            print ("\n✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪")
                            print ("✪   𝕐 𝕆 𝕌   𝕄 𝕀 𝕊 𝕊   ✪")
                            print ("✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪\n")
                            coin = coin - (bet * lose_Multipay)
                            print ('coins you have : ',coin,"$\n")
                            choice = None
                    else:
                        print ("your coin is : ", (coin),"$")
                        pass
                except ValueError :
                    if str(bet) != "return":
                        print ('Please enter a valid "number" bet.')
                    elif str(bet) != "hint":
                        print ('Please enter a valid "number" bet.')
            elif choice == "stop" :
                TY()
                break
            elif choice == "hint":
                hint()
                choice = None
                continue
            else:
                print ('Please enter "heads" or "tails" only.\n ')
                choice = None
                pass
        if coin <= minimum :
            print ("\n✌ ✌ ✌ ✌ ✌ ✌ ✌ ✌ ✌ ✌ ✌ ✌ ✌")
            print ('✌     𝕐 𝕆 𝕌  𝕃 𝕆 𝕊 𝕋    ✌')
            print ('✌          ಠ_ಠ          ✌')
            print ("✌ ✌ ✌ ✌ ✌ ✌ ✌ ✌ ✌ ✌ ✌ ✌ ✌\n")
            choice = None
        elif coin >= maximum :
            print ("\n♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛")
            print ('♛      𝕐 𝕆 𝕌  𝕎  𝕀 ℕ    ♛')
            print ('♛       ¯\_(ツ)_/¯      ♛')
            print ("♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛\n")
            choice = None
    elif Play == "OP":
        LV()  
        select_level = input('Your choice :')
        if select_level == '1':
            minimum = 1000
            maximum = 2000
            Win_Multiply = 2
            lose_Multipay = 0.5
            print ('\n======================')
            print ('You are at easy level.')
            print ('======================\n')
        elif select_level == '2':
            minimum = 1000
            maximum = 3000
            Win_Multiply = 1
            lose_Multipay = 1
            print ('\n=======================')
            print ('ou are at medium level.')
            print ('=======================\n')
        elif select_level == '3':
            minimum = 1000
            maximum = 3000
            Win_Multiply = 1
            lose_Multipay = 2
            print ('\n======================')
            print ('You are at hard level.')
            print ('======================\n')
        elif select_level == '4':
            minimum = 1000
            maximum = 10000
            Win_Multiply = 1
            lose_Multipay = 10
            print ('\n=====================================')
            print ('You are at don\'t make mistakes level.')
            print ('=====================================\n')
        elif select_level == 'LOOK LV':
            LV_Detil()
            continue
        else:
            print ('\n==========================')
            print ('You are at Original level.')
            print ('==========================\n')
    elif Play == "n":
        print ( "+----------------------------------+")
        print ( "|         see you later...         |")
        print ( "+----------------------------------+")
        break
    #dsfsdfsdf