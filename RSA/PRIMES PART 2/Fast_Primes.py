from factordb.factordb import FactorDB
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, inverse

f = open(r'C:\Users\DELL\Downloads\key_17a08b7040db46308f8b9a19894f9f95.pem', "r")
code = f.read()
key = RSA.import_key(code)
n = key.n
f.close()
f = FactorDB(n)
f.connect()
sto = f.get_factor_from_api()
e = 0x10001
p, q = int(sto[0][0]), int(sto[1][0])
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)
ahihi = long_to_bytes(int("249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28", 16))
res = cipher.decrypt(ahihi)
print(res)