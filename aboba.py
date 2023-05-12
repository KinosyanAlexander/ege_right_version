with open('26.txt') as f:
    n = int(next(f))
    data = list(map(lambda x: x.split(), f))
    data = list(map(lambda x: [int(x[0]), int(x[1]), x[2]], data))
data.sort()
park = {'A': [0]*70, 'B': [0]*30}

def find_place(car, park_type, park):
    for i, v in enumerate(park[park_type]):
            if v == 0:
                park[park_type][i] = car[1]
                return 1
    else:
        return 0

def parking(car, park):
    if car[-1] == 'A':
        if find_place(car, 'A', park):
            return 1
        if find_place(car, 'B', park):
            return 1
    elif car[-1] == 'B':
        if find_place(car, 'B', park):
            return 1
    return 0

def tick(time, park):
    for t in park.keys():
        for i, v in enumerate(park[t]):
            park[t][i] = max(0, v-time)
c_b = 0
loh = 0
for i, car in enumerate(data):
    if i > 0:
        tick(car[0] - data[i-1][0], park)
    kok = parking(car, park)
    if kok and car[-1] == 'B':
        c_b += 1
    if not kok:
        loh += 1

print(c_b, loh)
