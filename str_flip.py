str = input("enter string")
shf = int(input("enter bit of shift"))

shftd = str[shf:]+str[:shf]
print(shftd)
