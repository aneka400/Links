#https://github.com/aneka400/Links.git
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def tmp(my_list, n=0):
    if n ==  len(my_list):
        print("конец списка")
        return
    print(my_list[n])
    tmp(my_list, n + 1)
tmp(my_list)
