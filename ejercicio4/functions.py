def validate(size, in_mark, error, top, top_less):
    marks = list()
    for i in range(size):
        mark = float(input(in_mark))
        marks.append(mark)
        while mark > top or mark < top_less:
            print(error)
            mark = float(input(in_mark))
            marks.append(mark)
    return marks






def avg(marks, passed,av_fl,av_ps,cn_fl,cn_ps):
    count_pass, total_pass = 0, float(0)
    count_fail, total_fail = 0, float(0)
    for i in marks:
        if i >= passed:
            total_pass += i
            count_pass += 1
        else :
            total_fail += i
            count_fail += 1

    avg_failed = total_fail / count_fail
    avg_passed = total_pass / count_pass

    print(av_ps, avg_passed)
    print(cn_ps, count_pass)
    print(av_fl, avg_failed)
    print(cn_fl, count_fail)
