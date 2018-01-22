#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#Can't use range or xrange because the num is too high, causes overflow error
#Trick was using prime factorization

num = 600851475143	
n = 2 #start at 2

while (n <= num): #Loop through all nums from 2 to end
	
	#Find the first factor
	#one you find it, start the factorization
	#divide NUM by the 1st factor and keep finding next factors
	while (num%n == 0 ): #if the num is a factor
		print (n)
		num = num / n #use prime factorization
	n = n+1
