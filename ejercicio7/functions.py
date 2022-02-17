def sais(sz):
    size = int(input(sz))
    while size < 1 or size > 50:
        size = int(input(sz))
    return size


def nums(size,innum):
    ls_nums = list()
    for i in range(size):
        num = float(input(innum))
        while num < 0 or num > 10:
            num = float(input(innum))
        ls_nums.append(num)
    return ls_nums


def avg(ls_nums,av):
    total = avg = 0.0
    for i in ls_nums:
        total = i + total
    avg = total // len(ls_nums)
    print(av,avg)


def max(ls_nums,mx):
    aux = 0
    for i in ls_nums:
        if i > aux:
            aux = i
    print(mx,aux)
    return aux


def min(ls_nums,mn):
    min = ls_nums[0]
    for i in ls_nums:
        if i <= min:
            min = i
    print(mn,min)

def asc_order(ls_nums):
    for i in range(len(ls_nums)):
        for j in range(len(ls_nums)):
            if ls_nums[i] > ls_nums[j]:
                change = ls_nums[i]
                ls_nums[i] = ls_nums[j]
                ls_nums[j] = change
    for i in ls_nums:
       print(i)
