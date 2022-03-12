from logging import exception
import pandas as pd
import os
import csv
# G:\kuliah\machine Learning\probabilitas_statistik\package_python_data\pandas\kaggle_explorations-master\belajar_python_pandas\dataset\winemag-data-130k-v2.csv
def cetak_csv(data, path_dir):
    # deskripsi data
    deskripsi = data.describe()
    name_columns = data.columns
    jml_kol = len(name_columns)
    jml_baris = data[name_columns[0]].count()
    Size_data = data.size
    dic_data = {'Rows': jml_baris,
                'Columns': jml_kol,
                'Size': Size_data}

    # menulis data ke format csv
    path_file = path_dir+r"\Deskripsi.csv"
    
    if jml_baris == 0:
        print("Data File yang anda masukan kosong")
        return 0
    else:
        deskripsi.to_csv(path_file)
    with open(path_file, mode='a') as csv_file:
        Writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for key, item in dic_data.items():
            Writer.writerow([key, item])
    print("Deskripsi data berhasil dibuat!")

def persiapan_data():
    # masukan path data dan nama file
    path_in = input("Masukan path data beserta nama file: ")
    df = pd.read_csv(path_in)
    # path-path folder dan file
    path_current = os.getcwd()
    path_dir = path_current+r"\mencetak_deskripsi_data\deskripsi_data"
    return df, path_dir

def main():
    df, path_dir = persiapan_data()
    # membuat direktori/folder baru untuk menampung file
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
    cetak_csv(df, path_dir)

try:
    main()
except FileNotFoundError:
    print("File tidak ditemukan!")
except PermissionError:
    print("Path yang anda masukan salah")
