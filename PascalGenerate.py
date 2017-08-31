import math
def ncr(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
def pmf(x,r,p):
    return ncr(r-1+x,x)*(p**r)*((1-p)**x)
x = 60+1
print("r=10\r\n")
for i in range(x):
    print(pmf(i,10,0.5))
    print("\r\n")
print("r=20\r\n")
for i in range(x):
    print(pmf(i,20,0.5))
    print("\r\n")
print("r=30\r\n")
for i in range(x):
    print(pmf(i,30,0.5))
    print("\r\n")
