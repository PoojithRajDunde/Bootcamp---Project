import hashlib
h1=hashlib.sha3_256()
h2=hashlib.sha512()
h3=hashlib.sha1()
h31=hashlib.blake2s()


s=input("enter the string:")
print("The given string is:",s)
encoded_out=s.encode()
for i in s:  #adding iterations
 h1.update(encoded_out)
h1.update(b"thee salting output") #adding salting
msg=h1.hexdigest()
print("The sha3_256 hashed value is:",msg)
for i in s:
 h2.update(encoded_out)
h2.update(b"thee salting output")
msg2=h2.hexdigest()
print("The sha512 hashed value is:",msg2)
for i in s:
 h3.update(encoded_out)
h3.update(b"thee salting output")
msg3=h3.hexdigest()
print("The sha1 hashed value is:",msg3)
h31.update(encoded_out)
msg31=h31.hexdigest()
print("The blake2s hashed value is:",msg31)
