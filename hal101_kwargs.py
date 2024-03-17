def f(**kwargs):
    print('Nilai **kwargs\t: %s' % repr(kwargs))
    print('Tipe **kwargs\t: %s' % type(kwargs))
    
# memanggil fungsi f() dengan dua argumen
f(satu=1, dua=2)
print(' ')
f(satu=1, dua=2, tiga=3)
