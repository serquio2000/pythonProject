def countDigi(str2):
    count = 0
    num = int(input(str2))
    aux = num
    while aux > 0:
        aux = aux / 10
        count += 1
    return num


def toDecimal(binnum):
    res, decimal, j = 0, 0, 0
    while binnum > 0:
        res = binnum % 10
        decimal += 2 ** j *res
        binnum = binnum // 10
        j += 1
    return decimal



    # for i in range(binNum):
    #     res = binNum % 10
    #     decimal += 2 ** i * res
    #     binNum = binNum / 10
    # return decimal