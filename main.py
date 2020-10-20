from modules import *
from random import randint
#dodaj: random prvi igrac, online glasanje, trka zivotinja

def scoring(players, first):

	for i in range(first + 1, len(players) + first + 1):
		if players[first].vote == players[(first + i) % len(players)].vote: 
			all_guesses = True
		else:
			all_guesses = False
			break

	if all_guesses == True:
		for i in range(first + 1, len(players) + first):
			players[i % len(players)].score += 2 
		return players



	for i in range(first + 1, len(players) + first): 
		if players[first].vote != players[i % len(players)].vote: 
			no_guesses = True
		else:
			no_guesses = False
			break

	if no_guesses == True:
		for i in range(first + 1, len(players) + first):
			players[i % len(players)].score += 2
			if players[first].vote != players[i % len(players)].vote: 
				if players[players[i % len(players)].vote % len(players)].card == 7:
					players[players[i % len(players)].vote % len(players)].card = int(input("Card number " + str(players[i % len(players)].vote) + " belong to player: ")) - 1
					players[players[players[i % len(players)].vote % len(players)].card].score += 1
				else:
					players[players[players[i % len(players)].vote % len(players)].card].score += 1
		return players

	for i in range(len(players)):
		if players[first].vote == players[i].vote:
			players[i].score += 3
		else:
			if players[players[i].vote % len(players)].card == 7:
				ask = True
				while ask: 
					whose_card = input("Card number " + str(players[i].vote) + " belong to player: ")
					if isitint(whose_card):
						if int(whose_card) in range(1, len(players)+1):
							players[players[i].vote % len(players)].card = int(whose_card) - 1
							ask = False
					else:
						for j in range(len(players)):
							if players[j].name == str(whose_card):
								players[players[i].vote % len(players)].card = j
								ask = False
					if ask:
						print("Not existing player, please enter again!")

				players[players[players[i].vote % len(players)].card].score += 1
			else:
				players[players[players[i].vote % len(players)].card].score += 1

	return players


while True:

	try: 
		nop = int(input("Enter a number of players: "))

		if nop in [3, 4, 5, 6]:
			break
		elif not(nop in [3, 4, 5, 6]):
			print("It is allowed to have from 3 to 6 players, please enter again!")	
	except ValueError:
		print("Invalid input, enter a number of players")

players = []

for player in range(nop):
	players.append(Player(input("Enter a name of player " + str(player + 1) + ": "), 0, 0, 0, 7))


first = randint(1, nop)
game = True
while game:
	first = (first +1) % len(players)
	print("It's your turn " + str(players[first].name))

	for i in range(len(players)):
		players[i].vote = int(input(str(players[i].name) + " enter your vote: "))


	players = scoring(players, first)

	for i in range(len(players)):
		players[i].card = 7
		if players[i].score >= 30:
			game = False
			print("Winner is " + players[i].name + "! ")

	for player in players:
		print(player.name, str(player.score))
