limit = int(input("enter limit"))
for i in range(1,limit+1):
     if(i%3==0 and i%5==0):
         print("bizfiz")
     elif(i%3==0):
         print("biz")
     elif(i%5==0):
          print("fiz")

     else:
         print(i)