#built-in functions that take string(s)as parameter

print('John')
#input('Please enter your name: ')
type('Johh') #string--str
len('John')#return number of characters
int('1')
float('1.23')
bool('john')--False

team='New England Patriots'
letter=team[1]#Syart with 0, 1 is the second letter
print(letter)#e
print(team[0])#N
#print(team(1.0))#error--has to be integer
len(team)#20 including space, character

last=team[len(team)-1]
print(last)#s

last = team[-1]#-1:count from the last
print(last)

for letter in team:#letter is just a name
    print(letter)

prefixes='JKLMNOPQ'
suffix='ack'
for letter in prefixes:
    print(letter+suffix)

for letter in prefixes:
    if letter =='O' or letter =='Q':
        print(letter+'u'+suffix)
    else:
        print(letter+suffix)

#string slicing
team='New England Patriots'
print(team[0:11])#=print(team[:11])
print(team[12:20])#=print(team[11:])
print(team[:])
print(team[::2])#every letter but pull out every 2nd letter
print(team[::-2])#write from the back, omit one every 2 letters
print(team[::-1])#write from the back

#String is immutable=cannot change existing string
team='New England Patriots'
#team[12:20]='Seahawks'#TypeError since immutable
new_team=team[:12]+'Seahawks'
print(new_team)
print(team)

#Search
def find(word,letter):
    index=0
    while index < len(word):#while loop
        if word[index]==letter:
            return index
        index=index+1
    return -1
print(find(team,'E'))#4

#Counting/Looping
team='New England Patriots'
count=0
for letter in team:
    if letter=='a':
        count=count+1
print(count)#2

team='New England Patriots'
new_team=team.upper()#method to return values
#use Dot Notation
print(new_team)#upper letter all
another_team=team.lower()
print(another_team)#lower cases all

print(team.split())#split

s='   abc   '
print(s.strip())#remove space
