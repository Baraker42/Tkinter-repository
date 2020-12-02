from tkinter import *
#import cooking_def
from update_def import *
from recipe_def import new_recipe
from ingrediences_def import ingredience_update

#spustí funkci s tvorbou receptu
def recipe_start():
    #root.destroy()
    new_recipe()

    #spustí funkci, která zkotroluje zda existuje soubor s recepty, pokud ne nepokračuje dál
def load_file ():
    
    try:
        with open ("recepty.json") as f:
            recepies = json.load(f)
        
        #root.destroy()
        recipe_update(recepies)
        

    except FileNotFoundError:
        no_recipe()

#spustí funkci, která umožňuje přidání a úpravu surovin
def ingredience_interface():
    #root.destroy()
    ingredience_update()



root =Tk()
root.title("Receptar")
root.iconbitmap("cook.ico")

#vytvoření nových štítků a tlačítek
entry=Label(root,text="Vítejte v receptáři! Co si přejete dělat?")
cook=Button(root, text="Pojďme vařit!")
recipe=Button(root, text="Zadat recept",command=recipe_start)
update=Button(root, text="Upravit recept",command=load_file)
ingrediences=Button(root, text="Doplnit suroviny",command=ingredience_interface)


#umístění štítků a tlačítek do uživatelksého rozhrani
entry.grid(row=1,column=0, columnspan=2)
cook.grid(row=2,column=0)
ingrediences.grid(row=2,column=1)
recipe.grid(row=3,column=0)
update.grid(row=3,column=1)

root.mainloop()
