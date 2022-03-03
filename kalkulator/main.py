# program kalkulator sederhana
import os

while True:
    try:
        print("kalkulator".center(30, '='))
        angka1 = int(input("Masukan angka 1\t\t: "))
        operat = str(input("Pilih operator(+,-,/,x)\t: "))
        angka2 = int(input("Masukan angka 2\t\t: "))
        print('\nHasil:')

        if operat == "+":
            hasil = angka1+angka2
            print(angka1, '+', angka2, '=', hasil)
        elif operat == "-":
            hasil = angka1-angka2
            print(angka1, '-', angka2, '=', hasil)
        elif operat == "/":
            hasil = angka1/angka2
            print(angka1, '/', angka2, '=', hasil)
        elif operat == '*' or operat.lower() == "x":
            hasil = angka1*angka2
            print(angka1, 'x', angka2, '=', hasil)
        else:
            print('Warning: operator yang anda masukan salah')
            os.system('sleep(1000)')
            os.system('cls')
            continue

        jawab = str(input('\nketik exit untuk keluar dari program.\n'))
        if(jawab.lower() == 'exit'):
            break
        else:
            os.system('cls')

    except ValueError:
        print('\nWarning: input yang anda masukan bukan angka')
        os.system('pause > null')
        os.system('cls')
    except ZeroDivisionError:
        print('\nHasil:')
        print(angka1, '/', angka2, '= 00')
        jawab = str(input('\nketik exit untuk keluar dari program.\n'))
        if(jawab.lower() == 'exit'):
            break
        else:
            os.system('cls')
