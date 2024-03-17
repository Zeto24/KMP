def maksimum(a, b):
    if a >= b:
        return a
    else:
        return b
print('Tanpa lambda')   
print(maksimum(4, 3))
print(maksimum(3, 4))

maksimum = lambda a, b: a if a >= b else b
print('Dengan lambda')
print(maksimum(4, 3))
print(maksimum(3, 4))
