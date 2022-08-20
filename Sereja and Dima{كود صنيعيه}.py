x=int(input())
a=0
b=0
z= list(map(int,input().split()))
for i in z:
    if len(z)==1:
        a+=z[0]
    if z[0]>=z[-1]:
        a+=z[0] 
        z.remove(z[0])   
    else: 
        a+=z[-1] 
        z.remove(z[-1]) 
    if z[0]>=z[-1]:
        b+=z[0] 
        z.remove(z[0])   
    else: 
        b+=z[-1] 
        z.remove(z[-1])
         

print(a,b ) 

            
     