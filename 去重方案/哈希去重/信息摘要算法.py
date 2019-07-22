from hashlib import md5

m=md5()
m.update(b'12345678')
print(m.hexdigest())