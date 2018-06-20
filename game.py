import numpy as np
from player import Player
from gameboard import gameBoard
from agent import Agent

class Game:

	p1 = None
	p2 = None
	numTurns = 0
	state = ''
	numFlipped = 0

	def __init__(self):
		sel = np.random.randint(0, 24)
		g1 = gameBoard(sel)
		#self.p1 = Player("PLAYER 1", g1, sel)
		self.p1 = Agent("Charlie", g1, sel)
		print(self.p1.getName() + " selected " + self.p1.getBoard().getCharacter(self.p1.getBoard().getSelected()).getName())
		j = np.random.randint(0, 24)
		g2 = gameBoard(j)
		#self.p2 = Player("PLAYER 2", g2, j)
		self.p2 = Agent("Alex", g2, j)
		print(self.p2.getName() + " selected " + self.p2.getBoard().getCharacter(self.p2.getBoard().getSelected()).getName())
		numTurns = 0 
		self.state = 'START'
		self.numFlipped = 0

	def getState(self):
		if(self.state == 'WIN' or self.state == 'LOST'):
			return state
		else:
			return str(self.numFlipped)


	def getAction(self, i):
		if self.numTurns % 2 == 0:
			player = self.p1
			otherplayer = self.p2
		else:
			player = self.p2
			otherplayer = self.p1
		#each number corresponds to an action 
		#auto quit (debug only)
		if i == -1: 
			quit()
		#guess specific character
		if i >= 0 and i < 24:
			if(i == otherplayer.getBoard().getSelected()):
				print("CORRECT GUESS")
				player.setScore(player.getScore() + 1)
				if numTurns % 2 == 0:
					self.state = 'WON'
				else:
					self.state = 'LOST'
			else:
				print("INCORRECT GUESS")
				otherplayer.setScore(otherplayer.getScore() + 1)
				if numTurns % 2 == 0:
					self.state = 'LOST'
				else:
					self.state = 'WON'
			return 
		#y/n questions
		self.numFlipped = 0
		if i == 24:
			characterList, self.numFlipped = player.getBoard().askQ('isFemale', otherplayer.getBoard())
			player.getBoard().updateList(characterList
		if i == 25:
			characterList, self.numFlipped = player.getBoard().askQ('hasHat', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		if i == 26:
			characterList, self.numFlipped = player.getBoard().askQ('hasGlasses', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		if i == 27:
			characterList, self.numFlipped = player.getBoard().askQ('hasBeard', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		if i == 28:
			characterList, self.numFlipped = player.getBoard().askQ('hasMustache', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		if i == 29:
			characterList, self.numFlipped = player.getBoard().askQ('hasRosyCheeks', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		if i == 30:
			characterList, self.numFlipped = player.getBoard().askQ('isSmiling', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		if i == 31:
			characterList, self.numFlipped = player.getBoard().askQ('isBald', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		#binary search
		if i == 32:
			binaryPositions, characterlist, self.numFlipped = player.getBoard().binarySearch(player.getBinaryPositions(), otherplayer.getBoard())
			player.getBoard().updateList(characterlist)
			player.setBinaryPositions(binaryPositions)
		#hair colors
		else:
			characterlist, self.numFlipped = player.getBoard().askHairColor(i, otherplayer.getBoard())
			player.getBoard().updateList(characterlist)
		if self.numTurns % 2 == 0:
			self.p1 = player
		else:
			self.p2 = player

	def main(self): 
		p1turns = 0
		p2turns = 0 
		gameOver = False

		while(gameOver == False):
			#self.p1 gets even turns
			if(self.numTurns % 2 == 0):
				p1turns += 1
				action = 35
				print(self.p1.getName() + " is guessing" + str(action))
				#action = int(input("ACTION 1-40"))
				if(action >= 0 and action < 24):
					self.getAction(action)
					gameOver = True
				#for debug
				elif(action == -1):
					quit()
				else:
					self.getAction(action)
					print('P1 ACTIVE: ' + str(self.p1.getBoard().numberActive()))
					print('P2 ACTIVE: ' + str(self.p2.getBoard().numberActive()))
					if(self.p1.getBoard().numberActive() <= 1):
						self.p1.setScore(self.p1.getScore() + 1)
						print("PLAYER 1 WINS")
						self.state = 'WON'
						gameOver = True
			else: 
				p2turns += 1
				action = 35
				print(self.p2.getName() + " is guessing" + str(action))
				#action = int(input("ACTION 1-40"))
				if(action >= 0 and action < 24):
					self.getAction(action)
					gameOver = True
				#for debug
				elif(action == -1):
					quit()
				else:
					self.getAction(action)
					print("P1 ACTIVE: " + str(self.p1.getBoard().numberActive()))
					print("P2 ACTIVE: " + str(self.p2.getBoard().numberActive()))
					if(self.p2.getBoard().numberActive() <= 1):
						self.p2.setScore(self.p2.getScore() + 1)
						print("PLAYER 2 WINS")
						self.state = 'LOST'
						gameOver = True
			self.numTurns += 1
			print("TOTAL TURNS: " + str(self.numTurns))
			print("self.p1 TURNS: " + str(p1turns))
			print("self.p2 TURNS: " + str(p2turns))