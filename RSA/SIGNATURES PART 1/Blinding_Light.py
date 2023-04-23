from pwn import remote
from Crypto.Util.number import bytes_to_long, long_to_bytes
import json




r = remote("socket.cryptohack.org", 13376)
r.recvline()


r.sendline(json.dumps({"option": "get_pubkey"}))
pub_key = json.loads(r.recvline())
N = int(pub_key['N'], 16); e = int(pub_key['e'], 16)


# Note that we can factor our goal plaintext
p, q = 211578328037, 2173767566209
assert bytes_to_long(b"admin=True") == p*q


# We have
# M = sign(p) * sign(q) = p^d * q^d = C^d
# => M^e = (C^d)^e = C
r.sendline(json.dumps({"option": "sign", "msg": long_to_bytes(p).hex()}))
sign_p = int(json.loads(r.recvline())['signature'], 16)


r.sendline(json.dumps({"option": "sign", "msg": long_to_bytes(q).hex()}))
sign_q = int(json.loads(r.recvline())['signature'], 16)
assert long_to_bytes(pow( (sign_p * sign_q) % N, e, N)) == b"admin=True"


r.sendline(json.dumps({"option": "verify", "msg": b"admin=True".hex(), "signature": hex((sign_p * sign_q) % N)[2:]}))
print(json.loads(r.recvline())["response"])
