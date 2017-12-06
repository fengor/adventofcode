import hashlib

md5 = hashlib.md5()

secret = 'bgvyzdsv'

counter = 0
hex =  hashlib.md5(bytearray(secret+str(counter), "utf-8")).hexdigest()

while hex[0:5] != '00000': 
	counter += 1
	hex = hashlib.md5(bytearray(secret+str(counter), "utf-8")).hexdigest()
print(counter, hex)