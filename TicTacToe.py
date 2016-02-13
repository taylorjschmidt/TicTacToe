def start():
	global player_one
	global player_two
	global one_token
	global two_token
	
	player_one = raw_input("Player One, what is your name?\n")
	one_token = raw_input(player_one + ", would you like to be X or O?\n").upper()
	if one_token == 'X':
		two_token = 'O'
		print "OK. Player Two, you will be %s" % two_token
		player_two = raw_input("What is your name?\n")
		print "Great. Let's play!"
	elif one_token == 'O':
		two_token = 'X'
		print "OK. Player Two, you will be %s" % two_token
		player_two = raw_input("What is your name?\n")
		print "Great. Let's play!"
	else:
		print "Sorry, try again."
		start()

def print_board(layout):
	print "Currently, the board looks like this:"
	print ' ' + layout['1'] + ' ' + '|' + ' ' + layout['2'] + ' ' + '|' + ' ' + layout['3']
	print "-" * 11
	print ' ' + layout['4'] + ' ' + '|' + ' ' + layout['5'] + ' ' + '|' + ' ' + layout['6']
	print "-" * 11
	print ' ' + layout['7'] + ' ' + '|' + ' ' + layout['8'] + ' ' + '|' + ' ' + layout['9']
	
def check_winner(board):
	opt1 = board['1'] + board['2'] + board['3']
	opt2 = board['4'] + board['5'] + board['6']
	opt3 = board['7'] + board['8'] + board['9']
	opt4 = board['1'] + board['4'] + board['7']
	opt5 = board['2'] + board['5'] + board['8']
	opt6 = board['3'] + board['6'] + board['9']
	opt7 = board['1'] + board['5'] + board['9']
	opt8 = board['3'] + board['5'] + board['7']
	
	checker = [opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8]
	
	if 'XXX' in checker:
		return 'X'
	elif 'OOO' in checker:
		return 'O'
	else:
		return ' '
	
def check_full(board):
	for k, v in board.items():
		if v == ' ':
			return False
			break
	else:
		return True
		
def one_turn():
	space = raw_input(player_one + ", select a space to make your mark: ")
	if current_board[space] == ' ':
		current_board[space] = one_token
	else:
		print "Sorry, that space is already taken! Let's try again."
		one_turn()
	
def two_turn():
	space = raw_input(player_two + ", select a space to make your mark: ")
	if current_board[space] == ' ':
		current_board[space] = two_token
	else:
		print "Sorry, that space is already taken! Let's try again."
		two_turn()
	
current_board = {'1': ' ', '2': ' ','3': ' ','4': ' ','5': ' ','6': ' ','7': ' ','8': ' ','9': ' '}
winner = check_winner(current_board)
full = check_full(current_board)

print """
We are going to play Tic Tac Toe!
The first player to get three in a row wins!
The board layout is like this:
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9
	  
	"""

start()
while winner == ' ' and not full:
	one_turn()
	winner = check_winner(current_board)
	full = check_full(current_board)
	if winner == one_token:
		print_board(current_board)
		print player_one + " has won! Congratulations!"
		break
	elif full == True:
		print_board(current_board)
		print "This game is a draw!"
		break
	else:
		print_board(current_board)
		pass
	two_turn()
	winner = check_winner(current_board)
	full = check_full(current_board)
	if winner == two_token:
		print_board(current_board)
		print player_two + " has won! Congratulations!"
		break
	elif full == True:
		print_board(current_board)
		print "This game is a draw!"
		break
	else:
		print_board(current_board)
		pass
