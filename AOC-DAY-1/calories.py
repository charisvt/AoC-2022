#parse magic
data = [l.strip() for l in open('input.txt')]

max_sums = []

for elf in ('\n'.join(data)).split('\n\n'):
    sum = 0
    
    for calories in elf.split('\n'):
        sum += int(calories)
    
    max_sums.append(sum)

#print(max(max_sums)) for the first part

#sort in desc order
max_sums = sorted(max_sums, reverse=True)

top_sums = 0
#get the sum of top 3
for i in range(3): 
    top_sums += max_sums[i]

#cross your finders :)
print(top_sums)