#What is the sum of the digits of the number 2^1000?

digits = 2**1000
digits = str(digits)
listdigits = list(digits)
sum = 0

for i in range(0,len(list(digits))):
	sum = sum + int(listdigits[i])
	
print(sum)