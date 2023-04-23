import telnetlib
import json
from pwn import * # pip install pwntools
import json
import base64
from Crypto.Util.number import *
import codecs
from binascii import unhexlify

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

for i in range(0, 101):
    received = json_recv()
    if "flag" in received:
        print(received["flag"])
        break
    code = received["encoded"]
    t = received["type"]
    
    res = None
    if t == "flag":
        print(code)
        break
    if t == "base64":
        res = base64.b64decode(code).decode('utf8')
    elif t == "hex":
        res = (unhexlify(code)).decode('utf8')
    elif t == "rot13":
        res = codecs.decode(code, 'rot_13')
    elif t == "bigint":
        res = unhexlify(code.replace("0x", "")).decode('utf8')
    elif t == "utf-8":
        res = ""
        for c in code:
            res += chr(c)
    print("code : ", res)
    to_send = {
        "decoded": res
    }
    json_send(to_send)
