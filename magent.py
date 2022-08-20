x=int(input())
m=[]
g=1
for i in range(x):
    m.append(input())
    
for i in range(1,x):
    
       if m[i] != m[i-1]:
        g =g+1
      
             
print(g)  

    
