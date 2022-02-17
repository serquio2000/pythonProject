import functions

def main():
    innum = "insert number:"
    pw = "the result of pow is:"
    x = functions.validate(innum)
    y = functions.validate(innum)
    result = functions.pow(x,y)
    print(pw,result)
if __name__ == "__main__":
    main()
