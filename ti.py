n=[1,2,3,4,]  
def list (m):
    for i in m:
        yield i*i


z=list(n)
for i in z:
    pass
    #print(i)
import re 
zi="zzzzz"
com=re.compile(r'z').finditer(zi) 
for i in com:
    pass 
 #print(i)

print(5//2)   