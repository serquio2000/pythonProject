import functions

def main():
    sz = "insert a size:"
    innum = "insert a number:"
    av,mx,mn = "avg:", "max:", "min:"
    size = functions.sais(sz)
    ls_nums = functions.nums(size,innum)
    functions.avg(ls_nums,av)
    max = functions.max(ls_nums,mx)
    min = functions.min(ls_nums,mn)
    functions.asc_order(ls_nums)


if __name__ == "__main__":
    main()
