import functions

def main():
    str1 = "number in decimal:"
    str2 = "insert a binary number: "
    binnum = functions.countDigi(str2)
    dec = functions.toDecimal(binnum)
    print(str1, dec)
if __name__ == "__main__":
    main()
