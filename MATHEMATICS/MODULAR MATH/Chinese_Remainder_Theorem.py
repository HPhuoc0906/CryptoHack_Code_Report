from sympy.ntheory.modular import crt
# Khai báo các đại lượng
moduli = [5, 11, 17]
remainders = [2, 3, 5]
# Giải hệ phương trình đồng dư
x, _ = crt (moduli, remainders)
# In kết quả
print(x)
