from moves import *
from characters import *
from makeChar import *
import time

def getUserMove(user_char):
	choice_made = False
	while not choice_made:
		print "YOUR MOVE:\n1 for Attack -- 2 for Special Attack"
		try:
			answer = int(raw_input())
			move_list = user_char.moves[answer]
		except:	
			print "Not a valid selection"
			pass
		else:
			num = 1
			for entry in move_list:
				print "Enter ", num, ' to do ', entry.name
				num += 1
			try:
				answer2 = int(raw_input())-1
				move = move_list[answer2]
			except:
				print 'INVALID ENTRY'
				pass
			else:
				return move
				choice_made = True
				
				
def getCpuMove(cpu_char):
	choice_made = False
	print "COMPUTERS MOVE"
	print"...thinking..."
	time.sleep(1)
	while not choice_made:
		try:
			answer = int(random.randint(1,2))
			move_list = cpu_char.moves[answer]
			length = len(move_list)-1
			answer_two = int(random.randint(0,length))
			move = move_list[answer_two]
		except:
			pass
		else:
			return move
			choice_made = True
				
				
def execute_move(damage,type,defender):
	defender.TakeDamage(damage)
	print "%r Damage!" % damage
	print "%s has %d HP remaining" % (defender.name,defender.HP)
	if defender.HP <= 0:
		print "%s is DEAD!" % defender.name
		return True, defender.name
	else:
		return False
		
		
		
def Battle_Sequence(user_char, cpu_char):
	""" This starts the main battle sequence starting with the computer """
	is_dead = False
	who = 0
	while not is_dead:
		damage2,type2 = getCpuMove(cpu_char).Do_Damage(cpu_char._Attack,cpu_char._Defense,
													   cpu_char._SP_a,cpu_char._SP_d,
													   cpu_char._Luck, cpu_char._Life)
		is_dead = execute_move(damage2, type2, user_char)
		who += 1
		
		damage,type = getUserMove(user_char).Do_Damage(user_char._Attack,user_char._Defense,
													   user_char._SP_a,user_char._SP_d,
													   user_char._Luck, user_char._Life)
		is_dead = execute_move(damage, type, cpu_char)
		who -= 1
		
	if who == 0:
		return 0
	elif who == 1:
		return 2
					
### THESE ARE TESTS ###
"""
user = MakeCpuChar(7,4)
cpu = MakeCpuChar(7,4)


Battle_Sequence(user, cpu)
"""


