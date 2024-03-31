given_set = {x for x in range(0,101)}


def partition(set):
    partition = []
    while len(set) != 0:
        for x in (set):
            partition.append([])
            for e in set:
                if x[0]+e[1] == x[1]+e[0]:
                    partition[len(partition)-1].append(e)
            
            for i in partition[len(partition)-1]:
                set.remove(i)
            break
        
    return partition


cartesian_power = []
for x in given_set:
    for e in given_set:
        cartesian_power.append((x,e))


quotient_set = ((partition(cartesian_power)))
classes = dict()

for x in quotient_set:
    classes[x[0][0]-x[0][1]] = x

for c in sorted(classes):
    print(f'[{c}]: {classes.get(c)}')

print(f'Total classes: {len(classes)}')
