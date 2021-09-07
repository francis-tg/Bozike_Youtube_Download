from tkinter import *
from .YtDownload import Download, OpenFolder

class MainWindow:
    def __init__(self, title):
        self.win = Tk()
        self.win.title(title)
        self.win.resizable(False, False)
        self.win.geometry("600x600")
        self.UrlText = Label(self.win, text="Téléchargeur youtube pour Monsieur BOZIKE Fidèle", font=('Impact',17))
        self.UrlText.pack()
        self.UrlText = Label(self.win, text="Entrer l'Url :", font=('Impact',15))
        self.UrlText.pack(pady=10)
        self.url = Entry(self.win, font=('Consolas', 15),width=250)
        self.url.pack()
        self.btn = Button(self.win, text="Télécharger", font=('Arial',13),
         background='#393939',
          foreground='#fff', relief=GROOVE, command=self.SetDownload).pack(pady=10)
        self.btnopen = Button(self.win, text="Ouvrir le dossier de téléchargement", font=('Arial',13),
         background='#393939',
          foreground='#fff', relief=GROOVE, command=self.Open).pack(pady=10)
    def Run(self):
        return self.win.mainloop()
    def SetDownload(self):
        self.getUrl = self.url.get()
        return Download(self.getUrl)
    def Open(self):
        return OpenFolder()
        
        