import pandas as pd
import os
import csv

df = pd.read_csv(
    r"G:\kuliah\machine Learning\probabilitas_statistik\package_python_data\pandas\kaggle_explorations-master\belajar_python_pandas\dataset\winemag-data-130k-v2.csv")

# path-path folder dan file
path_current = os.getcwd()
path_data = path_current+"\\mencetak_deskripsi_data\\deskripsi_data"
path_file = path_data+"\\Deskripsi.csv"

# membuat direktori/folder baru untuk menampung file
if not os.path.exists(path_data):
    os.makedirs(path_data)

# deskripsi data
deskripsi = df.describe()
name_columns = df.columns
jml_kol = len(name_columns)
jml_baris = df[name_columns[0]].count()
Size_data = df.size
dic_data = {'Rows': jml_baris,
            'Columns': jml_kol,
            'Size': Size_data}

# menulis data ke format csv
deskripsi.to_csv(path_file)
with open(path_file, mode='a') as csv_file:
    Writer = csv.writer(csv_file, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for key, item in dic_data.items():
        Writer.writerow([key, item])
print("write done!")
