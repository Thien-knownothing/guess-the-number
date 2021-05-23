#Number Guessing Game Objectives:
# Include an ASCII art logo.
from art import logo
from replit import clear
import random

game_on = True

def guess(number,turn):
  guessed = int(input("Please guess a number in range 0-100: " ))
  if guessed > number:
    print("too hight")
  elif guessed < number:
    print("too low")
  elif guessed == number:
    print("you get it right")
  else:
    print('Please select an input in range')
  turn -=1
  return guessed,turn
  

while game_on:
  print(logo)
  number = random.randint(1,100)
  turn = 0
  mode = input("Please select game mode, easy or hard: ")
  if mode[0].lower() == "e":
    turn = 10
  elif mode[0].lower() == "h":
    turn = 5

  while turn >0:
    para = guess(number,turn)
    if para[1] == 0:
      print("You run out of turn")
    if para[0] == number:
      break
    else:
      turn -=1
      print(f"Your left turn: {para[1]}")
      
  if input("do you want to play another game, Yes/No: ")[0] == "n":
    print("thanks for play")
    game_on = False
  else:
    clear()



# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

