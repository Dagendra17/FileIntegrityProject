import hashlib

# File open karna
file = open("test.txt", "rb")

# File ka data read karna
data = file.read()

# Hash banana
new_hash = hashlib.sha256(data).hexdigest()

# Pehle wala hash
old_hash = "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"

# Compare karna
if new_hash == old_hash:
    print("File is safe")
else:
    print("File has been modified")