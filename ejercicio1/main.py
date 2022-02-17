import functions


def main():
    attempt = 3
    in_num = "insert a num:"
    att = "try again!"
    num = functions.validate(attempt,in_num,att)
    print("the number insert by user is:",num)


if __name__ == "__main__":
    main()
