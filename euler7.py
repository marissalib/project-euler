#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

import sys, math

num = 2
m = 1
count = 0

###################
### ISPRIME FUNCTION - Use to tell if a number is prime
################### 
def isprime(num):
	for i in xrange(2, int(math.sqrt(num))): #decrement from num to 0 to check for factors
		if num%i == 0:
			return False
	return True

	
while num>1: #Just keep looping

	if isprime(num):
		#print ("i'm prime", num)
		count = count + 1

	if count==10001:
		print ("10,001 prime is ", num)
		print("exiting")
		sys.exit()
		
		
	num = num + 1
	
	
	
