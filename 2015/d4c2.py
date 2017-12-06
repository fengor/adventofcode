import hashlib

md5 = hashlib.md5()

secret = 'bgvyzdsv'

counter = 0
hex =  hashlib.md5(bytearray(secret+str(counter), "utf-8")).hexdigest()

while hex[0:6] != '000000': 
	counter += 1
	hex = hashlib.md5(bytearray(secret+str(counter), "utf-8")).hexdigest()
print(counter, hex)