def echo(value, newline=True, end=' '):
    if newline:
        print(value)
    else:
        print(value, end=end)
        
echo('Kursus')              # akan membuat baris baru
echo('Pemrograman', False)  # tidak akan membuat baris baru
echo('Python 3', True)      # akan membuat baris baru