def kali():
    return 10 * 20
def echo():
    for i in range(3):
        print('Python')
def main():
    # memanggil fungsi kali()
    print('Memanggil fungsi kali(): ')
    print('10 x 20 = %d' % kali())
    # Memanggil fungsi echo()
    print('Memanggil fungsi echo(): ')
    echo()
    
if __name__ == '__main__':
    main()