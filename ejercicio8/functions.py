def validate(innum):
    num = int(input(innum))
    return num


def pow(x, y):
    result = 0
    for i in range(y - 1):
        result = x * x
    return result