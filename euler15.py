## Find number of paths through a 20x20 grid, only moving right and down

import time

def calcGrid(num):
    if num==1:
        return 2
    else:
        return (calcGrid(num-1)/num)*(num*(num-(num-5))-(num+2));


tic = time.clock()
count = calcGrid(20)
toc = time.clock();

print("Run time: ",toc-tic)
print("Answer", count);
    
