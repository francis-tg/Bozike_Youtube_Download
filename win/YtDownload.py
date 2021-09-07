#pip install pytube
import pytube
from tkinter import messagebox
import os


def Download( url):
    path = os.path.join("C:\\","Users",os.getlogin(),"Desktop","BOZIKE_Videos",'')
    video = pytube.YouTube(url)
    print("Recherche de la video")
    messagebox.showinfo("Information","Patiente je cherche la vidéo")
    for stream in video.streams:
        get_hight_video = video.streams.get_highest_resolution()
        print("Téléchargement...")
        messagebox.showinfo("Téléchargement", "Patienter pendant que le téléchargement s'éffectue")
        down = get_hight_video.download(output_path=path)
        if down:
            print("Terminé")
            messagebox.showinfo("Information", "Téléchargement terminé")
            break
        else:
            messagebox.showerror('Téléchargement échoué')
def OpenFolder():
    return os.startfile(os.path.join("C:\\","Users",os.getlogin(),"Desktop","BOZIKE_Videos",''))

# path = os.path.join("C:\\","Users",os.getlogin(),"Downloads","")
# for x in os.scandir(path):
#     if x.is_dir():
#         if x.name == 'BOZIKE_Videos':
#             pass
#         else:
#             os.mkdir(os.path.join("C:\\","Users",os.getlogin(),"Download","BOZIKE_Videos",''))
            