
################# MOVES OBJECTS ################## 

MoveList = [] # This list holds all of the games moves
Move_Dict = {1:[],2:[]}


class MoveTemplate(object):
	def __init__(self):
		self.damage = 0
		
	def _execute(self, move):
		pass
		
		
class Move(object):
	""" Basic building block of a move """
	def __init__(self):
		self._damage = 0
		self._multiplier = 1
	
	def Do_Damage(self, s1=1, s2=1, s3=1, s4=1, s5=1, s6=1):
		""" s1 = attack, s2 = defense, spA, spD, Luck, HP """
		self._multiplier = self._func1(s1,s2,s3,s4,s5,s6)
		self._damage = self._func2(self._multiplier)
		damage = self._damage
		return damage, self._type 
		
		
		
#-------- UNIQUE MOVES ---------#
#-- Type 1 moves --#

class Punch(Move):
	def __init__(self):
		self.name = 'Punch'
		self._damage = 0
		self._func1 = ''
		self._func2 = ''
		self._type = 1 #1 for reg 2 for SP
		self.initFunc()
		
	def initFunc(self):
		self._func1 = lambda s1,s2,s3,s4,s5,s6: (s1 - ((1/s6)*s1))
		self._func2 = lambda mult: 20 + (20 * mult)

class Kick(Move):
	def __init__(self):
		self.name = 'Kick'
		self._damage = 0
		self._func1 = ''
		self._func2 = ''
		self._type = 1 #1 for reg 2 for SP
		self.initFunc()
		
	def initFunc(self):
		self._func1 = lambda s1,s2,s3,s4,s5,s6: (s2/4 + s1/2)
		self._func2 = lambda mult: 10 + (15 * mult)

#-- Type 2 moves --#
class Fireball(Move):
	def __init__(self):
		self.name = 'Fireball'
		self._damage = 0
		self._func1 = ''
		self._func2 = ''
		self._type = 2 #1 for reg 2 for SP
		self.initFunc()
		
	def initFunc(self):
		self._func1 = lambda s1,s2,s3,s4,s5,s6: (s3 - ((1/s6/2)*s3))
		self._func2 = lambda mult: 50 + (1 * mult)
		
class HaitianVoodoo(Move):
	def __init__(self):
		self.name = 'Haitian Voodoo'
		self._damage = 0
		self._func1 = ''
		self._func2 = ''
		self._type = 2 #1 for reg 2 for SP
		self.initFunc()
		
	def initFunc(self):
		self._func1 = lambda s1,s2,s3,s4,s5,s6: (s6 -(1/(s3/s4)*s6) + s2/10)
		self._func2 = lambda mult: 5 + (30 * mult)
		

#ADDS FILES TO DICT
Punch = Punch()
Kick = Kick()
HaitianVoodoo = HaitianVoodoo()
Fireball = Fireball()
Move_Dict[Punch._type].append(Punch)
Move_Dict[Kick._type].append(Kick)
Move_Dict[HaitianVoodoo._type].append(HaitianVoodoo)
Move_Dict[Fireball._type].append(Fireball)
	
"""
#### THESE ARE TESTS ####
print "Test That Dict works and does damage"
print Move_Dict
print Move_Dict[1][0].Do_Damage()
print "*" * 20
"""





