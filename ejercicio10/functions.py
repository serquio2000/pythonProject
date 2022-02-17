def size():
    size = int(input("insert a size:"))
    return size

def add_record(size):
    book = list()
    for i in range(size):
        book.append(input("insert a name of book:"))
        book.append(input("insert a name of author:"))
        book.append(input("insert a name of editorial:"))
        book.append(int(input("insert books remaining:")))
        book.append(input("insert a name of user:"))
        book.append(int(input("insert a days remaining:")))
    return book



