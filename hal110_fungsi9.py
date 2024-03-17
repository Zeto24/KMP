import math

# fungsi bagian luar
def luasLingkaran(r):
    
    # fungsi lokal
    def kuadrat(x):
        return x ** 2
    
    # memanggil fungsi lokal dari fungsi bagian luar
    return math.pi * kuadrat(r)

def main():
    r = float(input('Masukan jari-jari lingkaran: '))
    # memanggil fungsi f1(), f2(), dan f3()
    luas = luasLingkaran(r)
    
    print('Luas Lingkaran = %.3f' % luas)
    
if __name__ == '__main__':
    main(5)