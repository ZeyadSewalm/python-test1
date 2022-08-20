


from ast import Str


str="MCMXCIV"
v=0
   
for i in str:
            if i=='I':
                v+=1
            elif i=='V':
                v+=5  
            elif i=='X':
                v+=10    
            elif i=='L':
                v+=50
            elif i=='C':
                v+=100
            elif i=='D':
                v+=500
            elif i=='M':
                v+=1000  
print(v)
                         

