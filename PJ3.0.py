import random

coin = 0
coin_player2 = 1500
choice = None
minimum = 1000
maximum = 2000
Win_Multiply = 1
lose_Multipay = 1
count_wins_player1 = 0
count_losses_player1 = 0
count_wins_player2 = 0
count_losses_player2 = 0
score_player1 = 0
score_player2 = 0
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
    print ("|  IN A Don't make mistakes  Game.         |        1       |       10        |     10000     |     1000      |")
    print ("|                                                                                                             |")
    print ("|                                    Good luck, have fun with the game.                                       |")
    print ("+-------------------------------------------------------------------------------------------------------------+\n")


def play_player2():
    print ("\n\n-------------------------------")
    print ("-        heads or tails       -")
    print ("-------------------------------\n\n")
    print ('coins player 2 has: ', coin_player2, "$\n")
def play_turn_player2():
    global coin_player2
    choice_player2 = input(f'Player 2, guess heads or tails using "heads" or "tails": ')
    if choice_player2 == "heads" or choice_player2 == "tails":
        try:
            bet_player2 = int(input(f'Player 2, enter the amount to bet: '))
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
                    print('coins player 2 has: ', coin_player2, "$\n")
                elif correct_player2 != choice_player2:
                    print("\n✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪")
                    print("✪   𝕐 𝕆 𝕌   𝕄 𝕀 𝕊 𝕊   ✪")
                    print("✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪\n")
                    coin_player2 -= bet_player2
                    print('coins player 2 has: ', coin_player2, "$\n")
            else:
                print("Player 2's coin is: ", coin_player2, "$")
        except ValueError:
            print('Please enter a valid "number" bet.')
    else:
        print('Player 2, please enter "heads" or "tails" only.\n ')

def play_turn():
    global coin, choice
    if choice is None:
        choice = input(f'Guess heads or tails using "heads" or "tails". : ')
    if choice == "heads" or choice == "tails":
        try:
            bet = int(input(f'Price to bet : '))
            if bet <= coin:
                print()
                correct = random.choice(["heads", "tails"])
                if correct == "heads":
                    HEAD()
                if correct == "tails":
                    TAIL()
                if correct == choice:
                    print("\n★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")
                    print("★   ℂ 𝕆 ℝ ℝ 𝔼 ℂ 𝕋   ★")
                    print("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★\n")
                    coin += (bet * Win_Multiply)
                    print('coins you have : ', coin, "$\n")
                    choice = None
                elif correct != choice:
                    print("\n✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪")
                    print("✪   𝕐 𝕆 𝕌   𝕄 𝕀 𝕊 𝕊   ✪")
                    print("✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪\n")
                    coin -= (bet * lose_Multipay)
                    print('coins you have : ', coin, "$\n")
                    choice = None
            else:
                print("Your coin is : ", (coin), "$")
        except ValueError:
            print('Please enter a valid "number" bet.')
    elif choice == "stop":
        TY()
    elif choice == "hint":
        hint()
        choice = None
    else:
        print('Please enter "heads" or "tails" only.\n ')
        choice = None


    
    print(f"Player 1: Wins {count_wins_player1}, Losses {count_losses_player1}")
    print(f"Player 2: Wins {count_wins_player2}, Losses {count_losses_player2}\n")
    
    print(f"Current Scores - Player 1: {coin}, Player 2: {coin_player2}\n")
print ("\n\nWelcome to the head or tails guessing game.\n")
while coin == 0:
    Play = input(f'Do you want to play the game? y/n : ')
    if Play == "y":
        coin = 1500
        play()

        while coin > minimum and coin < maximum and coin_player2 > minimum and coin_player2 < maximum:
            play_turn()
            play_turn_player2()
    
        if coin <= minimum or coin >= maximum:
            if coin == coin_player2:
                print("It's a draw!\n")
            else:
                print(f"Player {1 if coin > coin_player2 else 2} Wins!\n")
                if coin <= minimum:
                    count_wins_player2 += 1
                    count_losses_player1 += 1
                elif coin >= maximum:
                    count_wins_player1 += 1
                    count_losses_player2 += 1
        
        if coin > coin_player2:
            print("Player 1 is the overall winner!")
        elif coin < coin_player2:
            print("Player 2 is the overall winner!")
        else:
            print("It's a tie in the overall score!")
        break
print(f"Player 1: Wins {count_wins_player1}, Losses {count_losses_player1}")
print(f"Player 2: Wins {count_wins_player2}, Losses {count_losses_player2}\n")
    
print(f"Current Scores - Player 1: {coin}, Player 2: {coin_player2}\n")
