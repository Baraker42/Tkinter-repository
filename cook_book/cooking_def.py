from tkinter import*
import json
from tkinter import messagebox


    

def cook_show():
    root=Tk()
    root.title("Receptář")
    root.iconbitmap("cook.ico")
    with open ("suroviny.json") as f:
        ingrediences = json.load(f)
    with open ("recepty.json") as e:
        recipes = json.load(e)

    def cooking(i):
        #musím zvolit index podle hledaného objektu nikoliv pomocí čísla. Když to necham jak to je, tak z toho bude string
        #pravděpodobně jsem to vědel a zapomněl, protože jsem s tím už dlouho nepracoval
        recipe=recipes[i]
        print(ingrediences)
        not_enough=0
        miss=[]
        miss_mass=[]
        for i in recipe:
            want_ingredience=i["surovina"]
            want_mass=i["množství"]
            #s jednotkami bude asi problém, zatím bych je rád zachoval, protože mi přijdou celkem důležité, minimálně vizuálně
            want_unit=i["jednotka"]

            #vyhledá surovinu z receptu v ingrediencích a následně odečte potřebné množství  a v případě, že by se
            #dostala po odečtení do mínusu, tak surovinu neodečte a uživatele upozorní
            
            for search in ingrediences:
                if search["surovina"]==want_ingredience:
                    new_mass=int(search["množství"])-int(want_mass)
                    if new_mass <= 0:
                        miss.append(search["surovina"])
                        miss_mass_var=(str(new_mass*-1)+" " + (search["jednotka"]))
                        miss_mass.append(miss_mass_var)

                        not_enough=+1
                            
                        #nové rozhraní
                        not_enough_popup=Tk()
                        not_enough_popup.title("Receptář")
                        not_enough_popup.iconbitmap("cook.ico")

                        #štítky
                        not_enough_label=Label(not_enough_popup,text="Nemáš dostatek následujících surovin")
                        not_enough_label.grid(row=0,column=0,columnspan=2)
                        counter=1
                        for missing in miss:
                            missing_mass=miss_mass[counter-1]

                            missing_label=Label(not_enough_popup, text=missing)
                            missing_mass_label=Label(not_enough_popup, text=missing_mass)

                            missing_label.grid(row=counter,column=0)
                            missing_mass_label.grid(row=counter,column=1)

                            counter+=1





    
                    if new_mass >= 0:
                        change={"množství":new_mass}
                        search.update(change)
        
        #uloží změny v dostupných ingrediencích
        
        if not_enough == 0:        
            with open ("././/suroviny.json", "w") as file:
                    json.dump(ingrediences, file)
                    
            
        if not_enough >=0:  
            pass
            

        

    counter=0
    for i in recipes:
        recipe_label=Label(root, text=i)
        recipe_label.grid(row=counter,column=0)

        cook_button=Button(root, text="Vařit!", command=lambda i=i:cooking(i))
        cook_button.grid(row=counter,column=1)
        counter=+1



    root.mainloop()
            
