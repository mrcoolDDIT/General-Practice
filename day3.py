'''string operations
ankit vaghela
16ceusd021
'''
#1 string length
'''str = input("enter string")
print(len(str))
'''

#2 Number of occurance of a character
'''
def strcnt(str):
  dict={}
  for n in str:
    keys= dict.keys()
    if n in keys:
        dict[n]+=1
    else:
        dict[n] = 1
  return dict
str = input("enter string")
print(strcnt(str))
'''

#3 print first and last cahracter of string
'''
str = input("enter string")
print(str[0],str[1],str[-2],str[-1])
'''
#4 Replacing character with $
'''
def chn(str):
    chr = str[0]
    str = str.replace(chr,'$')
    str = chr + str[1:]
    return str


str = input("enter string")
print(chn(str))
'''

#5 manipulating string
'''
def modi(str1):
    if(len(str1)<3):
        return str1
    elif (str1[-3]=='i'and str1[-2]=='n' and str1[-1]=='g'):
        str1 = str1[0:-2] + 'l' + 'y'
        return str1
    else:
        str1 = str1 +'i'+'n'+'g'
        return str1

str1 = input("enter string")
print(modi(str1))
'''

#6 possible coins to make 21

def calcon(cn1,cn5):
    tot = 0
    cnt1 = 0
    cnt5 = 0
    while(tot!=26):
      if(cn5!=0):
         if():
           tot=tot+5
           cnt5+=1
           cn5-=1
      else:
          print("none")





cn1 = int(input("enter no of coins of 1"))
cn5 = int(input("enter no of coins of 5"))
