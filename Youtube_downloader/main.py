from pytube import YouTube
import os

os.system('cls')
print(" Youtube Downloader ".center(50, '='))

url = input("\nMasukan URL Video: ")
video = YouTube(url)
streams = set()

print("Loading....")
for stream in video.streams.filter(type="video"):
    streams.add(stream.resolution)

print("\nKualitas video yang tersedia: ", streams)
while(True):
    try:
        Res = input("Pilih kualitas video: ")
        stream = video.streams.filter(
            file_extension="mp4").get_by_resolution(Res)
        stream.download()
        print('\n')
        print(" Download berhasil! ".center(50, "="))
        break
    except:
        print("Vidio tidak bisa didownload pada kualitas ini, coba download pada kualitas lain")
