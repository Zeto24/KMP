# variabel global
g = 10

def f1():
    print('Nilai variabel g didalam f1(): %d' % g)

def f2():
    # mencoba untuk mengubah nilai g
    g = 20
    print('Nilai variabel g didalam f1(): %d' % g)

def f3():
    print('Nilai variabel g didalam f1(): %d' % g)

def main():
    # memanggil fungsi f1(), f2() dan f3()
    f1()
    f2()
    f3()
    
if __name__ == "__main__":
    main()