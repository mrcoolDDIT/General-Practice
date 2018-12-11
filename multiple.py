num = []
for i in range(int(input("enter starting range")),int(input("enter ending point"))):
    if(i%7==0) or (i%5!=0):
        num.append(str(i))

print(num)