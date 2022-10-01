N = int(input('Введите число: '))
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

n = list(range(-N, N+1))
print(n)
res = n[a-1] * n[b-1]
print(res)
