#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0

# Iterate from 1 to 1000
for i in range(1,1000):
	
	# If divisible by 3 or divisible by 5
	if i%3 == 0 or i%5 ==0:
		sum = sum + i
		print(i)
print (sum)