def segitiga_siku2():
    tinggi = int(
        input("Masukan tinggi segitiga siku-siku yang akan dicetak: "))
    print("\n")
    for i in range(tinggi):
        print("* "*(i+1))


def segitiga_samaSisi():
    segitiga = ""
    x = int(input("Masukkan tinggi segitiga sama sisi:"))
    bar = x
    # Looping Baris
    while bar >= 0:
        # Looping Kolom Spasi Kosong
        kol = bar
        while kol > 0:
            segitiga = segitiga + "   "
            kol = kol - 1
        # Looping Kolom Bintang Sisi Kiri
        kiri = 1
        while kiri < (x - (bar-1)):
            segitiga = segitiga + " * "
            kiri = kiri + 1
        # Looping Kolom Bintang Sisi Kanan
        kanan = 1
        while kanan < kiri - 1:
            segitiga = segitiga + " * "
            kanan = kanan + 1
        segitiga = segitiga + "\n\n"
        bar = bar - 1
    print(segitiga)


def persegi():
    sisi = int(input("Masukan panjang sisi persegi yang akan dicetak: "))
    print('\n')
    for i in range(sisi):
        print("*  "*sisi)


def persegi_panjang():
    panjang = int(input("Masukan panjang persegi yang akan dicetak: "))
    tinggi = int(input("Masukan tinggi persegi yang akan dicetak: "))
    print("\n")
    for i in range(tinggi):
        print("*  "*panjang)
