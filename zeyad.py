n=input()
n=int(n)
police=0
untreated=0
for i in range(n):
    x=input()
    x=int(x)
    if x>0:
      police +=x
    if x<0 and police>0:
      police-=1
    if x<0:
      untreated+=1

print(untreated)



