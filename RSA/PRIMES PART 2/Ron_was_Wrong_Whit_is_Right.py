from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from math import gcd
n=[]
c=[]
e=[]
for i in range(1, 51):
    key = RSA.importKey(open(f"{i}.pem", 'r').read())
    cipher = open(f"{i}.ciphertext", 'r').read()
    n.append(key.n)
    c.append(cipher)
    e.append(key.e)
ahihi = 0
for i in range(len(n)):
    for j in range(i,len(n)):
        uoc = gcd(n[i], n[j])
        if uoc != 1 and n[i] != n[j]:
            ahihi = uoc
            index = i
e = e[index] 
factor_1 = ahihi 
factor_2 = n[index]//ahihi 
phi = (factor_1-1)*(factor_2-1) 
d = pow(e,-1, phi) 

key = RSA.construct((n[index], e, d))
cipher = PKCS1_OAEP.new(key)
decrypt = cipher.decrypt(bytes.fromhex(c[index]))
print(decrypt)
