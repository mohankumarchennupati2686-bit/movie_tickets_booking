def Palindrome_or_Not():
    n=int(input())
    temp=n
    res=0
    while n>0:
        d=n%10
        res=res*10+d
        n=n//10
    if temp==res:
        print("Palindrome")
    else:
        print("Not Palindrome")


def prime_number_or_not():
    n=int(input())                      #3
    tem=1                                
    res=0
    while tem<=n:                       #1<=3       #2<=3       #3<=3
        if (n%tem)==0:                  #3%1==0(t)  #3%2==0(F)  #3%3==0(t)
            res+=1                      #res=1      #           #res=2
        tem+=1                          #tem=2      #tem=3      #tem=4
    if res==2:                          #2==0(t)
        print("prime number")           #prime number
    else:
        print("Not a prime number")
    prime_number_or_not()
def perfect_number_or_not():
    n=int(input())
    tem=1                                
    res=0
    while tem<n:                       
        if (n%tem)==0:                  
            res=res+tem
        tem+=1
    if sub==n:                          
        print("perfect")           
    else:
        print("Not a perfect")
    perfect_number_or_not()

def perfect_number_or_not_using_for_loop():
    n=int(input())
    res=0
    for i in range(1,n):                       
        if (n%i)==0:                  
            res=res+i
    if res==n:                          
        print("perfect")           
    else:
        print("Not a perfect")
       
    perfect_number_or_not_using_for_loop()

def fibonacci_series():
    n=int(input())
    i=1
    f=0
    s=1
    while i<=n:
        print(f,end=" ")
        f,s=s+f,f
        i+=1
    fibonacci_series()
def fibonacci_series_using_for_loop():
    n=int(input())
    f=0
    s=1
    for i in range(n):
        print(f,end=" ")
        #f=s+f
        #s=f(or)
        f,s=s+f,f
        i+=1
    fibonacci_series_using_for_loop()
def enven_and_odd_numbers_in_a_6dits():
    n=int(input())
    f=0
    s=0
    while n>0:
        d=n%10
        if d%2==0:
            f+=1
        else:
            s+=1
        n=n//10
    print(f"even numbers={f},odd numbers={s}")
    enven_and_odd_numbers_in_a_6dits()
def enven_and_odd_numbers_in_a_6dits_using_for():
    n=int(input())
    sri=str(n)
    f=0
    s=0
    #for i in range(len(sri)):
    for i in sri:
        d=n%10
        if d%2==0:
            f+=1
        else:
            s+=1
        n=n//10
    print(f"even numbers={f},odd numbers={s}")
enven_and_odd_numbers_in_a_6dits_using_for()
