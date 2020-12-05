from gameComponents import gameVars, winLose

def win():
	print("YOU WIN!")
	gameVars.computer_lives -= 1

def lose():
	gameVars.player_lives -= 1
	print("YOU LOSE!")

