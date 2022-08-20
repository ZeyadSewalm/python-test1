x=int(input())
reverse = 0
t=x
while x > 0:
  reverse *= 10
  reverse += x % 10
  x //= 10
if t== reverse:
      print('true')
else:
      print('false')    