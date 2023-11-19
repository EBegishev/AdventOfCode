score = 0

with open("Day04.txt") as f:
    lines = [i.split('\n', 1)[0] for i in f.readlines()]

for line in lines:
    pair1 = line.split(',')[0]
    pair2 = line.split(',')[1]

    p1_n1 = int(pair1.split('-')[0])
    p1_n2 = int(pair1.split('-')[1])
    p2_n1 = int(pair2.split('-')[0])
    p2_n2 = int(pair2.split('-')[1])

    if p1_n1 <= p2_n1 and p1_n2 >= p2_n2:
        score += 1
    elif p2_n1 <= p1_n1 and p2_n2 >= p1_n2:
        score +=1

with open("Day04.txt", "r") as f:
    lines2 = f.read()

score2 = 0

for line in lines2.split("\n"):
    pair1_2, pair2_2 = line.split(",")
    a0, b0 = map(int, pair1_2.split('-'))
    a1, b1 = map(int, pair2_2.split('-'))
    if max(a0, a1) <= min(b0, b1):
        score2 += 1

print(score2)
print(score)
