# 國家年齡考照問題
nationality = input('請輸入所在國家: ')
age = input('請輸入年齡: ')
if nationality == '台灣':
	if int(age) >= 18 :
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif nationality == '美國':
	if int(age) >= 16 :
		print('你可以考駕照')
	else:
		print('你還不譨考駕照')
else: 
	print('請輸入 台灣/美國')