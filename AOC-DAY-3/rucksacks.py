import string

#really unpolished code here

data = [l.strip() for l in open('input.txt')]

def score(v):
    return ord(v) - 96 if v.islower() else ord(v) - 38

sum = 0
for l in data:
    h = l[:len(l)//2]
    f = l[len(l)//2:]
    for u in h:
        flag = False
        for v in f:
            if u == v:
                sum += score(v)
                flag = True
                break
        if flag:
            break
print(sum)