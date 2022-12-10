data = [l.strip() for l in open('input.txt')]

#garbage code ahead - dont mind this 
#map X->A, Y->B, Z->C
for count in range(len(data)):
    data[count] = data[count].replace('X', 'A')
    data[count] = data[count].replace('Y', 'B')
    data[count] = data[count].replace('Z', 'C')

#restructure the data
new_data = []
for s in data:
    new_data.append(s.split())

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
    score += 1 if s=='A' else 2 if s=='B' else 3
    score += get_score(a,s)
print(score)