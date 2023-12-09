import hashlib
from cryptography.fernet import Fernet

cryp = hashlib.sha256();
cryp.update(b"babe")
hash = cryp.digest();
hexhash = cryp.hexdigest()
#print(hash)
print(hexhash)

cryp_with_salt = hashlib.pbkdf2_hmac("sha256", b"my_password", b"some salty salt", 100_000)
#print(cryp_with_salt.hex())

key = Fernet.generate_key()
cypher_suite = Fernet(key);
cypher_text = cypher_suite.encrypt(b"Take your eyes of this message!")
#print(cypher_text)
plain_text = cypher_suite.decrypt(cypher_text)
#print(plain_text)

new_crypt = hashlib.sha256()
new_crypt.update(b"girl")
new_hash = new_crypt.hexdigest()
print(new_hash) 



