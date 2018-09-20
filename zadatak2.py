def sum_of_squares(n):

    suma = 0

    for i in range(1, n):
        if i < n:
            suma += i*i

    return suma


print(sum_of_squares(6))