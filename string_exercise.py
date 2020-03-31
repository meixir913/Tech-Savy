#EXERCISE 5
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
print(any_lowercase1('sTr'))#-True
#If the FIRST letter is a lower case, return True, otherwise-False

def any_lowercase2(s):
    for c in s:
        if'c'.islower():
            return'True'
        else:
            return'False'
#-True
#If 'c' is a lower case, return True, otherwise-False

def any_lowercase3(s):
    for c in s:
        flag=c.islower()
    return flag
print(any_lowercase3('StaR'))#-False
#If the LAST letter of s is a lower case, return True, otherwise-False

def any_lowercase4(s):
    flag=False
    for c in s:
        flag==flag or c.islower()
    return flag
print(any_lowercase4('S'))
#Works find, but return False unless changing to True

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
print(any_lowercase5('star'))#-True
#If ALL letters are lower case, return True, otherwise-False

#EXERCISE 6
#METHOD 1
#encrypted_msg="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#encrypted_msg='map'
encrypted_msg='KCGVG'
original_msg=""
for letter in encrypted_msg:
    if letter.isalpha():
        decrypted_letter=chr(ord(letter)+2)
    else:
        decrypted_letter=letter
    original_msg+=decrypted_letter
print(original_msg)#Return MEIXI

#METHOD 2
import string
def rotate_letter(letter,amount):
    if letter.isupper():
        start=ord('A')
    elif letter.islower():
        start=ord('a')
    else:
        return letter
    distance=ord(letter)-start
    new_distance=(distance+amount)%26+start
    return chr(new_distance)
def rotate_word(word,amount):
    rotate=""
    for i in word:
        l=rotate_letter(i,amount)
        rotate=rotate+l
    return rotate
print(rotate_letter('J',3))#Return M
print(rotate_word('Kcgvg',2))#Return Meixi