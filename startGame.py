from battle import *
from characters import *
from moves import *
from makeChar import *
import time


def main(user_char,enemy_points):
	points = 0
	move_tot = 4
	cpu_char = MakeCpuChar(points, move_tot)
	points = Battle_Sequence(user_char,cpu_char)
	if points != 0:
		user_char.Add_Stats(points)
		enemy_points += 3
	

print "Welcome to KT BATTLE!"
time.sleep(1)

user_char = MakeUserChar()
enemy_points = 12

while True:
	print "Ready to Battle? yes/no"
	answer = raw_input()
	if answer == 'yes':
		main(user_char,enemy_points)
	elif answer == 'no':
		exit()
	else:
		print "note a valid entry"