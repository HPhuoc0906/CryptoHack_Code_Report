from Crypto.Util.number import inverse

s = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

pmn = max(s) + 1

for p in range(pmn, 1000):
    a = pow(s[0], p - 2) * s[1] % p
    check = True
    firstVal = a
    for i in range(0, len(s) - 1):
        a = pow(s[i], p - 2) * s[i + 1] % p
        if firstVal != a:
            check = False
            break
    if check:
        print(p, firstVal)
        break
