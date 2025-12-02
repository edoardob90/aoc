import hashlib

def hash(s):
    return hashlib.md5(s.encode()).hexdigest()

seed = "ckczppom"

i = 1

while True:
    if hash(seed + str(i)).startswith("000000"):
        print(i)
        break
    i += 1
