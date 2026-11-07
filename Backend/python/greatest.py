a = int(input())
b = int(input())
c = int(input())

if(a>b and a>c):
    print("The greatest number is:",a)
if(b>c and b>a):
    print("The greatest number is:",b)
else:
    print("The greatest number is:",c)