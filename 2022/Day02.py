#Advent of Code; Day 2 Part 1/2
with open("Day02.txt") as txt:
    inp = txt.read()

tscore = 0
tscore2 = 0 

for a in inp.split("\n"):
    challenger, myself = a.split()
    if myself == "X": 
        if challenger == "A": 
            tscore += 3
            tscore2 += 3
        elif challenger == "B":
            tscore2 += 1
        elif challenger == "C": 
            tscore += 6
            tscore2 += 2
        tscore += 1  

    if myself == "Y":
        if challenger == "A": 
            tscore += 6
            tscore2 += 1
        elif challenger == "B":
            tscore += 3
            tscore2 += 2
        elif challenger == "C":
            tscore2 += 3
        tscore += 2
        tscore2 += 3

    if myself == "Z": 
        if challenger == "A": 
            tscore2 += 2
        elif challenger == "B":
            tscore += 6
            tscore2 += 3
        elif challenger == "C": 
            tscore += 3
            tscore2 += 1 
        tscore += 3
        tscore2 += 6

print(tscore)
print(tscore2)

