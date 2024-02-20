from tkinter import *

#création de la fenêtre
window = Tk()

#personnalisation de la fenêtre
window.title("Le jeu")
window.geometry("1080x720")
window.minsize(480, 360)
window.config(background='#F3A1FF')
#window.iconbitmap("")

#ajout du texte
label_title = Label(window, text="Hello World", font=("#F3A1FF"))
label_title.pack()

window.mainloop()