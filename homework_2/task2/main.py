n = int(input('введите n: '))
f = 1
for i in range(1, n+1):
    f *= i
    print(f, end=' ')
