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
lastchoice_player1 = None
lastchoice_player2 = None
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
    print("\n\n+----------------------------------+")
    print("|     Thank you for playing...     |")
    print("+----------------------------------+\n\n")
    print("Summary:")
    print(f"Player 1: Wins {count_wins_player1}, Losses {count_losses_player1}")
    print(f"Player 2: Wins {count_wins_player2}, Losses {count_losses_player2}\n")
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
def play_player2():
    print ("\n\n-------------------------------")
    print ("-        heads or tails       -")
    print ("-------------------------------\n\n")
    print ('coins player 2 has: ', coin_player2, "$\n")
def play_turn_player2():
    global coin_player2, choice_player2
    if choice_player2 is None:
        choice_player2 = input(f'{Name_player2}, guess heads or tails using "heads" or "tails": ')
    if choice_player2 == "heads" or choice_player2 == "tails":
        try:
            bet_player2 = int(input(f'{Name_player2}, enter the amount to bet: '))
            if bet_player2 <= coin_player2:
                print()
                correct_player2 = random.choice(["heads", "tails"])
                if correct_player2 == "heads":
                    HEAD()
                if correct_player2 == "tails":
                    TAIL()
                if correct_player2 == choice_player2:
                    print("\n★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")
                    print("★   ℂ 𝕆 ℝ ℝ 𝔼 ℂ 𝕋   ★")
                    print("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★\n")
                    coin_player2 += bet_player2
                    print(f'coins {Name_player2} has: ', coin_plaer2, "$\n")
                    choice_player2 = None
                    choice = None
                elif correct_player2 != choice_player2:
                    print("\n✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪")
                    print("✪   𝕐 𝕆 𝕌   𝕄 𝕀 𝕊 𝕊   ✪")
                    print("✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪\n")
                    coin_player2 -= bet_player2
                    print(f'coins {Name_player2} has: ', coin_player2, "$\n")
                    choice_player2 = None
                    choice = None
            else:
                print(f"{Name_player2} coin is: ", coin_player2, "$")
        except ValueError:
            print('Please enter a valid "number" bet.')
    else:
        print(f'{Name_player2}, please enter "heads" or "tails" only.\n ')

def play_turn():
    global coin, choice
    choice = input(f'Guess heads or tails using "heads" or "tails": ')
    
    if choice == "heads" or choice == "tails":
        try:
            bet = int(input(f'Place your bet: '))
            if bet <= coin:
                print()
                correct = random.choice(["heads", "tails"])
                if correct == "heads":
                    HEAD()
                if correct == "tails":
                    TAIL()
                
                print('You have 15 seconds to make your guess...')
                
                start_time = time.time()
                elapsed_time = 0
                
                while elapsed_time < 15:
                    try:
                        guess = input('Enter your guess (heads/tails): ')
                        if guess.lower() in ["heads", "tails"]:
                            elapsed_time = time.time() - start_time
                            if elapsed_time >= 15:
                                guess = "tails"
                                continue
                            else:
                                print(f'Time remaining: {15 - elapsed_time:.2f} seconds')
                        else:
                            print('Please enter a valid guess (heads or tails).')
                    except ValueError:
                        print('Please enter a valid guess (heads or tails).')
                
                if elapsed_time < 15:
                    if correct == guess.lower():
                        print("\n★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")
                        print("★   ℂ 𝕆 ℝ ℝ 𝔼 ℂ 𝕋   ★")
                        print("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★\n")
                        coin += (bet * Win_Multiply)
                        print('You have won! Coins remaining: ', coin, "$\n")
                    else:
                        print("\n✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪")
                        print("✪   𝕐 𝕆 𝕌   𝕄 𝕀 𝕊 𝕊   ✪")
                        print("✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪\n")
                        coin -= (bet * lose_Multipay)
                        print('You have lost! Coins remaining: ', coin, "$\n")
                else:
                    print('Time is up! Your guess is not accepted.\n')
                    
            else:
                print("Your coin is : ", (coin), "$")
        except ValueError:
            print('Please enter a valid "number" bet.')
    elif choice == "stop":
        TY()
    elif choice == "hint":
        hint()
    else:
        print('Please enter "heads" or "tails" only.\n ')

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
            Name_playrer1 = input('player 1, Enter your name: ')
            coin = 1500
            coin_player2 = 1500
        elif num_players == 2:
            Name_playrer1 = input('player 1, Enter your name: ')
            Name_playrer2 = input('player 2, Enter your name: ')
            coin = 1500
            coin_player2 = 1500
        
        play()

        while coin > minimum and coin < maximum and coin_player2 > minimum and coin_player2 < maximum:
            if num_players == 1:
                play_turn()
            elif num_players == 2:
                if choice_player2 is None:
                    play_turn()
                if choice is None:    
                    play_turn_player2()
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
