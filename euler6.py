#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_squares (max):
	sum = 0
	for i in range(1,max+1):
		sum = i*i + sum
		
	return sum

def square_sum (max):
	sum = 0
	for i in range(1,max+1):
		sum = i + sum
	return sum*sum
	
print(sum_squares(100))
print(square_sum(100))
print("diff ", sum_squares(100) - square_sum(100))

