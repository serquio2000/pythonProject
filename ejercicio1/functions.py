
def validate(attempt, in_num,att):
    count = 0
    num = int(input(in_num))
    while (num < 10 or num>5000 )and count < attempt :
        print(att)
        num = int(input(in_num))
        count += 1
    return num