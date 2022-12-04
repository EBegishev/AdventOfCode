#Advent of Code; Day 1 Part 1/2
with open("Day01.txt") as txt:
    inp = txt.read()

def data():
    dmax = sorted(sum(int(cals) for cals in elfers.split("\n")) for elfers in inp.split("\n\n")) #OMG the debuggging on this was painful
    print(dmax[-1])
    #print(dmax) #debugging
    topelves = sum(dmax[-3:])
    print(topelves)
    
data()
