def main():
    c = input('Masukan huruf: ')[0].lower()
    
    if c in ['a', 'e', 'i', 'e', 'o']:
        print('%c adalah huruf vokal' % c)
        
if __name__ == '__main__':
    main()