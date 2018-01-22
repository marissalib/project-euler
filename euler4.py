#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2 digit nums is 9009 = 91 * 99
#Find the largest palindrome made from the product of two 3-digit numbers.

prods = []

def ifpalin(strnum):
	for x in range(0, len(strnum)/2):

		if strnum[x] != strnum[len(strnum)-1-x]:
			return False
	return True


for i in range(100,1000):

	for j in range(i,1000): #start at i so you don't double count

		num = i * j
		strnum = str(num)
	
		
		if ifpalin(strnum):
			prods.append(num)
		

print ("Max:", max(prods))


