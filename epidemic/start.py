from tkinter import *
from Game import faze_2

root = Tk()
root.title("Epidemic The Game")
root.iconbitmap("c:/Users/PAN Hakl/Desktop/Programování/vir.ico")
#vykreslí konzole na napsání jména hráče a jména viru
e=Entry(root, width = 30, borderwidth=5)
vir=Entry(root,width = 30, borderwidth=5)

vstup= Label(root, text="Vítejte ve hře Epidemie, zvládnete porazit zákeřný virus?")
#sputí další herní okno a zavře předchozí
def faze_1(starosta,virus):
    root.destroy()
    faze_2(starosta,virus)
    

start_game = Button(root, text ="Start game", padx=30, pady=25, command=lambda :faze_1(e.get(),vir.get()))


vstup.pack()
e.pack()
vir.pack()
start_game.pack()


e.insert(0,"Zadejte vaše jméno")
vir.insert(0,"Zadejte jméno viru")


root.mainloop()

