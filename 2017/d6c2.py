import operator

banks = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]
#banks = [0,2,7,0]
seen = set()
counter = 0

while '-'.join(str(banks)) not in seen:
    index, value = max(enumerate(banks), key=operator.itemgetter(1))
    seen.add('-'.join(str(banks)))

    banks[index] = 0
    for i in range(value):
        banks[(i+1+index)%len(banks)] += 1

    counter += 1

target = '-'.join(str(banks))
print(counter)

counter = 0 
index, value = max(enumerate(banks), key=operator.itemgetter(1))
seen.add('-'.join(str(banks)))

banks[index] = 0
for i in range(value):
    banks[(i+1+index)%len(banks)] += 1

counter += 1


while '-'.join(str(banks)) != target:
    index, value = max(enumerate(banks), key=operator.itemgetter(1))
    seen.add('-'.join(str(banks)))

    banks[index] = 0
    for i in range(value):
        banks[(i+1+index)%len(banks)] += 1

    counter += 1
print(counter)
