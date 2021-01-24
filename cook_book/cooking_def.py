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
        for i in recipe:
            want_ingredience=i["surovina"]
            want_mass=i["množství"]
            #s jednotkami bude asi problém, zatím bych je rád zachoval, protože mi přijdou celkem důležité, minimálně vizuálně
            want_unit=i["jednotka"]

            #vyhledá surovinu z receptu v ingrediencích a následně odečte potřebné množství - zatím neumí pracovat s tím,
            #když se dostane do mínusu, ale to se postupně doplní
            for search in ingrediences:
                if search["surovina"]==want_ingredience:
                    new_mass=int(search["množství"])-int(want_mass)
                    change={"množství":new_mass}
                    search.update(change)

        #uloží změny v dostupných ingrediencích        
        with open ("././/suroviny.json", "w") as file:
                json.dump(ingrediences, file)      
        
            

        

    counter=0
    for i in recipes:
        recipe_label=Label(root, text=i)
        recipe_label.grid(row=counter,column=0)

        cook_button=Button(root, text="Vařit!", command=lambda i=i:cooking(i))
        cook_button.grid(row=counter,column=1)
        counter=+1



    root.mainloop()
            
