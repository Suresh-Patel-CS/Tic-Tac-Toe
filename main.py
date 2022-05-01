#!/usr/bin/env python



from turtle import position


board  = ['-', '-', '-', 
          '-', '-', '-', 
          '-', '-', '-']

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
  # Displays Intial Board
  display_board()

  handle_turn()
 

def handle_turn():
  position = input("Choose a position from 1-9: ")
  position = int(position) - 1

  board[position] = 'X'


play_game()
display_board()


# board
# display 
# play game 
# handle turn
# check win
  # Check row
  # Check Column
  # Check Diagnoal
# check tie

# flip between players
