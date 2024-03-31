values = int(input('n of values: '))
sequence = list()

for x in range(0, values):
    sequence.append(1) if len(sequence) < 2 else sequence.append(sequence[x - 1] + sequence[x - 2])
    print(sequence, x)
