#compare two numbers then swap their location if greater than
#time complexity of O(n^2)
import time
tic = time.clock()
a=[9,8,7,6,5,4,3,2,1,0]

for n in range(0,len(a)-1):
    flag = 0
    for i in range(0,len(a)-1-n):
     if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
        flag = 1

    if flag ==0:
        break

    else:
        pass

print(a)
toc = time.clock()
print(toc-tic)