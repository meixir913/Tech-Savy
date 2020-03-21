# a named sequence of statements tat performs a computation
A=area_of_circle(x)

#FUNCTION CALLS
type(42) #name of the function=type, 42=arguments, results=return value
type('42')
int('42')
int('Hello')#ValueError
int(3.99)
int(-2.3)
float(42)
float('3.14')
str(42)
str(3.14)
abs(-100)
abs(-100, 42)#TypeError--one argument
max(1,2)
max(42,5345,-654,2,0,99999)

#MATH FUNCTIONS
import math
math
    ratio=100
    math.log10(ratio)
    degrees=45
    radians=degrees/180*math.pi #math=constant
    math.sin(radians)

def print_lyrics():
    print("Hey, Jude...")
    type(print_lyrics)
    print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print('hhhhh')
    print_lyrics()
repeat_lyrics()

#PARAMETERS AND ARGUMENTS
def print_twice(whatever_name):
    print(whatever_name)
    print(whatever_name)
print_twice('USC')
my_name='Macy'
print_twice(my_name)

#LOCAL VARIABLES AND PARAMETERS
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
line1='1112'
line2='2223'
cat_twice(line1,line2)
print(cat)#NameError destroyed

#RETURN VALUES
def give_me_a_break():
    str1="break"
    return str1
print(give_me_a_break)
def give_me_a_break():
    str1="break"
    return str1
    print('another break')
print(give_me_a_break)

#VOID FUNCTIONS (NO RETURN VALUE)
result=print_twice('Bing')
print(result)#Special Value "None"

#EMPTY FUNCTION
def nop():
    pass
age= int(input()) ##############?
if age >= 18:
    pass

import math
def move(x,y,step,angle):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)
