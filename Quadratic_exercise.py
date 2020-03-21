#Method 1 (Simplest)
import math
def quadratic(a,b,c):
    a=float(input('Enter a: '))
    b=float(input('Enter b: '))
    c=float(input('Enter c: '))

    delta=math.sqrt(b*b-4*a*c)
    r1=(-b+delta)/(2*a)
    r2=(-b-delta)/(2*a)
    
    print('The solutions are:', r1, r2)

#Method 2
import math
def quadratic(a,b,c):
    a=float(input('Enter a: '))
    b=float(input('Enter b: '))
    c=float(input('Enter c: '))

delta=b*b-4*a*c

if delta>0:
    root1=(-b+math.sqrt(delta)/(2*a))
    root2=(-b+math.sqrt(delta)/(2*a))
    print('The solutions to this equation are{} and {}'.format(root1,root2))
elif delta==0:
    root1=(-b/(2*a))
    print("Two roots are real and equal:"root1,'and'root2)
else:
    print("No real roots")
    
#Method 3 (Complexed math)
import cmath
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
delta=b*b-4*a*c
Root1=(-b-cmath.sqrt(delta)/(2*a))
Root2=(-b+cmath.sqrt(delta)/(2*a))
print('The solutions to this equation are{}and{}'.format(Root1,Root2))
