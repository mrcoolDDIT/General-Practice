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

de