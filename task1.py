def multiples():

    three_multi = []
    five_multi = []

    x = range(3, 1000)

    for threes in x:
        if threes % 3 == 0:
            three_multi.append(threes)

    for fives in x:
        if fives % 5 == 0:
            five_multi.append(fives)

    mutual_lis = []

    for i in three_multi:
        if i in five_multi:
            mutual_lis.append(i)
            three_multi.remove(i)
            five_multi.remove(i)

    sum_threes = sum(three_multi)
    sum_fives = sum(five_multi)
    sum_mutual = sum(mutual_lis)

    total = sum_threes+sum_fives+sum_mutual

    print(total)

