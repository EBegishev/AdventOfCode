crates = [['P', 'F', 'M', 'Q','W','G','R','T'],
          ['H', 'F', 'R'],
          ['P', 'Z', 'R', 'V', 'G', 'H','S','D'],
          ['Q', 'H', 'P', 'B', 'F', 'W', 'G'],
          ['P', 'S', 'M', 'J', 'H'],
          ['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'],
          ['P', 'T', 'H', 'N', 'M', 'L'],
          ['F', 'D', 'Q', 'R'],
          ['D', 'S', 'C', 'N', 'L', 'P', 'H']]

with open('Day05_2.txt') as txt:
    sets = [e.split('\n', 1)[0] for e in txt.readlines()]

for value in sets:
    val = value.split(',')
    for letters in val:
        words = value.split()
        num = int(words[1])
        Sfrom = int(words[3])
        Sto = int(words[5])

        for i in range(num):
            s = len(crates[Sfrom-1]) - (num - i)
            item = crates[Sfrom-1][s]
            crates[Sfrom-1].pop(s)
            crates[Sto-1].append(item)

final = ''
for crate in crates:
    final += crate[-1]
print(final)
