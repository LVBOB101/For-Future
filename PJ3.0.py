import random
import time
minimum = 1000
maximum = 2000
coin = 0
coin_player2 = 0
choice = None
choice_player2 = None
Win_Multiply = 1
lose_Multipay = 1
num_players = 0
Name_player1 = None
Name_player2 = None
lastchoice_player1 = "heads"
lastchoice_player2 = "heads"
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
    print ("|  IN A Don't make mistakes  Game.         |        1       |      10000      |     10000     |     1000      |")
    print ("|                                                                                                             |")
    print ("|                                    Good luck, have fun with the game.                                       |")
    print ("+-------------------------------------------------------------------------------------------------------------+\n")

    global coin_player2, choice_player2 , elapsed_time
    if choice_player2 is None:
        start_time = time.time()
        elapsed_time = 0
        correct_player2 = random.choice(["heads", "tails"])
        print('You have 15 seconds to make your guess...')
        while elapsed_time == 0:
            try :
                choice_player2 = input(f'{Name_player2}, guess heads or tails using "heads" or "tails": ')
                if choice_player2.lower() in ["heads", "tails"]:
                    elapsed_time = time.time() - start_time
                    if elapsed_time >= 15:
                        choice_player2 = lastchoice_player2
                    else:
                        print(f'Time remaining: {15 - elapsed_time:.2f} seconds')
            except ValueError:
                print('Please enter "heads" or "tails" only.')
        elapsed_time = 0
        start_time = time.time()
        try :
            bet_player2 = int(input(f'{Name_player2}, enter the amount to bet: '))
            if bet_player2 <= coin_player2 :
                elapsed_time = time.time() - start_time
                if elapsed_time >= 15:
                    bet_player2 = coin_player2
                else:
                    print(f'Time remaining: {15 - elapsed_time:.2f} seconds')
            else:
                print(f'{Name_player2} coin is: ', coin_player2, "$")
        except ValueError:
            print('Please enter a valid "number" bet.')
    if correct_player2 == choice_player2:
        print("\n★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")
        print("★   ℂ 𝕆 ℝ ℝ 𝔼 ℂ 𝕋   ★")
        print("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★\n")
        coin_player2 += (bet_player2 * Win_Multiply)
        print('coins you have : ', coin, "$\n")
        choice_player2 = None
        choice = None
    elif correct_player2 != choice_player2:
        print("\n✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪")
        print("✪   𝕐 𝕆 𝕌   𝕄 𝕀 𝕊 𝕊   ✪")
        print("✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪\n")
        coin_player2 -= (bet_player2 * lose_Multipay)
        print('coins you have : ', coin, "$\n")
        choice_player2 = None
        choice = None
while num_players not in [1, 2]:
    num_players_input = input('Enter the number of players (1 or 2): ')
    try:
        num_players = int(num_players_input)
    except ValueError:
        print('Please enter a valid number (1 or 2).')

print ("\n\nWelcome to the head or tails guessing game.\n")

while num_players in [1, 2]:
    Play = input('Do you want to play the game? (y/n): ')
    if Play == "y":

        if num_players == 1:
            Name_player1 = input('player 1, Enter your name: ')
            coin = 1500
            coin_player2 = 1500
        elif num_players == 2:
            Name_player1 = input('player 1, Enter your name: ')
            Name_player2 = input('player 2, Enter your name: ')
            coin = 1500
            coin_player2 = 1500
        
        play()

        while coin > minimum and coin < maximum and coin_player2 > minimum and coin_player2 < maximum:
            if num_players == 1:
                if choice is None:
                    start_time = time.time()
                    elapsed_time = 0
                    correct = random.choice(["heads", "tails"])
                    print('You have 15 seconds to make your guess...')
                    while elapsed_time == 0:
                        try :
                            if choice is None :
                                choice = input(f'{Name_player1} Guess heads or tails using "heads" or "tails". : ')
                                if choice == "heads" or "tails" :
                                    elapsed_time = time.time() - start_time
                                elif choice == "stop":
                                    break
                                if elapsed_time >= 15:
                                    choice = lastchoice_player1
                            else:
                                print(f'Time remaining: {15 - elapsed_time:.2f} seconds')
                        except ValueError:
                            choice = None
                            print('Please enter "heads" or "tails" only.')
                            continue
                        elapsed_time = 0
                        start_time = time.time()
                        try :
                            if choice is not None :
                                print(f'{Name_player1}, can type "return" to go back: ')
                                bet = (input(f'Place your bet: '))
                                if bet == "return":
                                    choice = None
                                    continue
                                bet = int(bet)
                                if choice != None and bet <= coin :
                                    elapsed_time = time.time() - start_time
                                    if elapsed_time >= 15:
                                        print(f'Time remaining: {15 - elapsed_time:.2f} seconds')
                                        bet = coin
                                    else:
                                        print(f'Time remaining: {15 - elapsed_time:.2f} seconds')
                                    if correct == "heads" :
                                        HEAD()
                                    elif correct == "tails":
                                        TAIL()
                                    if correct == choice:
                                        print("\n★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")
                                        print("★   ℂ 𝕆 ℝ ℝ 𝔼 ℂ 𝕋   ★")
                                        print("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★\n")
                                        coin += (bet * Win_Multiply)
                                        print('coins you have : ', coin, "$\n")
                                        choice_player2 = None
                                        choice = None       
                                    elif correct != choice:                                   
                                        print("\n✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪")
                                        print("✪   𝕐 𝕆 𝕌   𝕄 𝕀 𝕊 𝕊   ✪")
                                        print("✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪\n")
                                        coin -= (bet * lose_Multipay)
                                        print('coins you have : ', coin, "$\n")
                                        choice_player2 = None
                                        choice = None
                                else:
                                    print(f'{Name_player1} coin is: ', coin, "$")
                        except ValueError:
                            if str(bet) != "return":
                                print ('Please enter a valid "number" bet.')
            elif num_players == 2:
                ###player 1
                if choice_player2 is None:
                    start_time = time.time()
                    elapsed_time = 0
                    correct = random.choice(["heads", "tails"])
                    print('You have 15 seconds to make your guess...')
                    while elapsed_time == 0:
                        try :
                            if choice is None :
                                choice = input(f'{Name_player1} Guess heads or tails using "heads" or "tails". : ')
                                if choice.lower() in ["heads", "tails"]:
                                    elapsed_time = time.time() - start_time
                                elif choice == "stop":
                                    break
                                if elapsed_time >= 15:
                                    choice = lastchoice_player1
                            else:
                                print(f'Time remaining: {15 - elapsed_time:.2f} seconds')
                        except ValueError:
                            choice = None
                            print(f'{Name_player1},Please enter "heads" or "tails" only.')
                        elapsed_time = 0
                        start_time = time.time()
                        try :
                            print(f'{Name_player1}, can type "return" to go back: ')
                            bet = (input(f'Place your bet: '))
                            if bet == "return":
                                choice = None
                                continue
                            bet = int(bet)
                            if choice != None and bet <= coin :
                                elapsed_time = time.time() - start_time
                                if elapsed_time >= 15:
                                    print(f'Time remaining: {15 - elapsed_time:.2f} seconds')
                                    bet = coin
                                else:
                                    print(f'Time remaining: {15 - elapsed_time:.2f} seconds')
                                if correct == "heads" :
                                    HEAD()
                                elif correct == "tails":
                                    TAIL()
                                if correct == choice:
                                    print("\n★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")
                                    print("★   ℂ 𝕆 ℝ ℝ 𝔼 ℂ 𝕋   ★")
                                    print("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★\n")
                                    coin += (bet * Win_Multiply)
                                    print('coins you have : ', coin, "$\n")
                                    choice_player2 = None
                                    choice = None       
                                elif correct != choice:                                   
                                    print("\n✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪")
                                    print("✪   𝕐 𝕆 𝕌   𝕄 𝕀 𝕊 𝕊   ✪")
                                    print("✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪\n")
                                    coin -= (bet * lose_Multipay)
                                    print('coins you have : ', coin, "$\n")
                                    choice_player2 = None
                                    choice = None
                            else:
                                print(f'{Name_player1} coin is: ', coin, "$")
                        except ValueError:
                            if str(bet) != "return":
                                print ('Please enter a valid "number" bet.')
                ###player2                
                if choice is None:    
                    start_time = time.time()
                    elapsed_time = 0
                    correct_player2 = random.choice(["heads", "tails"])
                    print('You have 15 seconds to make your guess...')
                    while elapsed_time == 0:
                        try :
                            if choice is None :
                                choice_player2 = input(f'{Name_player2} Guess heads or tails using "heads" or "tails". : ')
                                if choice_player2.lower() in ["heads", "tails"]:
                                    elapsed_time = time.time() - start_time
                                elif choice_player2 == "stop":
                                    break
                                if elapsed_time >= 15:
                                    choice_player2 = lastchoice_player2
                            else:
                                print(f'Time remaining: {15 - elapsed_time:.2f} seconds')
                        except ValueError:
                            choice_player2 = None
                            print(f'{Name_player2},Please enter "heads" or "tails" only.')
                        elapsed_time = 0
                        start_time = time.time()
                        try :
                            print(f'{Name_player2}, can type "return" to go back: ')
                            bet_player2 = (input(f'Place your bet: '))
                            if bet_player2 == "return":
                                choice_player2 = None
                                continue
                            bet_player2 = int(bet)
                            if choice_player2 != None and bet_player2 <= coin_player2 :
                                elapsed_time = time.time() - start_time
                                if elapsed_time >= 15:
                                    print(f'Time remaining: {15 - elapsed_time:.2f} seconds')
                                    bet_player2 = coin_player2
                                else:
                                    print(f'Time remaining: {15 - elapsed_time:.2f} seconds')
                                if correct_player2 == "heads" :
                                    HEAD()
                                elif correct_player2 == "tails":
                                    TAIL()
                                if correct_player2 == choice_player2:
                                    print("\n★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")
                                    print("★   ℂ 𝕆 ℝ ℝ 𝔼 ℂ 𝕋   ★")
                                    print("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★\n")
                                    coin_player2 += (bet_player2 * Win_Multiply)
                                    print('coins you have : ', coin, "$\n")
                                    choice_player2 = None
                                    choice = None       
                                elif correct_player2 != choice:                                   
                                    print("\n✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪")
                                    print("✪   𝕐 𝕆 𝕌   𝕄 𝕀 𝕊 𝕊   ✪")
                                    print("✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪\n")
                                    coin_player2 -= (bet_player2 * lose_Multipay)
                                    print('coins you have : ', coin, "$\n")
                                    choice_player2 = None
                                    choice = None
                            else:
                                print(f'{Name_player1} coin is: ', coin, "$")
                        except ValueError:
                            if str(bet) != "return":
                                print ('Please enter a valid "number" bet.')
        if num_players == 1:
            if coin <= minimum :
                print(f"{Name_player1} loses!\n")
                break
            elif coin >= maximum:
                print(f"{Name_player1}, Wins!\n")
            print(f"Current Scores - {Name_player1}: {coin}\n")
            break
        elif num_players == 2:
            if coin > coin_player2:
                print(f"{Name_player1} is the overall winner!")
            elif coin < coin_player2:
                print(f"{Name_player2} is the overall winner!")
            else:
                print("It's a draw!\n")
            print(f"Current Scores - {Name_player1}:{coin}, {Name_player2}: {coin_player2}\n")
            break
    elif Play == "n":
        break
    else:
        print('Please enter "y" or "n" only.\n')
