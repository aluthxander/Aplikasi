# program kalkulator sederhana
import os
import time
import re

def kalkulasi(angka1, operator, angka2):
    if operator == "+":
        hasil = angka1+angka2
    elif operator == "-":
        hasil = angka1-angka2
    elif operator == "/":
        hasil = angka1/angka2
    elif operator == '*' or operat.lower() == "x":
        hasil = angka1*angka2
    return hasil

def iterasi():
    jawab = str(input('\nketik exit untuk keluar dari program.\n'))
    return jawab.lower()

while True:
    try:
        os.system('cls')
        print("kalkulator".center(30, '='))
        angka1 = int(input("Masukan angka 1\t\t: "))
        operat = str(input("Pilih operator(+,-,/,x)\t: "))
        if not re.match(r'^[\+\-\*xX\/]', operat) or len(operat) > 1:
            print('Warning: operator yang anda masukan salah')
            time.sleep(2)
            continue
        angka2 = int(input("Masukan angka 2\t\t: "))
        print('\nHasil:')
        print(kalkulasi(angka1, operat, angka2))

        if(iterasi() == 'exit'):
            break
        else:
            None

    except ValueError:
        print('\nWarning: input yang anda masukan bukan angka')
        time.sleep(2)
    except ZeroDivisionError:
        print('\nHasil:')
        print(angka1, '/', angka2, '= 00')
        if(iterasi() == 'exit'):
            break
        else:
            None
