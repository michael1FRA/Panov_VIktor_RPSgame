from gameComponents import gameVars, winLose

def beg():
	print("===============*/ RPS /*====================")
	print("    Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("    Player Lives:  ", gameVars.player_lives, "/", gameVars.total_lives)
	print("============================================")
	print("Choose your weapon! or type quit to exit\n")