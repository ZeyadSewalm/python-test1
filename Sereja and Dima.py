ln = int(input())
crds = list(map(int, input().split(" ")))
s = 0
d = 0
trn = 1
while len(crds)>0:
    if crds[0]>crds[-1]:
        mx = crds[0]
        del crds[0]
    else:
        mx = crds[-1]
        del crds[-1]
    if trn%2!=0:
        s += mx
    else:
        d += mx
    trn += 1
print(s, d)    