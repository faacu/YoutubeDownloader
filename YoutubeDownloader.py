import pytube, tkinter
from tkinter import filedialog 

centinela = 0

while centinela == 0:
    print("1- Descargar video\n2- Informacion de un video\n3- Salir")
    el = int(input())
    if el == 1:
        print("Ingrese link del url: ")
        url = input()
        yt = pytube.YouTube(url)
        root = tkinter.Tk()
        root.directory = filedialog.askdirectory()
        root.destroy()
        if yt.streams.first().download(root.directory):
            print("Se descargo con exito!")
    elif el == 2:
        print("Ingrese link del url: ")
        url = input()
        yt = pytube.YouTube(url)
        print("Titulo: "+yt.title)
        print("Descripcion: "+ yt.description)
        print("Duracion: "+ str(yt.length))
        print("Autor: "+ yt.author)
        print("Url del canal: "+ yt.channel_url)
    elif el == 3:
        centinela = 1