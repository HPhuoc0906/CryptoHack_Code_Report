from Crypto.Util.number import *
import numpy as np

h = 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800
q = 7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257
e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523


def decrypt(f, g, e):
    a = (f*e) % q
    m = (a*inverse(f, g)) % g
    return m

def gauss(u, v):
    u = np.array(u)
    v = np.array(v)
    while True:
        if u.dot(u) > v.dot(v):
            u, v = v, u
        m = u.dot(v) // u.dot(u)
        if m == 0:
            return u
        v -= m * u

# We gotta find (f, g) such that f * h == g + t * q

(f, g) = gauss((1, h), (0, q))
assert f * f < q and g * g < q and GCD(f, g) == 1

msg = decrypt(f, g, e)
print(long_to_bytes(msg).decode())
# flag : crypto{Gauss_lattice_attack!}
