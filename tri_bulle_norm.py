def tri_bulle_norm(list):

    long_tableau = len(list)

    for i in range(long_tableau - 1):

        for j in range(0, long_tableau - i - 1):

            if list[j] > list[j + 1]:

                list[j], list[j + 1] = list[j + 1], list[j]

    return list

print(tri_bulle_norm(list))