
from sqlalchemy import true


def isPalindrome( x):
        
        temp = x
        reverse = 0
        while x > 0:
            reverse *= 10
            reverse += x % 10
            x //= 10
            if temp == reverse:
                return true
print(isPalindrome(121))                

