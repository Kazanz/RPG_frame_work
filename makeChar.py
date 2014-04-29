from moves import *
from characters import *
import random

def MakeUserChar():
	print "Enter Name:"
	new_char = Unique_Char(raw_input())
	new_char.Add_Stats(7)
	selected = select_moves(4)
	for moves in selected:
		move = (moves._type,moves)
		new_char.addMove(move)
	return new_char
	
	
def MakeCpuChar(points, move_tot):
	new_char = Unique_Char("COMP DEFAULT")
	statlist = new_char._stats
	tot = 0
	new_char.Randomize_Stats(points)
	move_num = 0
	selected = []
	while move_num < move_tot:
		type_list = Move_Dict[random.randint(1,2)]
		selected.append(type_list[random.randint(0,len(type_list)-1)])
		move_num += 1
	for moves in selected:
		move = (moves._type,moves)
		new_char.addMove(move)
	return new_char	
	
	
def select_moves(amount):
	selected_moves_list = []
	while amount > 0:
		print "You get %d new moves." % amount
		print "Enter 1 for Attacks, enter 2 for Special Attacks"
		try:
			answer = int(raw_input())
			move_list = Move_Dict[answer]
		except:
			pass
		else:	
			num = 1
			for moves in move_list:
				print 'Enter ', num, ' for ', moves.name
				num +=1
			choice = int(raw_input())-1
			try:
				selected_moves_list.append(Move_Dict[answer][choice])
			except:
				print "-------! Not a valid choice. Try Again !-------"
			else:
				amount -= 1
			
	return selected_moves_list

			
"""		
### THESE ARE TESTS ###	
print "COMPUTER _____________________________"
cpu = MakeCpuChar(7,4)
cpu.Show_Stats()
print cpu.moves

print "USER____________________________________"
user = MakeUserChar()
user.Show_Stats()
print user.moves
"""