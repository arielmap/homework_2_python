str_num = input("введите вещественное число: ")
sum_digits = 0
for n in str_num:
    if n.isdigit():
        sum_digits += int(n)
print(f'{str_num} ->  {sum_digits}')