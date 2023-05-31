def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    print(x)


numbers = [1, 2, 3, 7, 1, 2, 3, 4, 5, 3, 6, 5, 1, 2, 3, 8]
unique_list(numbers)
