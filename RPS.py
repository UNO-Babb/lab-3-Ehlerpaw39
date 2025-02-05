#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  options = ["R", "P","S"]
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.
  Player_choice = input("Enter choice (R for rock, P for paper, S for scissor):") . upper()
  if Player_choice not in options:
    print("invalid input. please enter R, P, OR S.")
    computer_choice = random.choice(options)
    print(f"computer chose:{computer_choice}")
    if Player_choice == computer_choice:
      print("It's a tie!")
      ties += 1 
  elif (Player_choice =="R"and computer_choice == "S") or \
       (Player_choice =="P"and computer_choice == "R") or \
       (Player_choice =="S"and computer_choice == "P"):
    print("You win")
    wins += 1
  else:
    print("You lose")
    losses += 1
  Play_again = input("would you like to play again? (Y/N):") .upper()
  if Play_again != "Y": 
    breakpoint
  #In the end, print the stats
  print("\nFinal Stats:")
  print("Win\tTies\tLosses")
  print(f"{wins}\t{ties}\t{losses}")

if __name__ == '__main__':
  main()
