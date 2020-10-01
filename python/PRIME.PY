#Prime number

def prime(n):
    Flag=0
    if n==0 or n<0:
       While True:
          print('error')
    for i in range(2,n):
        if n%i==0:
          Flag=1
        else:
          Flag=0
     return Flag
num = int(input())
g=prime(num)
if g==0:
    print("the number is prime")
else:
    print("The number is non prime")
