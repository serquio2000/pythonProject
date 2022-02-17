import functions


def main():
    size = 15
    top, top_less, passed = 10, 0, 5
    in_mark = "insert a mark:"
    error = "try again !"
    av_ps = "the average of passed is:"
    av_fl = "the average of failed is:"
    cn_ps = "the students passed is:"
    cn_fl = "the students failed is:"
    marks = functions.validate(size, in_mark, error, top, top_less)
    avg = functions.avg(marks, passed,av_fl,av_ps,cn_fl,cn_ps)


if __name__ == "__main__":
    main()