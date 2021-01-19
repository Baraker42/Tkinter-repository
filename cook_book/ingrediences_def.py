from tkinter import *
from tkinter import messagebox
import json

#last edit 19.1.2021: v základu funguje jak má. Jdou vkládat suroviny, jdou mazat suroviny, jdou upravovat suroviny
#nicméně mi to přijde celkem neelegatní, takže budu později ladit a přidávat funkce
#přidat možnost vymazat a upravit surovinu hned po přidání
#zatím funguje pěkně - třeba přidat funkce úpravy stavu suroviny(to jest přejmenování, aktualizace současného počtu) případně celkové vymazání (myslet na chyby ne jako korpo)
#otázka jestli nebude jednodušší a praktičtější rozdělit na dvě funkce, přičemž jedna se spustí, když není nic vložené a druhá v příapdě že jsou už nějaké suroviny v souboru(asi ne)
def ingredience_update():
    # slouží k uložení nového záznamu surovin. Řídí se tím, jestli už jsou nějaké suroviny v seznamu či nikoliv
    def save_stock(ingrediences,ingredience_e, quantity_e, unit_e, counter):
        if unlock==True:
            bag={"surovina":ingredience_e, "množství":quantity_e, "jednotka":unit_e}
            ingrediences.append(bag)
        else:
            ingrediences=[]
            bag={"surovina":ingredience_e, "množství":quantity_e, "jednotka":unit_e}
            ingrediences.append(bag)
        with open ("././/suroviny.json", "w") as file:
            json.dump(ingrediences, file)

        global ingredience
        global ingredience_entry
        global quantity
        global quantity_entry
        global unit
        global unit_entry
        global save_button
        
        #vymazání původních řádků
        ingredience.grid_forget()
        ingredience_entry.grid_forget()
        quantity.grid_forget()
        quantity_entry.grid_forget()
        unit.grid_forget()
        unit_entry.grid_forget()
        save_button.grid_forget()
        new_ingredience_label=Label(root, text=ingredience_e)
        new_quantity_label=Label(root, text=quantity_e)
        new_unit_label=Label(root, text=unit_e)

        new_ingredience_label.grid(row=counter,column=0)
        new_quantity_label.grid(row=counter,column=2)
        new_unit_label.grid(row=counter,column=4)

        counter=counter+1

        
        ingredience=Label(root, text="Surovina")
        ingredience_entry=Entry(root,width = 15, borderwidth=5)

        
        quantity=Label(root, text="Množství")
        quantity_entry=Entry(root,width = 10, borderwidth=5)

        
        unit= Label(root, text="Jednotka")
        unit_entry=Entry(root, width= 5, borderwidth=5)

        ingredience.grid(row=counter, column=0)
        ingredience_entry.grid(row=counter, column=1)
        quantity.grid(row=counter, column=2)
        quantity_entry.grid(row=counter,column=3)
        unit.grid(row=counter,column=4)
        unit_entry.grid(row=counter,column=5)

        
        save_button=Button(root,text="Uložit",command=lambda:save_stock(ingrediences,ingredience_entry.get(), quantity_entry.get(), unit_entry.get(),counter))
        save_button.grid(row=counter,column=6)

    root =Tk()
    root.title("Receptar")
    root.iconbitmap("cook.ico")
    #tato část skriptu zjsití, jestli už nějaký soubor se surovinami existuje a pokud ano, tak ho otevře, pokud ne 
    #vytvoří nový list
    try:
        with open ("suroviny.json") as f:
            ingrediences = json.load(f)
            unlock=True

    except FileNotFoundError:
        ingrediences=[]
        pass


    info_label=Label(root, text="Zde můžete přidávat věci do spíže")
    info_label.grid(row=0,column=0,columnspan=6)

    #vytvořeno pouze kvůli zavření jednoho okna - nevymyslel jsem jak jinak bych to mohl provést
    def end_root():
        root.destroy()
        
  
        #funkce pro úpravu informací o surovinách
    def ingredience_edit(ingredience_1):
        #uloží změny v konkrétní surovině chci vyrobit i jednodušší variantu, kde se pouze napíše číslo a jedním tlačítkem potvrdí
        #třeba zařídit, aby po uložení změn došlo k uzavření všech oken a jejich opětovné načtení, jako jsem to už několikrát dělal
        def save_changes(ingredience_1, material_entry, mass_entry, unit_entry):

                update_info={"surovina":material_entry, "množství":mass_entry, "jednotka":unit_entry}
              
                counter=0
                for i in ingrediences:
                    if i["surovina"]==ingredience_1:
                        del ingrediences[counter]
                        ingrediences.insert(counter, update_info)
                    counter=counter+1

                with open ("././/suroviny.json", "w") as file:
                        json.dump(ingrediences, file)
                root.destroy()
                end_root()
                ingredience_update()


        #nové vyskakovací okno
        root =Tk()
        root.title("Receptar")
        root.iconbitmap("cook.ico")
        for i in ingrediences:
            if i["surovina"]==ingredience_1:
                print("tohle chci",i)
                material=i
        

        material_entry=Entry(root, width=15, borderwidth=2, justify="center")
        mass_entry=Entry(root, width=10, borderwidth=2, justify="center")
        unit_entry=Entry(root, width=5, borderwidth=2, justify="center")

        change_info_label=Label(root, text="Zde můžete změnit údaje o surovině")
        #definice štítků
        material_label=Label(root, text="Surovina")
        mass_label=Label(root, text="Množství")
        unit_label=Label(root, text="Jednotka")


        save_material=Button(root, text="Uložit změny", command=lambda: save_changes(ingredience_1, material_entry.get(), mass_entry.get(), unit_entry.get()))
        #vykreslení štítků
        material_label.grid(row=1,column=0)
        mass_label.grid(row=2,column=0)
        unit_label.grid(row=3,column=0)

        change_info_label.grid(row=0, column=0, columnspan=2)
        #Vykreslení konzolí
        material_entry.grid(row=1,column=1)
        mass_entry.grid(row=2, column=1)
        unit_entry.grid(row=3, column=1)
        #vykreslní tlačítka
        save_material.grid(row=4, column=1)
        #instrukce k vyplnění konzolí
        material_entry.insert(0, material["surovina"])
        mass_entry.insert(0, material["množství"])
        unit_entry.insert(0, material["jednotka"])

        root.mainloop()

    def ingredience_delete(ingredience_1):
        really=messagebox.askquestion("Smazat recept",f"Vážně chcete odstranit {ingredience_1} ze seznamu?")
        if really == "yes":
            chest=[]
            for i in ingrediences:
                this_one=i["surovina"]
                if this_one != ingredience_1:
                    chest.append(i)
            with open ("././/suroviny.json", "w") as file:
                json.dump(chest, file)
            root.destroy()
            ingredience_update()


    counter=1
    for i in ingrediences:
        global ingredience_label
        global quantity_label
        global unit_label
        ingredience_1=i["surovina"]
        quantity_1=i["množství"]
        unit_1=i["jednotka"]

        ingredience_label=Label(root, text=ingredience_1)
        quantity_label=Label(root, text=quantity_1)
        unit_label=Label(root, text=unit_1)
        change_button=Button(root, text="Upravit",command = lambda ingredience_1 = ingredience_1: ingredience_edit(ingredience_1) )
        del_button=Button(root, text ="X", command = lambda ingredience_1 = ingredience_1: ingredience_delete(ingredience_1))

        ingredience_label.grid(row=counter,column=0)
        quantity_label.grid(row=counter,column=2)
        unit_label.grid(row=counter,column=4)
        change_button.grid(row=counter, column=5)
        del_button.grid(row=counter, column=6)
        counter=counter+1



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

    counter=counter+1

    ingredience.grid(row=counter, column=0)
    ingredience_entry.grid(row=counter, column=1)
    quantity.grid(row=counter, column=2)
    quantity_entry.grid(row=counter,column=3)
    unit.grid(row=counter,column=4)
    unit_entry.grid(row=counter,column=5)

    global save_button
    save_button=Button(root,text="Uložit",command=lambda:save_stock(ingrediences,ingredience_entry.get(), quantity_entry.get(), unit_entry.get(),counter))
    save_button.grid(row=counter,column=6)

    root.mainloop()
