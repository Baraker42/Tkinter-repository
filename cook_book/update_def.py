from tkinter import *
from tkinter import messagebox
import json

#spustí se v případě že ještě nexistuje soubor s recepty
def no_recipe():
    
    root =Tk()
    root.title("Receptar")
    root.iconbitmap("cook.ico")
    #založí štítek a tlačítko
    warning_label=Label(root,text="Zatím nebyl vložený žádný recept")
    close_button=Button(root,text="Zavřít",command=root.destroy)

    #vypíše štítek a tlačítko
    warning_label.pack()
    close_button.pack()

    root.mainloop()

#hlavní funkce tohoto modulu. Větví se na řadu dalších funkcí a v tuto chvíli je to poměrně nepřehledně řešené
def recipe_update(recepies):
    
    #základní rozhraní
    root1 =Tk()
    root1.title("Receptar")
    root1.iconbitmap("cook.ico")

    info_label=Label(root1, text="V tomto rozhraní můžete upravovat již vložené recepty")
    info_label.grid(row=0,column=0,columnspan=2)
    
 

        #provádí změny ve zvolených surovinách
    def change_mod(this_one,change_ingredience,change_mass,change_unit,chosen):
        for i in chosen:
            if i["surovina"]==this_one:
                all_change={"surovina":change_ingredience,"množství":change_mass,"jednotka":change_unit}
                i.update(all_change)
        #uloží změny do souboru
        with open ("././/recepty.json", "w") as file:
            json.dump(recepies, file)
    
    #funkce pro zvolení receptu k úpravě
    def recipe_mod(chosen,chose_ingredience):
        root =Tk()
        root.title("Receptar")
        root.iconbitmap("cook.ico")
        print("recipe mod",chosen)

        for i in chosen:
            chosen_one=i["surovina"]
            if chosen_one == chose_ingredience:
                chose_ing=i["surovina"]
                chose_mass=i["množství"]
                chose_unit=i["jednotka"]

                ingredience_label=Label(root, text="surovina")
                change_ingredience_entry=Entry(root, width = 15, borderwidth=5)
                ingredience_label.grid(row=0,column=0)
                change_ingredience_entry.grid(row=0,column=1)
                change_ingredience_entry.insert(0,chose_ing)

                mass_label=Label(root, text="množství")
                change_mass_entry=Entry(root, width = 10, borderwidth=5)
                mass_label.grid(row=0,column=2)
                change_mass_entry.grid(row=0,column=3)
                change_mass_entry.insert(0,chose_mass)

                unit_label=Label(root, text="jednotka")
                change_unit_entry=Entry(root, width=5, borderwidth=5)
                unit_label.grid(row=0,column=4)
                change_unit_entry.grid(row=0,column=5)
                change_unit_entry.insert(0,chose_unit)

                this_one=chosen_one

            change_button=Button(root, text="Změnit", command=lambda: change_mod(this_one,change_ingredience_entry.get(),change_mass_entry.get(),change_unit_entry.get(),chosen))
            change_button.grid(row=0,column=6)

        root.mainloop()


    #uloží změnu názvu (bohužel v současné době musí přepsat celý soubor a znovu uložit)
    

        #slouží ke změně názvu receptu 
    
 
        
        #uloží přidanou surovinu
        #přepsat aby se vypsalo všechno znovu
    
    #funkce, která vypíše název receptu a všechny suroviny s možností úpravy
    def print_recept(i):

        def name_mod(name):
            root =Tk()
            root.title("Receptar")
            root.iconbitmap("cook.ico")

            old_name_label=Label(root,text="původní název receptu")
            old_name_label.grid(row=0,column=0)

            old_name_show=Label(root, text=name)
            old_name_show.grid(row=0,column=1)

            new_name_label=Label(root, text="nový název receptu")
            new_name_label.grid(row=1, column=0)

            new_name_entry=Entry(root, width = 15, borderwidth=5)
            new_name_entry.grid(row=1,column=1)
        
                #uložení provedené změny spustí funkci save_name
            def save_name(new_name,name):
                new_one=(recepies[name])
                finalization={}
        

                    #Zapíše všechny recepty do složky, kromě receptu, který se přejmenovává
                for i in recepies:
            
                    if i != name:
                        rewrite=(recepies[i])
                        finalization[i]=rewrite
                    else:
                        finalization[new_name]=new_one
            
        

                       
                    #uloží upravený název receptu
                    with open ("././/recepty.json", "w") as file:
                        json.dump(finalization, file)

                    root.destroy()
                    root2.destroy()
                    root1.destroy()
                    
                    recipe_update(finalization)

            save_button=Button(root, text="Uložit změnu", command=lambda:save_name(new_name_entry.get(),name))
            save_button.grid(row=2,column=1)
            print(name)

            root.mainloop()


        def save_ingredience (name,chosen,added_ingredience,added_quantity,added_unit):

                new_entry={"surovina":added_ingredience,"množství":added_quantity,"jednotka":added_unit}
                chosen.append(new_entry)
            
                with open ("././/recepty.json", "w") as file:
                    json.dump(recepies, file)
      #ukončí rozhraní a spustí ho znovu s novými zdrojovými daty
                root2.destroy()
                print_recept(name)
        
        #vymaže zvolenou surovinu
        def delete_mode(name,chosen, chosen_ingr):
            
            new_chosen=[]
            for i in chosen:
                if i["surovina"] != chosen_ingr:
                    new_chosen.append(i)

            finalization={}
            
            
            for i in recepies:
                new_name=i
                if name != new_name:
                    rewrite=(recepies[i])
                    finalization[i]=rewrite
                else:
                    
                    finalization[name]=new_chosen
            
            
            recepies.update(finalization)
            with open ("././/recepty.json", "w") as file:
                json.dump(recepies, file)

                root2.destroy()
            
                print_recept(name)
           

            
#funkce, která přidá řádek, který umožní přidávat další ingredience do existujícího receptu
        def add_ingredience(chosen,counter):

            global add_ingredience_label
            global add_quantity_label
            global add_unit_label
            add_ingredience_label=Label(root2, text="nová surovina")
            add_quantity_label=Label(root2,text="množství")
            add_unit_label=Label(root2, text="jednotka")

            #přidá konzole na přidání nové suroviny
            global add_ingredience_entry
            global add_quantity_entry
            global add_unit_entry
            add_ingredience_entry=Entry(root2, width = 15, borderwidth=5)
            add_quantity_entry=Entry(root2, width = 10, borderwidth=5)
            add_unit_entry=Entry(root2, width = 5, borderwidth=5)

            

            add_ingredience_label.grid(row=counter,column=0)
            add_quantity_label.grid(row=counter,column=2)
            add_unit_label.grid(row=counter,column=4)
            
            add_ingredience_entry.grid(row=counter,column=1)
            add_quantity_entry.grid(row=counter,column=3)
            add_unit_entry.grid(row=counter,column=5)

            #tlačítko, které spustí funkci na uložení ingredeince
            global save_button
            save_button=Button(root2, text="Uložit do receptu",command=lambda:save_ingredience(name,chosen,add_ingredience_entry.get(),add_quantity_entry.get(),add_unit_entry.get()))
            save_button.grid(row=counter, column=6)
            
            counter=counter+1
            global add_ingredience_button
            add_ingredience_button.grid_forget()
            
            add_ingredience_button=Button(root2, text="Přidat další",command=lambda:add_ingredience(chosen,counter))
            add_ingredience_button.grid(row=counter,column=6)

        root2 =Tk()
        root2.title("Receptar")
        root2.iconbitmap("cook.ico")
        name=i
        print(type(i),"vypíše typ i")

        #vypíše název receptu
        chosen_label=Label(root2, text=i)
        chosen_label.grid(row=0,column=0)
        chosen_mod_button=Button(root2, text="Upravit",command=lambda:name_mod(name))
        chosen_mod_button.grid(row=0,column=6)

        #for loop postupně vypíše všechny informace o receptu
        rec_counter=1
        chosen=recepies[i]

        for i in chosen:
            print (i["surovina"])
            chosen_ingr=i["surovina"]
            chosen_quant=i["množství"]
            chosen_unit=i["jednotka"]



            chosen_label_ingr=Label(root2, text=chosen_ingr)
            chosen_label_ingr.grid(row=rec_counter,column=1)
            

            chosen_label_quant=Label(root2, text=chosen_quant)
            chosen_label_quant.grid(row=rec_counter,column=3)

            chosen_label_unit=Label(root2, text=chosen_unit)
            chosen_label_unit.grid(row=rec_counter,column=5)

            chosen_button=Button(root2, text="Upravit",command=lambda chosen_ingr=chosen_ingr : recipe_mod(chosen,chosen_ingr))
            chosen_button.grid(row=rec_counter,column=6)

            delete_ingredience_button=Button(root2, text="X",command=lambda chosen_ingr=chosen_ingr :delete_mode(name,chosen, chosen_ingr))
            delete_ingredience_button.grid(row=rec_counter,column=7)

            rec_counter=rec_counter+1

            #bude odkazovat na funkci, která přidá do receptu další suroviny
        global add_ingredience_button
        add_ingredience_button=Button(root2, text="Přidat další",command=lambda:add_ingredience(chosen,rec_counter))
        add_ingredience_button.grid(row=rec_counter,column=6)

        root2.mainloop()

    #funkce na smazání zvoleného receptu
    def delete_recept(i):
        #ujistí se zda uživatel chce skutečně recept vymazat
        asking=messagebox.askquestion("Smazat recept",f"Vážně chcete recept {i} vymazat?")
        if asking == "yes":
            #vytvoří nový seznam, do kterého nevloží položku které se to týká
            new_recepies={}
            for recipe in recepies:
                if recipe != i:
                    rewrite=recepies[recipe]
                    new_recepies[recipe]=rewrite

            #uloží nový seznam receptů
            with open ("././/recepty.json", "w") as file:
                json.dump(new_recepies, file)

            root1.destroy()
        
            recipe_update(new_recepies)
        else:
            pass

        

    #for loop vypíše všechny recepty s možností úpravy    
    counter=1
    for i in recepies:
        recipe_label=Label(root1, text=i)
        recipe_label.grid(row=counter, column=0)
        recipe_button=Button(root1, text="Upravit", command=lambda i=i:print_recept(i))
        recipe_button.grid(row=counter,column=1)
        recipe_delete=Button(root1, text="X", command=lambda i=i:delete_recept(i))
        recipe_delete.grid(row=counter,column=2)
        counter=counter+1
    
 

    root1.mainloop()
