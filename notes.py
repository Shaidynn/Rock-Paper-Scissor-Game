import random

def get_choices():
    player_choice = input('Enter a choice (rock, paper, scissors): ')
    options = ['rock','paper', 'scissor']
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f'You chose {player}, computer chose {computer}')
    if player == computer:
     return "It's a tie"
    elif player == 'rock':
     if computer == 'scissors':
      return 'rock smashes scissors! You win!'
     else:
       return "paper covers rock! You lose."
    elif player == "paper":
      if computer == 'rock':
        return 'Paper covers rock! You win!'
      else:
        return "Scissors cuts paper! You lose."
    elif player == 'scissors':
      if computer == "paper":
        return "Scissors cuts paper! You win"
      else:
        return "Rock smashes sicssors! You lose."
      
choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)

OR an alternative method could be the following:

import random

starter = input("Would you like to play rock, paper, scissors? Please answer Yes or No. ")

if starter.lower() == "yes":
    starter2 = input("Would you like to pick rock, paper or scissors? ")
    if starter2.lower() == "rock":
        value = random.randint(1, 3)
        if value < 2:
            mode = "rock"
        if value < 2:
            print(f"You picked {starter2} and the computer picked {mode}.")
            quit()
        if value == 2:
            mode = "paper"
        if value == 2:
            print(f"You picked {starter2} and the computer picked {mode}.")
            quit()
        if value > 2:
            mode = "scissors"
        if value > 2:
            print(f"You picked {starter2} and the computer picked {mode}.")
            quit()
    if starter2.lower() == "paper":
        value = random.randint(1, 3)
        if value < 2:
            mode = "rock"
        if value < 2:
            print(f"You picked {starter2} and the computer picked {mode}.")
            quit()
        if  value == 2:
            mode = "paper"
        if  value == 2:
            print(f"You picked {starter2} and the computer picked {mode}.")
            quit()
        if value > 2:
            mode = "scissors"
        if value > 2:
            print(f"You picked {starter2} and the computer picked {mode}.")
            quit()
    if starter2.lower() == "scissors":
        value = random.randint(1, 3)
        if value < 2:
            mode = "rock"
        if value < 2:
            print(f"You picked {starter2} and the computer picked {mode}.")
            quit()
        if  value == 2:
            mode = "paper"
        if  value == 2:
            print(f"You picked {starter2} and the computer picked {mode}.")
            quit()
        if value > 2:
            mode = "scissors"
        if value > 2:
            print(f"You picked {starter2} and the computer picked {mode}.")
            quit()

elif starter.lower() == "no":
    print("See you later! Feel free to revisit us anytime!")
    exit()

else:
    print("Unfortunately, an error has occured. Please try again soon!")


 
    

