price = float(input('price: '))
discount = float(input('discount: '))
vat = float(input('vat: '))

base = price * (1 - discount / 100)
vat_amount = base * (vat/100)
total = base + vat_amount

f_base = f"{base:.2f}"
f_vat = f"{vat_amount:.2f}"
f_total = f"{total:.2f}"

print(f'База после скидки: {f_base}₽')
print(f'НДС: {f_vat}₽')
print(f'Итого к оплате: {f_total}₽')