import fractions

a = fractions.Fraction(2, 4)
b = fractions.Fraction(2, 4, _normalize=False)

print(f'{b} Dinormalisasi/Disederhanakan menjadi = {a}')
print(f'{b} Tidak disederhanakan')