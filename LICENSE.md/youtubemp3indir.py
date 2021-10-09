import youtube_dl
import sys
import time

print("\n")

print("                __                                                                __")                                                   
print("                  \033[92m\                                                              /")
print("                   \033[92m\                                                            /")
print("                    \033[92m\|--------------------------------------------------------|/")
print("                     \033[92m|                  .....MAJESTAR....                     |")
print("                     |--------------------------------------------------------|")
print("                     |   CODDED BY MAJESTAR WİTH PYTHON3 / YOUTUBE-DL         |")
print("                     | -------------------------------------------------------|")
print("                     |    MÜZİK EN MAX YÜKSEK KALİTEDE İNECEKTİR              |")
print("                     |                    Hoşgeldiniz :)                      |")
print("                     |    \033[94mLinki Yapıştırmadıysanız Müzik İnmeyecektir         |")
print("                     |               KEYİFLİ<><><><><><><>DİNLEMELER          |")
print("                     |       MÜZİK YoutubeMP3-Tr KLASÖRÜNE İNECEKTİR          |")
print("                    /|--------------------------------------------------------|\ ")                                                 
print("                   /                                                            \ ")
print("                __/                                                              \__ ")
print(" \033[92m\n")             
time.sleep(2)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

if __name__ == "__main__":
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        filenames = sys.argv[1:]
        ydl.download(filenames)
