a=int(input("number of rolls and columes:"))
'''for i in range(1,a+1):
    for s in range((a+1)-i):
        print(" ",end=" ")
    for j in range((i*2)-1):        
        print("*",end=" ")
    print()'''


'''a=int(input())
for i in range(1,a+1):
    for s in range((a*2)-i):
        print("*",end=" ")
    for j in range((i*2)-1):        
        print(" ",end=" ")
    print()'''



'''a=int(input())
for i in range(a,0,-1):
    for s in range((a+1)-i):
        print(" ",end=" ")
    for j in range((i*2)-1):        
        print("*",end=" ")
    print()'''



'''n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"i"*(2*i-1))
for j in range(n-1,0,-1):
    print(" "*(n-j)+"i"*(2*j-1))'''


'''a=int(input("number of roes and columes:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    for k in range(2*(n-i)):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()'''


'''for i in range(1,n+1):
    print("*"*i+' '*2*(n-i)+'*'*i)
for j in range(n-1,0,-1):
    print("*"*j+' '*2*(n-j)+'*'*j)'''


'''for i in range(1,a+1):
    for j in range(1,a+1):
        print(i,end=" ")
    print(i)'''


'''for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''


'''for i in range(a):
    for s in range(a-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(j,end=" ")
    print()'''

'''for i in range(a,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print() '''

for i in range(1,a+1):
    if i==5:
        continue
    print(i)
else:
    print("loop completed")
    
