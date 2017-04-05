#!/usr/bin/env python

import random

player_mark = 'X'
computer_mark = 'O'

ttt_grid = [' '] * 10

def choose_first_player():
    if random.randint(0, 1) == 0:
        return player_mark
    else:
        return computer_mark

def check_winner(mark):
    return ((ttt_grid[7] == mark and ttt_grid[8] == mark and ttt_grid[9] == mark) or # across the top
    (ttt_grid[4] == mark and ttt_grid[5] == mark and ttt_grid[6] == mark) or # across the middle
    (ttt_grid[1] == mark and ttt_grid[2] == mark and ttt_grid[3] == mark) or # across the bottom
    (ttt_grid[7] == mark and ttt_grid[4] == mark and ttt_grid[1] == mark) or # down the middle
    (ttt_grid[8] == mark and ttt_grid[5] == mark and ttt_grid[2] == mark) or # down the middle
    (ttt_grid[9] == mark and ttt_grid[6] == mark and ttt_grid[3] == mark) or # down the right side
    (ttt_grid[7] == mark and ttt_grid[5] == mark and ttt_grid[3] == mark) or # diagonal
    (ttt_grid[9] == mark and ttt_grid[5] == mark and ttt_grid[1] == mark)) # diagonal

def space_check(position):
    return ttt_grid[position] == ' '

def full_grid_check():
    for i in range(1,10):
        if space_check(i):
            return False
    return True

def player_choice(mark):
    position = 0
    while position not in range(1,10) or not space_check(int(position)):
	if(mark == computer_mark):
		position = random.randint(1, 10)
	else:
        	position = raw_input("What's your next move? ")
		position = int(position)

    return int(position)

def show_grid():
    print '   |   |'
    print ' ' + ttt_grid[7] + ' | ' + ttt_grid[8] + ' | ' + ttt_grid[9]
    print '   |   |'
    print '-----------'
    print '   |   |'
    print ' ' + ttt_grid[4] + ' | ' + ttt_grid[5] + ' | ' + ttt_grid[6]
    print '   |   |'
    print '-----------'
    print '   |   |'
    print ' ' + ttt_grid[1] + ' | ' + ttt_grid[2] + ' | ' + ttt_grid[3]
    print '   |   |'
    print "\n"

def place_marker(marker, position):
    ttt_grid[position] = marker

print "============================================="
print "Let's play Tic Tac Toe!"
print "============================================="

whos_next  = choose_first_player()

play_in_progress = True

while play_in_progress:
	if whos_next == player_mark:
	    show_grid()
	    position = player_choice(player_mark)
	    place_marker(player_mark, position)

	    if check_winner(player_mark):
		show_grid()
		print 'Congratulations! You have won the game!'
		play_in_progress = False
	    else:
		if full_grid_check():
		    show_grid()
		    print 'The game is a draw!'
		    break
		else:
		    whos_next = computer_mark
	else: # Computer's turn.
	    print "Now it's my turn.."
	    show_grid()
	    position = player_choice(computer_mark)
	    place_marker(computer_mark, position)

	    if check_winner(computer_mark):
		show_grid()
		print 'Better luck next time! :)'
		play_in_progress = False
	    else:
		if full_grid_check():
		    show_grid()
		    print 'The game is a tie!'
		    break
		else:
		    whos_next = player_mark
