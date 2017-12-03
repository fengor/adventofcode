from math import sqrt 


input = 289326
#input= 25
x, y = 0, 0
value = 1
counter = 1

while value < input:
    counter += 2
    value = counter ** 2
    x, y = x+1, y-1 

counter -= 2
value = counter ** 2
x, y = x-1, y+1
counter = x

while value < input:
    print(value, x, y, counter)
    value += 1
    if x == counter and y == -counter:
        x += 1
        counter += 1
        continue
    if x == counter and y < counter:
        y += 1
        continue
    if x > -counter and y == counter:
        x -= 1
        continue
    if x == -counter and y > -counter:
        y -= 1
        continue

print(value, x, y, counter)
print(abs(x), abs(y), abs(x)+abs(y))
