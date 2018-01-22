#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
import time

###################
### ISPRIME FUNCTION - Use to tell if a number is prime
################### 
import math
def isprime(num):
	if num == 1:
		return False
		
	if num < 4: #2 & 3 are prime
		return True
		
	if num % 2 == 0: #evens aren't prime
		return False
		
	if num < 9: #this picks up 5, 7
		return True
	
	if num % 3 == 0:
		return False
	
	i = 5
#	while i <=int(math.sqrt(num)):
		if num%i == 0:
			return False
		if num%(i+2) == 0:
			return False
		
		i = i + 6
	return True
	
	
#	for i in xrange(2, int(math.sqrt(num))):
#		if num%i == 0:
#			return False
#	return True
start = time.time()
sum = 0	
for i in xrange(2,2000000):
	if isprime(i):
		#print("Prime: ", i)
		sum = sum + i
print (sum)
end = time.time()
print (end - start)