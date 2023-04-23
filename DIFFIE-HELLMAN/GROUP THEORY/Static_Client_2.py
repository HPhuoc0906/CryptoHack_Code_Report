from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from sympy.ntheory.residue_ntheory import discrete_log
import gmpy2
from Crypto.Util.number import *

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))

def find_smooth(p):
    i = 2
    k_smooth = 1
    while k_smooth < p or not isPrime(k_smooth + 1):
        k_smooth *= i
        i += 1
    k_smooth += 1
    return k_smooth

def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii') 

def find_smooth(p):
    i = 2
    k_smooth = 1
    while k_smooth < p or not isPrime(k_smooth + 1):
        k_smooth *= i
        i += 1
    return k_smooth + 1

p = int(0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff)
A = int(0xf77ad1bd4efac24eb273eb432f53df926417d7f2e358c2f96d0638e1b27579a1ec0c74be9b43f22e2d2180d8b38491da1c42d84a7026a200e769ca58de4a989ed838133797d3d61bdb47f9a437676b0a06ae27e6aa9ac4c0a2720b7613e8c2710b14fe226a3dddad574cef6e9b47a8880d7ed9a471513d155154967ea4e90760d8976351e363b381ea1b5dcb1fbea42e46539c865da47d3d4b664c9cbb2ea4fc25f1c881a95e9fe396374c3e6caed3e76aa08a40ae511585a28653af390baa3a)
B = int(0x56c2f62b18614911dfca2942d1c5f60d84f2d95dde472190424658940f9fd7aeb5af05432b2e4db94feb69040a7d7d39700463f4e1c98903edc7740e2f72eb7beea78206c0a1cc80c7adc5de2a1599e5cfcc183a790d8ee4cb009627899341298722cc2fb9c30f7ce78fad0ed743fa227341d4085335504a26febca986e25bb8fab55d0b3396e49d4db63a52ac33f0a31b6d8a55e7902dce7b8ee66a3d338a2d62d647297adcc7fd1007bb1be74db7c7af9d6374db3f3950dad7895c2244ff40e2d1ae577740ef672b0c29d97a8175dc34a8e2a014a8e279fed464fbbd9e79109ec2aba2cefddfedfc092c0dd48e8d276da5e3b04959bf8829bc8187215cc6cc063842bc3ac69d5b62eddfc00f1fe2678c65656d)
g = 2

b = discrete_log(find_smooth(p), B, g)
shared_secret = pow(A, b, p)
iv = "1632aea70ef65503acdd459cf9a85547"
ciphertext = '618bc7168fb1212a86aea0101765528c7e6383487a500c1e43a20a3f4230dbb0f3d2b3aaab117f8a8bba8af092a92ef0'

print(decrypt_flag(shared_secret, iv, ciphertext))