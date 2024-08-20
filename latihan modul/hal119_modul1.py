import aritmetika

def main():
    a = int(input('Masukan nilai a: '))
    b = int(input('Masukan nilai b: '))
    c = float(b)
    
    print('a\t: %d' % a)
    print('b\t: %d' % b)
    print('c\t: %.2f\n' % c)
    
    print('a + b\t: %d' % aritmetika.tambah(a, b))
    print('a - b\t: %d' % aritmetika.kurang(a, b))
    print('a * b\t: %d' % aritmetika.kali(a, b))
    print('a // b\t: %d' % aritmetika.bagi(a, b))
    print('a / c\t: %f' % aritmetika.bagi(a, b))
    print('a','%','b\t: %d' % aritmetika.sisaBagi(a, b))
    print('a ** b\t: %d' % aritmetika.pangkat(a, b))
    
if __name__ == '__main__':
    main()