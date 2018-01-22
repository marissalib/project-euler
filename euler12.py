#What is the value of the first triangle number to have over five hundred divisors?

import math
i = 1
while i>0:
	tri_num = 0
	
	for num in range(1,i):
		tri_num = tri_num + num
	i = i + 1
	#print(tri_num)
	
	factors_count = 0
	factors = {}
	
	for j in xrange(1,int(math.sqrt(tri_num))+1):
		if tri_num % j == 0:
			factors_count = factors_count + 1
			#print("     ",j)
	factors_count = factors_count * 2;	#multiply by 2 because using the sqrt to find the factors only results in half the factors
	#print(factors_count)
			
	if factors_count > 300:
		print("I made it to 300", tri_num)
	if factors_count > 400:
		print("I made it to 300", tri_num)
		
	if factors_count > 500:
		i = 0
		print ("DONE", tri_num, factors_count)