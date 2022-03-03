import os
import cetak


# main program
while True:
    try:
        print("1. Segitiga Siku-siku\n2. Segitiga Sama Sisi\n3. Persegi\n4. Persegi Panjang\n5. Exit")
        input_user = str(input("Silahkan pilih dari daftar menu diatas: "))
        pilihan = input_user.upper()

        if pilihan == '1' or pilihan == 'SEGITIGA SIKU-SIKU':
            cetak.segitiga_siku2()
            os.system('pause > NULL')
            os.system('cls')
        elif pilihan == '2' or pilihan == 'SEGITIGA SAMA SISI':
            cetak.segitiga_samaSisi()
            os.system('pause > NULL')
            os.system('cls')
        elif pilihan == '3' or pilihan == 'PERSEGI':
            cetak.persegi()
            os.system('pause > NULL')
            os.system('cls')
        elif pilihan == '4' or pilihan == 'PERSEGI PANJANG':
            cetak.persegi_panjang()
            os.system('pause > NULL')
            os.system('cls')
        elif pilihan == '5' or pilihan == 'EXIT':
            break
        else:
            print("pilihan tidak ada didaftar menu")
            os.system('pause > NULL')
            os.system('cls')
    except ValueError:
        print("Maaf, input yang anda masukan bukan angka. Silahkan Coba lagi")
        os.system('pause > NULL')
        os.system('cls')
