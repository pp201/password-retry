password = 'a123456'

chance = 2
x = 0
while x < 3:
	enter_password = input('Enter your password ')
	if enter_password != password:
		print('Wrong password, you have', chance-x, 'chance.')
		x = x + 1
	elif enter_password == password:
		print('BINGO')
		break