x=int(input())
ans=0

for i in range(x):
   z=list(map(int,input().split()))
   c=0 
   for i in z:
       
       if i==1:
           c=c+1
   if(c>=2):
       ans+=1
print(ans)       

       
              
              