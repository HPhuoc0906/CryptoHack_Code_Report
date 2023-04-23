from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

def ahehe(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))
def getFlag(shared_secret: int, iv: str, ciphertext: str):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if ahehe(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')
p = int(0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff)
g = 2
A = int(0x38a3dfda6a853eccb6c0fa0dec361b26415f63e87096bfe08441258356363c913b6f095afffc49b44b9072a1b9ab2c6433a3cdf3a5c2c2151d0a683689a499772665d995762c516399133d5ce6cd9604fcf442f6b3bdba318def51ad3f00b0771f7ad7f681402e30f91a32c81be8e3645e9ddd9322482c06ee7cb5c87a2db3aba690aaa61875eb2ac6d1e1bb4cfa942b8d87c86ddfa5b8097af933257d88ac3c7563b8d1379d67691a36522d2c059beebf2bd5fb1f9fd79e266476f0262b3c64)
B = int(0x44de41eae9c0a007337696c1cf5602217f19bf09d85f72f78a31fdbe9b508b7e57850f49160ea610f295e910995827115740c91c3bbd7ccd8d1c6f3385b247e39e42fa702ee43b759154545fde532a6db7bfaa4d50b313fb54eaff76547e52a51d24bf16ef58d5c2f596d6506cb3a7be8d2cee7db7e8604fad90697303bc80d8919fc2bc67bb904423c487eb52565ad59b1cccc2a33c12ef5a0143dc6889eb08ffdd4f6a0bf725d5584617446b58fb31e5bdf5108778c36cdc5ee73f009f1414)

a = (A // 2) % p
shared_secret = B * a % p
o = "7a685f2f42e3fe2134f1cd8e6472e29f"
ciphertext = '96d11856762edc2abd4e44930f1994bb0bdec67672b4f9d6ec9c62ab4d32470897fb9784529d8535f7f59ab8621e16f3'
print(getFlag(shared_secret, o, ciphertext))