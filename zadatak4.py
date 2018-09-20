def sum_of_odd_squares(n):

    suma = 0

    for i in range(1, n):
        if i < n:
            if not i % 2 == 0:

                suma += i*i

    return suma


print(sum_of_odd_squares(6))