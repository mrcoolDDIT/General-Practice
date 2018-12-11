import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

p =  input("enter password")
if p in s:
  print ("valid password")
else:
    print("invalid password")