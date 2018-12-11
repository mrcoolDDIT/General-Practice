def calc(adult,children):
     adlt = float(37550.0*adult)
     chld = float(37550.0)*1/3
     ttlch = adlt + chld
     tax= float(ttlch*3)/100
     ttlch = ttlch + tax

     print("Total charge:",ttlch)

adult = float(input("enter no of adult"))
children = float(input("enter no of children"))
calc(adult,children)