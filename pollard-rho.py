import math
import random
import time
start=time.time()
def prime(n):#定义函数prime，目的是检验n是否为素数
    if n in{2,3,5,7,11}:#先进行一遍初筛
        return True
    if n%2==0 or n%3==0 or n%5==0 or n%7==0 or n%11==0:
        return False
    t=0
    p=n-1
    while p%2==0:#当p是偶数时，p除以二，t+1
        t=t+1
        p=p//2 
    s=5
    for i in range(s):
        a=random.randint(2,n-1) #a取2到n-1之间的一个随机数
        r=pow(a,p,n) #r=a*p%n
        if r!=n-1:
            return False
        return True

def find(n,a):
    def f(x):
        return(x*x+a)%n
    if n%2==0:
        return 2
    x1=random.randint(0,n)
    x2=x1
    while True:
        x1=f(x1)
        x2=f(f(x2))
        m=math.gcd(abs(x2-x1),n)#m等于x2-x1的绝对值与整数n的最大公因子
        if m>1 and m<n:
            return m
        if x1==x2:
            return n
num=int(input('请输入要分解的整数:'))
print(f'{num}=')
start=time.time()
prime_list=[]
while num!=1:
    if prime(num):#如果输入的整数为素数，则其素因子为它本身
        prime_list.append(num)
        break
    else: #若不是，则扔进find函数中利用pollard算法来寻找素数
        c=find(num,random.randint(0,num-1))
        if prime(c):
            prime_list.append(c)
            num//=c

prime_list.sort()
print('*'.join(map(str,prime_list)))
elasped=time.time()-start
print(elasped)
