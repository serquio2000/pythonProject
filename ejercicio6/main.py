import functions


def main():
    ins_num = "insert a num:"
    a = functions.validate(ins_num)
    functions.ladder(int(a))

if __name__ == "__main__":
    main()
