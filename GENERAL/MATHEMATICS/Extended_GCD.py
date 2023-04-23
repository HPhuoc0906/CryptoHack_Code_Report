def extendedEuclid(a, b):
  global temp, d, x, y
  if b == 0:
    d = a
    X = 1
    y = 0
  else:
    extendedEuclid(b, a%b)
    temp = x
    x = y
    y = temp - int(a / b)
extendedEuclid(26513, 32321)
print(min(x, y))
