# For a given integer N, print all the squares of integer numbers where the
# square is less than or equal to N, in ascending order.

N = int(input("введите число: "))
for i in range(1, N+1):
    if i**2 <= N:
        print (i**2)
        