import matplotlib.pyplot as plt
import pandas as pd
import os

os.system('cls')
print(' Plotting '.center(40, '='))

# =========== memasukkan file =============
path_file = str(input('Masukkan path data file: '))
data_file = pd.read_csv(path_file)

os.system('cls')
# print(data_file[garis_x])
# print(data_file[garis_y])
# =========== memilih jenis plot ==========
print('1. Line Plot\n2. Histogram')
jenis_plot = str(input('Pilih jenis plot: '))

# =========== mmebuat plot ================
if jenis_plot == '1' or jenis_plot.lower() == 'line plot' or jenis_plot.lower() == 'line':
    judul = str(input('Title plot\t: '))
    garis_x = str(input('Axis X\t\t: '))
    garis_y = str(input('Axis Y\t\t: '))
    plt.plot(data_file[garis_x], data_file[garis_y])
    plt.title(judul)
    plt.xlabel(garis_x)
    plt.ylabel(garis_y)
    plt.show()
    os.system('cls')
