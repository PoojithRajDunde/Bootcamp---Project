import hashlib
n1= hashlib.sha3_256()
s=input("enter text:")
e=s.encode()

for i in s:
    n1.update(e) #adding iteration
n1.update(b"thee salting output") #adding salting
m=n1.hexdigest()
print(m)
