import hashlib
h=hashlib.md5()
s=input("enter the string:")
print("the given string is:",s)
encoded_out=s.encode()
for i in s:
   h.update(encoded_out) #adding iterations
h.update(b"thee salting output") #adding salting
msg=h.hexdigest()
print(msg)
