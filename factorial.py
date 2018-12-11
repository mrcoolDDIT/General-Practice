num =  int(input("enter number "))
factorial=1
if (num<0):
    print("factorial does not exits")
elif(num == 0):
    print("factor of 0 is 1")
else:
  for i in range(1,num+1):
    factorial=factorial*i

print("factor of",num,"is",factorial)