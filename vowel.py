str = input("enter string")
vow = ['a','e','i','o','u']
vow_flag = 0
for i in range(0,5):
       if vow[i] in str:
           print("vowel found", vow[i])
           vow_flag = 1

if(vow_flag == 0):
      print("vowel not found")

