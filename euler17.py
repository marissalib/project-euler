

numbers = ['zero','one', 'two','three','four','five','six','seven','eight','nine','ten','eleven','twelve',
'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']



#numbers[20] = 'twenty'
#numsize[30] = 6 #'thirty'
#numsize[40] = 5#'forty'
#numbers[50] = 'fifty'
#numbers[60] = 'sixty'
#numbers[70] = 'seventy'
#numbers[80] = 'eighty'
#numbers[90] = 'ninety'
#numbers[100] = 'one hundred'

numsize = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]


sum = 0
count = 0;

tenssize = [0,3,6,6,5,5,5,7,6,6,10,10,];
tencount = 0;


for i in range(0, 1001): #1001):

	#1 to 20
	if i<20:
		sum = numsize[i] + sum
		continue
	
	elif i%10==0:
                count=0;
		if (i>= 110) and not(i%100==0):
                        hundredName = int(str(i)[:1])
                        numsize.append(numsize[hundredName] + 7 + 3 + numsize[i%100])
                elif i%100==0:
                        if i==1000:
                                numsize.append(3+8)
                        else:
                                hundredName = int(str(i)[:1])
                                numsize.append(numsize[hundredName] + 7)
		else:
                        numsize.append(tenssize[i/10])
                        tencount = tenssize[i/10]
	
		
	if (i>20 and i<100) and not(i%10==0):
		count = 1 + count
		numsize.append(tencount+numsize[count])
	
	if (i>100 and i<1000) and not (i%10==0):
                #count = 1 + count
                hundredName = int(str(i)[:1])
                remainName = int(str(i)[1:])
                
		numsize.append(numsize[hundredName] + 7 + 3 + numsize[remainName])
	
	print(i, numsize[i])
	sum = numsize[i] + sum	
		
print(sum)
