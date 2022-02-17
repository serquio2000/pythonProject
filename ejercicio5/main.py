import functions


def main():
    ins_num = "insert number:"
    val_a,val_b = "a:", "b:"
    a = functions.validate(ins_num)
    b = functions.validate(ins_num)
    functions.change(a,b,val_a,val_b)

if __name__ == "__main__":
    main()
