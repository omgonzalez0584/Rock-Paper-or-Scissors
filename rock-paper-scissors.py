import random

print("Welcome to the game - Rock, Paper and Scissors!")
player1 = input("Input rock, paper o scissors. x for exit: ")
lista = ['rock','paper','scissors']
player2 = random.choice(lista)
while True:

    if player1 != 'x':
    
        if player1 == 'rock':
            if player2 == 'paper':
                print(f"player 1: {player1} - player 2: {player2}, paper wins!")
            elif player2 == 'scissors':
                print(f"player 1: {player1} - player 2: {player2}, rock wins!")
            else:
                print(f"player 1: {player1} - player 2: {player2}, draw!")

        elif player1 == 'paper':
            if player2 == 'scissors':
                print(f"player 1: {player1} - player 2: {player2}, scissors wins!")
            elif player2 == 'rock':
                print(f"player 1: {player1} - player 2: {player2}, paper wins!")
            else:
                print(f"player 1: {player1} - player 2: {player2} , draw!")

        elif player1 == 'scissors':  
            if player2 == "rock":
                print(f"player 1: {player1} - player 2: {player2}, rock wins!")
            elif player2 == "paper":
                print(f"player 1: {player1} - player 2: {player2}, scissors wins!")
            else:
                print(f"player 1: {player1} - player 2: {player2}, draw!")
        
        else:
            print("Invalid option, try again: ")

        player1 = input("Input rock, paper o scissors. x for exit: ")
        player2 = random.choice(lista)


    else:
        print("Good bye!")
        break
    

    