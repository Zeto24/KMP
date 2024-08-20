def main():
    a = int(input('Masukan nilai a: '))
    b = int(input('Masukan nilai b: '))
    
    temp = a
    while a >= b: a -= b
    
    print('\n%d mod %d = %d' % (temp, b ,a))
    
if __name__ == '__main__':
    main()