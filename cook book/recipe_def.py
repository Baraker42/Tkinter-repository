
# po uložení receptu třeba přidat možnost návratu na původní okno (případně ho nezavírat a při uložení zavřít toto)
from tkinter import *
import json
def new_recipe():
    #základní rozhrani
    root =Tk()
    root.title("Receptar")
    root.iconbitmap("cook.ico")

    global row_counter
    row_counter=2
    print(row_counter)
    
    #připraví lisk do kterého bude ukládat soubory surovin
    whole=[]

    #přidá nový řádek
    def new_row(e_ingredience,e_quantity,e_unit):
        global row_counter
        #vypsání naposledy zadaných surovin do předchozího řádku
        label_ingredience=Label(root, text=e_ingredience)
        label_ingredience.grid(row=row_counter,column=0)

        label_quantity=Label(root, text=e_quantity)
        label_quantity.grid(row=row_counter,column=2)

        label_unit=Label(root, text=e_unit) 
        label_unit.grid(row=row_counter,column=4)
        record={"surovina":e_ingredience,"množství":e_quantity,"jednotka":e_unit}
        
        #přidá zápis do celého seznamu
        whole.append(record)
        

        
        row_counter=row_counter+1

        #globalizace všech potřebných jednotek
        global ingredience
        global ingredience_entry
        global quantity
        global quantity_entry
        global unit
        global unit_entry
        global new_ingredience
        global save_recipe
        
        #nutné vymazání předchozích řádků
        ingredience.grid_forget()
        ingredience_entry.grid_forget()
        quantity.grid_forget()
        quantity_entry.grid_forget()
        unit.grid_forget()
        unit_entry.grid_forget()
        new_ingredience.grid_forget()
        save_recipe.grid_forget()

        #přidat ingredienci
        ingredience=Label(root, text="Surovina")
        ingredience_entry=Entry(root,width = 15, borderwidth=5)
        ingredience.grid(row=row_counter,column=0)
        ingredience_entry.grid(row=row_counter,column=1)

        #přidat množství
        quantity=Label(root, text="Množství")
        quantity_entry=Entry(root,width = 10, borderwidth=5)
        quantity.grid(row=row_counter,column=2)
        quantity_entry.grid(row=row_counter,column=3)

        #přidat jednotku
        unit= Label(root, text="Jednotka")
        unit_entry=Entry(root, width= 5, borderwidth=5)
        unit.grid(row=row_counter,column=4)
        unit_entry.grid(row=row_counter,column=5)

        #přidat řádek na vložení další ingredience
        new_ingredience=Button(root, text="Přidat surovinu",command=lambda:new_row(ingredience_entry.get(),quantity_entry.get(),unit_entry.get()))
        new_ingredience.grid(row=(row_counter+1),column=5)

        #přidat řádek na uložení receptu
        save_recipe=Button(root,text="Uložit recept", command=lambda:final(whole,name_entry.get()))
        save_recipe.grid(row=(row_counter+2),column=5)
    
    #ukončení tvorby nového receptu - uložení do souboru json
    def final(whole,e_name):
       
        #v případě že už nějaký soubor json vytvořený je
        try:
            with open ("recepty.json") as f:
                data = json.load(f)
            finalization=data
            finalization[e_name]=whole

        #v případě že žádný soubor vytvořený není, tak ho vytvoří
        except FileNotFoundError:
            finalization={}
            finalization[e_name]=whole

        #uloží vytvořený recept
        with open ("././/recepty.json", "w") as file:
            json.dump(finalization, file)
        root.destroy()


    #název receptu
    name=Label(root, text="Název receptu")
    name_entry=Entry(root,width = 20, borderwidth=5)
    
    #suroviny
    global ingredience
    global ingredience_entry
    ingredience=Label(root, text="Surovina")
    ingredience_entry=Entry(root,width = 15, borderwidth=5)

    
    #množství
    global quantity
    global quantity_entry
    quantity=Label(root, text="Množství")
    quantity_entry=Entry(root,width = 10, borderwidth=5)

    #jednotka
    global unit
    global unit_entry
    unit= Label(root, text="Jednotka")
    unit_entry=Entry(root, width= 5, borderwidth=5)

    #přidat surovinu
    global new_ingredience
    new_ingredience=Button(root,text="Přidat surovinu",command=lambda:new_row(ingredience_entry.get(),quantity_entry.get(),unit_entry.get()))

    #uložit recept
    global save_recipe
    save_recipe=Button(root,text="Uložit recept", command=lambda:final(whole,name_entry.get()))

    #vykreslení tlačítek apod
    #1.řádek
    name.grid(row=1,column=2)
    name_entry.grid(row=1,column=3)

    #2řádek
    ingredience.grid(row=2,column=0)
    ingredience_entry.grid(row=2,column=1)
    quantity.grid(row=2,column=2)
    quantity_entry.grid(row=2,column=3)
    unit.grid(row=2,column=4)
    unit_entry.grid(row=2,column=5)

    #3.řádek  
    new_ingredience.grid(row=3,column=5)

    #4.řádek
    save_recipe.grid(row=4,column=5)

    root.mainloop()
