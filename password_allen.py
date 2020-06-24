password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
	i = i - 1
	pwd = input('Enter password: ')
	if pwd == password:
		print('Welcome to log in')
		break
	else:		
		if i > 0:
			print('Wrong password! you have', i, 'chance')
		else:
			print('No more chance')
		