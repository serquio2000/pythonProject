def suma_rec(n):
    if n==1:
        return 1
    else:
         return n+ suma_rec(n-1)
print(suma_rec(4))