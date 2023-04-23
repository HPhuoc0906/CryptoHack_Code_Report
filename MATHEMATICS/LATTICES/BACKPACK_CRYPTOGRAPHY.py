a = [
    #public key
]

s = #ciphertext

n = len(a)
N = ceil(sqrt(n) / 2)

b = []
for i in range(n):
    vec = [0 for _ in range(n + 1)]
    vec[i] = 1
    vec[-1] = N * a[i]
    b.append(vec)

b.append([1 / 2 for _ in range(n)] + [N * s])

BB = matrix(QQ, b)
l_sol = BB.LLL()
for e in l_sol:
    if e[-1] == 0:
        msg = 0
        isValidMsg = True
        for i in range(len(e) - 1):
            ei = 1 - (e[i] + (1 / 2))
            if ei != 1 and ei != 0:
                isValidMsg = False
                break

            msg |= int(ei) << i

        if isValidMsg:
            print('[*] Got flag:', long_to_bytes(msg))
            break
