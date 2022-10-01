a = int(input('Введите число: '))
b = []
summa = 0
for i in range(1, a+1):
    b.append((1+1/i)**i)
print(b)
summa = sum(b)
print(round(summa, 3))