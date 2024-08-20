a = 2
b = a 
c = 3

print(f'id{a} = {id(a)}')
print(f'id{b} = {id(b)}')
print(f'id{c} = {id(c)}')

print(f'{a} is {b} = {a is b}')
print(f'{a} is {c} = {a is c}')
print(f'{a} is not {b} = {a is not b}')
print(f'{a} is not {c} = {a is not c}')
