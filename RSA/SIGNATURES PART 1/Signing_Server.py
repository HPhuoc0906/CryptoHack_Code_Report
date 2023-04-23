from pwn import *
import json


# We have access to both sign and get_secret...use both to get the flag


r = remote("socket.cryptohack.org", 13374)
r.recvline()
r.sendline(json.dumps({"option": "get_secret"}))
secret = json.loads(r.recvline())["secret"] # Grab secret
r.sendline(json.dumps({"option": "sign", "msg": secret})) # Send secret to be signed
print(bytes.fromhex(json.loads(r.recvline())["signature"][2:])) # and get flag
