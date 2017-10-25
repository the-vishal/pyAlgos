#minimum of a is appended to b, i.e. selected and sepated to right hand side
a = [9,8,5,6,7,4,3,2,1,0]
'''b= []
for i in range(0,len(a)):
    b.append(min(a))
    a.remove(min(a))
print(b)'''
#but it is not an In- place algorithm bcz it requires extra memory i.e b
#then what we do now is just swap the position of minimum with elements if left
#starting from position 1,2,3..... and so on.
for i in range(0,len(a)):
   a[a.index(min(a[i:len(a)]))],a[i]=a[i],a[a.index(min(a[i:len(a)]))]
   print(a)