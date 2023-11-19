#Advent of Code; Day 6
with open('Day06.txt') as txt:
    inp = [e.split('\n')[0] for e in txt.readline()]

Puzzle1 = 0
for a, dummyvariable in enumerate(inp):
    if a > len(inp) - 5:
        break
    sub = inp[a:a+4]
    unique = len(set(sub)) == len(sub)
    if unique:
        Puzzle1 = a+4
        break
    
#print(unique) #debugging

Puzzle2 = 0
for a, dummyvariable in enumerate(inp):
    if a > len(inp) - 15:
        break
    sub = inp[a:a+14]
    unique = len(set(sub)) == len(sub)
    if unique:
        Puzzle2 = a+14
        break

print(Puzzle1)
print(Puzzle2)
