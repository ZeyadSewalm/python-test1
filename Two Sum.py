z=list(map(int,input().split(',')))
t=int(input())
for i in range(0,(len(z))):
       if z[i-1]+z[i]==t:
           print(i-1,i)

