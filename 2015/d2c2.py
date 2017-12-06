with open("d2_input.txt") as f:
	presents = f.readlines()

ribbon = 0
	
for present in presents:
	l, w, h = present.split('x')
	l = int(l)
	w = int(w)
	h = int(h)
	
	ribbon += 2*(l+w+h-max(l,w,h))
	ribbon += l*w*h
	
print(ribbon)