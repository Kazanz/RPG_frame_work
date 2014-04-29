
from moves import *
import random

################# CHARACTER OBJECTS ###################

class characterModel(object):
	""" Basic class of a character """
	def __init__(self, name):
		self.name = str(name).upper()
		self._Life = 1
		self.HP = 100
		self._Attack = 1
		self._Defense = 1
		self._SP_a = 1
		self._SP_d = 1
		self._Luck = 1
		self.stat_names = ['Life', 'Attack', 'Defense', 'Special Attack', 'Special Defense', 'Luck']
		self._stats = [self._Life,self._Attack,self._Defense,self._SP_a,self._SP_d,
				 self._Luck]
		
	def TakeDamage(self, damage):
		self.HP -= damage
		
	def Add_Stats(self, points):
		num = 0
		while points > 0:
			print "You have %d points remaining" % points
			for stat in self.stat_names:
				print "Enter ", num+1, ' to increase ', stat, ' Total: ',self._stats[num]
				num += 1
			try:
				answer = int(raw_input())-1
			except:
				num = 0
				print "-----! Please enter a number 1-6 !-----"
			else:
				self._stats[answer] += 1
				points -= 1
				num = 0
		print "%s's stats:" % self.name
		self.HP = int(100 * self._Life)
		self.Show_Stats()
				
	def Show_Stats(self):
		num = 0
		for stat in self.stat_names:
				print self._stats[num], ': ',stat
				num += 1
				
	def Randomize_Stats(self, points):
		tot = 0
		while tot != points:
			self._stats[random.randint(0,5)] += 1
			tot += 1
	
	
class Unique_Char(characterModel):
	def __init__(self, name):
		characterModel.__init__(self, name)
		self.moves = {1:[],2:[]}
		
	def addMove(self, move): # Move needs to be a tuple. 1 = Attack 2 = SP.A
							 # The second half of the tuple needs to be a func()
		self.moves[move[0]].append(move[1])
		

### These are Tests ###
"""
Bob = Unique_Char("bobby b")
Bob.Randomize_Stats(4)
Bob.Show_Stats()

# Test adding and executing moves.
move = Move_Dict[1][0]._type, Move_Dict[1][0]

Bob.addMove(move)
print Bob.moves
"""

