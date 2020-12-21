from tkinter import *
import json

#zatím funguje pěkně - třeba přidat funkce úpravy stavu suroviny(to jest přejmenování, aktualizace současného počtu) případně celkové vymazání (myslet na chyby ne jako korpo)
#otázka jestli nebude jednodušší a praktičtější rozdělit na dvě funkce, přičemž jedna se spustí, když není nic vložené a druhá v příapdě že jsou už nějaké suroviny v souboru(asi ne)
def ingredience_update():
    def save_stock(ingrediences,ingredience_e, quantity_e, unit_e, counter):
        if unlock==True:
            bag={"surovina":ingredience_e, "množství":quantity_e, "jednotka":unit_e}
            ingrediences.append(bag)
        else:
            ingrediences=[]
            bag={"surovina":ingredience_e, "množství":quantity_e, "jednotka":unit_e}
            ingrediences.append(bag)
            print(ingrediences)
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
    try:
        with open ("suroviny.json") as f:
            ingrediences = json.load(f)
            unlock=True

    except FileNotFoundError:
        ingrediences=[]
        pass
   


    print(ingrediences)
    info_label=Label(root, text="Zde můžete přidávat věci do spíže")
    info_label.grid(row=0,column=0,columnspan=6)

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

        ingredience_label.grid(row=counter,column=0)
        quantity_label.grid(row=counter,column=2)
        unit_label.grid(row=counter,column=4)
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
