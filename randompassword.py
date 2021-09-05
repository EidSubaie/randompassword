import random
def getpassword (data):
	Max = 10
	password = ""
	while len (password)!=Max:
		value = random.choice(data)
		password+=value
	return password
	
data ='@#$%&*-+()123450gbnmaq'
for i in range(20):
    print(getpassword (data))