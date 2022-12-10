data = [l.strip() for l in open('input.txt')]

#restructure the data
new_data = []
for s in data:
    new_data.append(s.split())

def pick_s(a,b):
    #pick same symbol to tie
    if(b == 'Y'):
        return a
    #pick a symbol to lose
    if(b == 'X'):
        return 'A' if a == 'B' else 'B' if a == 'C' else 'C'
    #pick a symbol to win
    if(b == 'Z'):
        return 'A' if a == 'C' else 'B' if a == 'A' else 'C'

#get points according to the result
def get_score(a,b):
    if a == b :
        return 3
    if (a == 'A' and b =='B') or (a == 'B' and b == 'C') or (a == 'C' and b == 'A'):
        return 6  
    else:
        return 0

#count total score
score = 0
for a, s in new_data:
    s = pick_s(a,s)
    score += 1 if s=='A' else 2 if s=='B' else 3
    score += get_score(a,s)
print(score)