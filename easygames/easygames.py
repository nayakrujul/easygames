import os
import random


'''
Function for one game of Rock-Paper-Scissors - user vs computer.
This gets the input from the user, randomly generates one for the computer, and works out the winner.

Return values:
0 if draw
1 if player wins
2 if computer wins
'''

def rock_paper_scissors():
	options = ['R', 'P', 'S']
	computer_choice = random.choice(options)
	while True:
		user_choice = input('Choose Rock (R), Paper (P), or Scissors (S): ').upper()
		if user_choice:
			if user_choice[0] in options:
				break
		print('Invalid choice')
	print('Computer chose:', computer_choice)
	diff = options.index(user_choice[0]) - options.index(computer_choice)
	if diff < 0:
		diff += 3
	if diff == 0:
		print('Draw!')
	elif diff == 1:
		print('You win!')
	else:
		print('Computer wins!')
	return diff
