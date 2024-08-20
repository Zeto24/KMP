data = ['ani', 'ANE', 'Ana']
data.sort()
print('Tanpa lambda')
print(data)

data = ['ani', 'ANE', 'Ana']
data.sort(key=lambda element: element.lower())
print('Dengan lambda')
print(data)