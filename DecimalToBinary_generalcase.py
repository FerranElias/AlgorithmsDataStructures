from pythonds.basic.stack import Stack

def BaseConverter(decNumber,base):
	digits = "123456789ABCDEF"
	
	remstack = Stack()
	
	while decNumber > 0:
		rem = decNumber % base
		remstack.push(rem)
		decNumber = decNumber//base
	
	newString = ""
	while not remstack.isEmpty():
		newString = newString + digits[remstack.pop()]
		
	return newString
	
print(baseConverter(25,2))
print(baseConverter(25,16))