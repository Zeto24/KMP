def main():
    print('Masukan data diri Anda')
    nama = input('Nama\t: ')
    alamat = input('Alamat\t: ')
    telepon = input('No telepon\t: ')
    
    print('\nData diri: %s, %s, %s' % (nama, alamat, telepon))
    
    print(('\ntype(nama)\t: %s' % type(nama)))
    print(('\ntype(alamat)\t: %s' % type(alamat)))
    print(('\ntype(telepon)\t: %s' % type(telepon)))
    
if __name__ == '__main__':
    main()