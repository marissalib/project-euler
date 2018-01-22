#Which starting number, under one million, produces the longest chain?
#Longest COllatz sequence

longest = 0
longest_num = 0

for i in range(13,1000000):

	num = i
	sum = 0
	while i>1:
	
		if i%2==0:
			i = i/2
		else:
			i = (3*i)+1
		 
		sum = sum + 1 
		if sum > longest:
			longest = sum
			longest_num = num
			
		#print i

print ("lognest", longest_num, longest)