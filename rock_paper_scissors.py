import random

def main():
    """
    Rock, Paper, Scissors game.

    The user is asked to choose one of the three options, the computer chooses one at random, and the program finds who the winner is.

    Scores are kept in a dictionary, and player can keep playing as long as they want.
    """
    
    print("Let's play!")
    playerscores = {
        "wins":0,
        "losses":0,
        "ties":0
    }
    while True:
        p1 = playerchoice()
        npc = npcchoice()
        
        if p1 == npc:
            playerscores["ties"] += 1
            print(f"Computer chose {npc.capitalize()} \n You both chose {p1.capitalize()}, that's a tie!")
        else:
            win = winner(p1, npc)
            if win == True:
                playerscores["wins"] += 1
            else:
                playerscores["losses"] += 1
        print(f"Current scores are: {playerscores}")
        playagain = ""
        while playagain != "y" and playagain != "n":    
            playagain = input("Play again? (y/n) ").lower()
        if playagain == "y":
            print("Yay, let's play again!")
        elif playagain == "n":
            break

def playerchoice():
    """
    Ask the player to choose Rock, Paper, or Scissors until valid input is provided.
    """
    while True:
        choice = input("Rock, Paper, or Scissors? ").lower()
        if choice != "rock" and choice != "paper" and choice != "scissors":
            print("Invalid input. Please choose Rock, Paper, or Scissors!")
        else:
            break         
    return choice

def npcchoice():
    """
    The computer randomly selects rock, paper, or scissors.
    """
    choicenum = random.randint(1,3)
    if choicenum == 1:
        choice = "rock"
    elif choicenum == 2:
        choice = "paper"
    else:
        choice = "scissors"
    return choice

def winner(p1, npc):
    """
    Determine the winner based on the rules:
    -Rock crushes Scissors
    -Scissors cuts Paper
    -Paper covers Rock

    Only valid inputs both in p1 and npc are "rock", "paper", or "scissors".
    """
    if p1 == "rock":
        if npc == "paper":
            print(f"Computer chose Paper. \n Paper covers Rock \n Computer wins!")
            return False
        else:
            print(f"Computer chose Scissors. \n Rock crushes Scissors \n You win!")
            return True
    elif p1 == "paper":
        if npc == "rock":
            print(f"Computer chose Rock. \n Paper covers Rock \n You win!")
            return True
        else:
            print(f"Computer chose Scissors. \n Scissors cuts Paper \n Computer wins!")
            return False
    else:
        if npc == "rock":
            print(f"Computer chose Rock. \n Rock crushes Scissors \n Computer wins!")
            return False
        else:
            print(f"Computer chose Paper. \n Scissors cuts Paper \n You win!")
            return True

main()