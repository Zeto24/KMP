import sys

def main():
    print('PROGRAM PEMBAGIAN BILANGAN')
    a = float(input('Masukan nilai a: '))
    b = float(input('Masukan nilai b: '))
    
    if b == 0:
        print('\nSalah: Nilai b tidak boleh nol')
        sys.exit(1)
        
    print('\n%.3f / %.3f = %.3f' % (a, b, a / b))
    
if __name__ == '__main__':
    main()