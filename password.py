password = 'a123456'
i = 1
while i <= 3:
	your_password = input('請輸入你的密碼: ')
	if your_password == password:
		print('登入成功!')
		break
	else:
		print('密碼錯誤! 還有', 3 - i, '次機會')
		i = i + 1