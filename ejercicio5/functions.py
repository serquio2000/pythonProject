def validate(ins_num):
    num = int(input(ins_num))
    return num


def change(a,b,val_a,val_b):
    print(val_a,a, val_b,b)
    aux = a
    a = b
    b = aux
    print(val_a,a, val_b,b)
