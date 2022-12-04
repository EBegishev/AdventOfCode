#Advent of Code; Day 3 Part 1/2
with open("Day03.txt") as txt:
    inp = [e.split('\n')[0] for e in txt.readlines()] 
#print(inp) #Debugging
pr = 0
pr2 = 0

for string in inp: #Part 1
    mid = len(string)//2
    sinkv1 = string[:mid] #Brick/Sink are inside jokes, for everyone whose reading this and being confused
    sinkv2 = string[mid:]
    brick = list(set(sinkv1).intersection(sinkv2))[0]

    #print(brick) #debugging
    #print(ord(brick)) #debugging
    deletus = 96 if brick.islower() else 38
    pr += ord(brick) - deletus

for i in range(0, len(inp)-1, 3): #Part 2
    elf1 = inp[i]
    elf2 = inp[i+1]
    elf3 = inp[i+2]
    #print(elf1) #Debugging
    #print(elf2) #Debugging
    #print(elf3) #Debugging
    brick2 = list(set(elf1).intersection(elf2).intersection(elf3))[0]

    deletus2 = 96 if brick2.islower() else 38
    pr2 += ord(brick2) - deletus2

#print(chr(97)) #Debugging
#print(chr(65)) #Debugging

print(pr)
print(pr2)
