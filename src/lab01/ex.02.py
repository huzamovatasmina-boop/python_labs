#Ввод чисел
a = str(input('a: '))
b = str(input('b: '))
#перевод в правильную запись вещественных чисел
a_str = a.replace(',', '.')
b_str = b.replace(',', '.')

a = float(a_str)
b = float(b_str)

sum = a + b
avg = sum / 2
print(f'sum={sum}, avg={avg:.2f}')