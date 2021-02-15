
from tkinter import*
import json
from tkinter import messagebox

#tato část skriptu odečítá suroviny podle receptu a aktualizuje je v původním souboru
def cooking(i):
        #musím zvolit index podle hledaného objektu nikoliv pomocí čísla. Když to necham jak to je, tak z toho bude string
        #pravděpodobně jsem to vědel a zapomněl, protože jsem s tím už dlouho nepracoval
        recipe=recipes[i]
        not_enough=0
        miss=[]
        miss_mass=[]
        not_in_stock=[]
        for i in recipe:
            want_ingredience=i["surovina"]
            
            want_mass=i["množství"]
            #s jednotkami bude asi problém, zatím bych je rád zachoval, protože mi přijdou celkem důležité, minimálně vizuálně
            want_unit=i["jednotka"]

            #vyhledá surovinu z receptu v ingrediencích a následně odečte potřebné množství  a v případě, že by se
            #dostala po odečtení do mínusu, tak surovinu neodečte a uživatele upozorní
            #doplnit variantu, kdy nějaká surovina úplně chybí, tedy není její existence evidována
            length=len(ingrediences)
            for search in ingrediences:
                if search["surovina"]!=want_ingredience:
                    length-=1
                    if length==0:
                        not_in_stock.append(want_ingredience)
                        not_enough=+1
                if search["surovina"]==want_ingredience:
                    new_mass=int(search["množství"])-int(want_mass)
                    if new_mass < 0:
                        miss.append(search["surovina"])
                        miss_mass_var=(str(new_mass*-1)+" " + want_unit)
                        miss_mass.append(miss_mass_var)

                        not_enough=+1
                        
                    if new_mass >= 0:
                        change={"množství":new_mass}
                        search.update(change)
        
        #uloží změny v dostupných ingrediencích
        
        if not_enough == 0:        
            with open ("././/suroviny.json", "w") as file:
                    json.dump(ingrediences, file)
                    
            
        if not_enough >=0:  
            #nové rozhraní pro vypsání surovin, kterých je nedostatek nebo nejsou evidované
            not_enough_popup=Tk()
            not_enough_popup.title("Receptář")
            not_enough_popup.iconbitmap("cook.ico")

            #štítky
            not_enough_label=Label(not_enough_popup,text="Nemáš dostatek následujících surovin:",font=("Helvetica",10,"bold"))
            not_enough_label.grid(row=0,column=0,columnspan=2)
            counter=1
            #vypíše suroviny, kterých je nedostatečné množství ve spíži
            for missing in miss:
                missing_mass=miss_mass[counter-1]

                missing_label=Label(not_enough_popup, text=missing)
                missing_mass_label=Label(not_enough_popup, text=missing_mass)

                missing_label.grid(row=counter,column=0)
                missing_mass_label.grid(row=counter,column=1)

                counter+=1
            
            #vypíš suroviny, které nejsou evidované
            not_in_stock_label=Label(not_enough_popup, text="Tyto suroviny nemáš zaevidované:",anchor="center",font=("Helvetica",10,"bold"))
            not_in_stock_label.grid(row=counter,column=0)
            counter+=1
            
            for not_stocked in not_in_stock:
                not_stocked_label=Label(not_enough_popup,text=not_stocked)
                not_stocked_label.grid(row=counter)
                counter+=1
            not_enough_popup.mainloop()
             

def cook_show():
    
    try:
        global ingrediences
        with open ("suroviny.json") as f:
            ingrediences = json.load(f)
            fail=(ingrediences[0])
    except IndexError:
        no_ingredience_root=Tk()
        no_ingredience_root.title("Receptář")
        no_ingredience_root.iconbitmap("cook.ico")
        no_ingredience_label=Label(no_ingredience_root,text="Nemáš žádné suroviny, ze kterých by šlo vařit")
        no_ingredience_button=Button(no_ingredience_root, text="Zavřít",command=no_ingredience_root.destroy)
        no_ingredience_label.grid(row=0,column=0)
        no_ingredience_button.grid(row=1,column=0)
        no_ingredience_root.mainloop()
    global recipes
    #zjistí zda jsou uložené nějaké recepty a pokud ne, informuje uživatele
    with open ("recepty.json") as e:
        
        recipes = json.load(e)
        
        if len(recipes) ==0:
            #rozhraní, které informuje uživatele, že není v tuto chvíli žádný recept uložený
            no_recipe_root=Tk()
            no_recipe_root.title("Receptař")
            no_recipe_root.iconbitmap("cook.ico")
            no_recipe_label=Label(no_recipe_root,text="Nemáš žádný recept, podle kterého by šlo vařit")
            no_recipe_button=Button(no_recipe_root, text="Zavřít",command=no_recipe_root.destroy)        
            no_recipe_label.grid(row=0,column=0)
            no_recipe_button.grid(row=1,column=0)
            no_recipe_root.mainloop()
        else:
            #v případě, že je k dispozici jak dokument s recepty i se surovinami, spustí rozhrnaí por vaření
            root=Tk()
            root.title("Receptář")
            root.iconbitmap("cook.ico")

            counter=0
            #vypíše recepty, které jsou k dispozici
            for i in recipes:
                recipe_label=Label(root, text=i)
                recipe_label.grid(row=counter,column=0)

                cook_button=Button(root, text="Vařit!", command=lambda i=i:cooking(i))
                cook_button.grid(row=counter,column=1)
                counter=+1

            root.mainloop()
            


