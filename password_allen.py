password = 'a123456'
i = 3
while True:
	pwd = input('Enter password: ')
	if pwd == password:
		print('Welcome to log in')
		break
	else:
		i = i - 1
		print('Wrong password! you have', i, 'chance')
		if i == 0:
			break