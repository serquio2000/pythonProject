def validate(ins_num):
    num = int(input(ins_num))
    while num < 0:
        num = int(input(ins_num))
    return num


def ladder(num):
    suma = 0
    count = 1
    while num > suma:
        suma = suma + count
        print(count-1)
        count += 1
