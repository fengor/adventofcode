input = 289326
value = 1
x,y = 0, 0
ring = 0
fields = [[ 0 for x in range(1000)] for y in range(1000)]

fields[x][y] = 1

def calcNextField(x,y, ring):
    if x == ring and y == -ring:
        ring += 1
        return x+1, y,ring
    if x== ring and y == ring:
        return x-1, y,ring
    if x == -ring and y == -ring:
        return x+1, y,ring
    if x == -ring and y == ring:
        return x, y-1,ring
    if x == ring and y < ring:
        return x, y+1,ring
    if x > -ring and y == ring:
        return x-1, y, ring
    if x == -ring and y > -ring:
        return x, y-1,ring
    if x < ring and y == -ring:
        return x+1, y, ring

def calcSum(x,y):
    x = int(x)
    y = int(y)
    value = fields[x-1][y+1] + fields[x][y+1] + fields[x+1][y+1] 
    value += fields[x-1][y] + fields[x+1][y]
    value += fields[x-1][y-1] + fields[x][y-1] + fields[x+1][y-1]
    return value

while value < input:
    x, y, ring = calcNextField(x,y,ring)
    value =  calcSum(x,y)
    fields[x][y] = value

print( value)
