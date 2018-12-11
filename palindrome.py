def reverse(s):
     return s[::-1]

def isPalindrome(s):
    rev = reverse(s)
    print(rev)
    if (s == rev):
         return True
    return False



s = input("enter string ")
ans = isPalindrome(s)

if (ans == 1):
      print(s,"is palindrome")
else:
 print(s,"is not palindrome")