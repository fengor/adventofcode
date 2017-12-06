with open("d2_input.txt") as f:
	presents = f.readlines()

sqf = 0
	
for present in presents:
	l, w, h = present.split('x')
	l = int(l)
	w = int(w)
	h = int(h)
	
	side1 = l*w
	side2 = w*h
	side3 = h*l

	sqf += 2*side1 + 2*side2 + 2*side3 + min(side1,side2,side3)

print(sqf)