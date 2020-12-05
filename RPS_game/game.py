# import packages to extend python
from random import randint

# re-import our game variables
from gameComponents import gameVars, winLose, start, printer

# set up our game loop
while gameVars.player is False:
	# shorten the beginning
	start.beg()

	gameVars.player = input("Choose rock, paper or scissors: \n")

	if gameVars.player == "quit":
		print("You chose to quit, quitter!")
		exit()

	computer = gameVars.choices[randint(0, 2)]

	print("user chose: " + gameVars.player)
	print("AI chose:   " + computer)

	if (computer == gameVars.player):
		print("TIE")

	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			printer.lose()
		else:
			printer.win()

	elif (computer == "paper"):
		if (gameVars.player == "scissors"):
			printer.lose()
		else:
			printer.win()


	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			printer.lose()
		else:
			printer.win()

	# check player lives and AI lives
	if gameVars.player_lives == 0:
		winLose.winorlose("lost")

	elif gameVars.computer_lives == 0:
		winLose.winorlose("won")

	else:
		gameVars.player = False
