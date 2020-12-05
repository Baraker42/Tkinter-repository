
from tkinter import *
from epidemie_prubeh_final import *
from PIL import ImageTk
from PIL import Image

#Tento skript funguje jako funkce ve funkci. Vykreslí rozhraní, ve kterém se provádí jednotlivé změny
#testování musí být trochu komplikovanější. Než bude možnost testovat všechny obyvatele
#bude třeba vytvořit testovací metodu a "vybudovat" testovací centra.
#každé cetrum umožní za den otestovat určitý počet obyvatel
def faze_2(starosta,virus):
    root = Tk()
    
    
    complet_set=zalozeni()#založí náhodný set obyvatel
    set_of_people=complet_set[0]
    set_for_state=complet_set[1]
    
    
    global labs 
    labs=set_for_state["Laboratoře"]
    global progress
    progress = 0

    def change_budget(budget):
        global budget_label
        budget_label.grid_forget()
        budget_label=Label(root,fg="green", text=(f"Rozpočet: {budget}"), font=("Helvetica",9,"bold"))
        budget_label.grid(row=1,column=4,columnspan=2)
  

    def health_interface (complet_set):#rozhraní v rámci kterého půjde upravovat kolik testů může být provedeno
        global lab_image
    
        lab_image=(ImageTk.PhotoImage(Image.open("lab_icon_small.png")))
        root=Toplevel()
        root.title("Epidemic The Game")
        root.iconbitmap("vir.ico")
        set_of_people=complet_set[0]
        global set_for_state
        set_for_state=complet_set[1]
        medical_care=set_for_state["zdravotnictví"]
      
        def testing(testing_entry): #testovací funkce - hráč zvolí kolik procent osob z celkové populace se zvládne otestovat
            print(type(testing_entry))
            try:
                number=int(testing_entry)
                new_percentil={"testování":number}
                set_for_state.update(new_percentil)
               
                

                #VYTVOŘIT mezi vpisovací konzoli a testovat napíše kolik bude dané testování denně stát
            except ValueError:
                #VYTVOŘIT okno, které bude upozorňovat na to, že danou akci nejde provést (možná univerzání, aby s edalo použít i v jiných případech
                pass
            
        def lab(day):
        #uprava budgetu, pždy před výpočtem si musí nechat vypsat aktuální rozpočet
            #provede výpočty
            global labs
            global budget
            labs=labs+1
            print(progress)
            
            
            budget=budget-50000
            change_budget(budget)
            
            
          
            


        
            #vytvoří štítky
            lab_label=Label(root,image=lab_image)
            lab_1_label=Label(root,text=(f"Laboratoř 1 - {progress} %"))
        
       

            #umístí štítky
            lab_label.grid(row=1,column=1)
            lab_1_label.grid(row=2,column=1)
        
        

            #aktualizuje data
            new_budget={"Laboratoře":labs,"rozpočet":budget}
            set_for_state.update(new_budget)

            

        def space(medical_care): #rozšiřuje kapacitu lůžek pro pacienty
            medical_care=set_for_state["zdravotnictví"]
            medical_care=medical_care+100
            global budget
            budget=budget-10000
            change_budget(budget)
            new_medical_care={"zdravotnictví":medical_care}
            medical_care_label=Label(root, text=(f"Kapacita zdravotnictví: {medical_care}"))
            medical_care_label.grid(row=0,column=1)
            set_for_state.update(new_medical_care)
            increse_capacity_button = Button(root, text="Koupit 100 lůžek", command=lambda:space(medical_care))
            increse_capacity_button.grid(row=0,column=2)

        
        
        budget=set_for_state["rozpočet"]
        
        print(labs)
        if labs == 1: #vykleslí obrázek když už byla laboratoř dříve postavená
            lab_label=Label(root,image=lab_image)
            lab_1_label=Label(root,text=(f"Laboratoř 1 - {progress} %"))

            lab_label.grid(row=1,column=1)
            lab_1_label.grid(row=2,column=1)
        test_rate=set_for_state["testování"]
        print(test_rate,"tolik se testuje")
        if progress == 100: #stavění laboratoře - pokud progress dosáhne 100, laboratoř je funkční a zprovozní se testování
            testing_entry=Entry(root,width = 5)

            test_button = Button(root, text="Testovat",command=lambda:testing(testing_entry.get()))
            #VYTVOŘIT label na popis konzole "aktuální počet testů
            #VYTVOŘIT label popisující kolik testů je v tuto chvíli možné dělat
            testing_entry.grid(row=4,column=2)
            test_button.grid(row=5,column=2)
            testing_entry.insert(0,test_rate)

        medical_care_label=Label(root, text=(f"Kapacita zdravotnictví: {medical_care}"))

        build_lab_button = Button(root, text="Postavit laboratoř",command=lambda:lab(day))
        price_of_lab_label = Label(root, text="(-50 000)")
        increse_capacity_button = Button(root, text="Koupit 100 lůžek", command=lambda:space(medical_care))
        price_of_capacity_label = Label(root, text="(-10 000)")
        exit_button = Button(root, text="Zavřít", command=root.destroy)

        medical_care_label.grid(row=0,column=1)
        increse_capacity_button.grid(row=0,column=2)
        price_of_capacity_label.grid(row=1,column=2)
        build_lab_button.grid(row=3,column=1)
        price_of_lab_label.grid(row=4,column=1)
        exit_button.grid(row=5,column=1)


        root.mainloop()

    def help_interface():
        root = Toplevel()
        root.title("Epidemic The Game") 
        root.iconbitmap("vir.ico")
       
        help_label = Label(root, text="Na tlačítku se pracuje")
        construction_img = (ImageTk.PhotoImage(Image.open("under_construction.jpg")))
        img_label = Label(root, image=construction_img)
        exit_button = Button(root, text="Zavřít napovědu", command=root.destroy)
        img_label.pack()
        help_label.pack()
        exit_button.pack()
        root.mainloop()
        
        
        
        exit_button.pack()
        root.mainloop()
    
    

    
   
    #uloží potřebné proměné
    mask_status=set_for_state["roušky"]
    population=set_for_state["populace"]
    global budget
    budget=set_for_state["rozpočet"]
    dissatisfaction=set_for_state["nespokojenost"]
    disinformation=set_for_state["dezinformace"]
    information=set_for_state["informovanost"]
    medical_care=set_for_state["zdravotnictví"]
    fear=set_for_state["strach"]
    global day
    day=1
    global pozor
    pozor=0

    root.title("Epidemic The Game")
    root.iconbitmap("vir.ico")

   

    def health_crisis():
       
        root=Toplevel()
        root.title("Epidemic The Game")
        root.iconbitmap("vir.ico")

        warning_image=(ImageTk.PhotoImage(Image.open("warning_small.png")))
        warning_label=Label(root, image=warning_image)
        atention_label=Label(root, fg="red", text="Pozor! Kapacity zdravotnictví jsou přeplněné! Zvýšené riziko úmrtí!",font=("Helvetica",13,"bold"))
        exit_button=Button(root, text="Zavřít", command=root.destroy)
        
        warning_label.pack()
        atention_label.pack()
        exit_button.pack()

        
        root.mainloop()

    
    #sputí další den a provede výpočty 
    def dalsi_den():
        global budget_label
        global population_label
        budget_label.grid_forget() #sláva vymaže se to co potřebuju
        population_label.grid_forget()
        print ("laboratoře", labs)
        #stavba laboratoře
        if labs == 1:
            global progress
            if progress < 100:
                progress=progress+50
            
        

        #print(set_for_state)
        #print(new_tests)
        deamon=new_day(complet_set)
        people=deamon[0]
        state=deamon[1]
        population=state["populace"]
        test_rate=state["testování"]
        print("testování",test_rate)
        #spočítá počet obyvatel s uritými vlastnostmi
        ill_people=[]
        dead_people=[]
        
        for i in people:
            e=i["Nakažený"]
            d=i["stav"]
           
            ill_people.append(e) 
            dead_people.append(d)
            
        dead=dead_people.count("Mrtvý")
        infected=ill_people.count(True)
        new_population=population-dead
        
       
        print(infected)

        
        
        

        #změny v rozpočtu
        mask_status=state["roušky"]
        if mask_status == "Ano":
            cost = 5000
        if mask_status == "Ne":
            cost= 0
        budget=state["rozpočet"]
        budget=budget-cost
        new_budget={"rozpočet":budget}
        state.update(new_budget)


        
        print(infected)
        global day
        
        day=day+1

        #změní údaje na štítcích na základě provedených výpočtů
        
        
        

        budget_label=Label(root,fg="green", text=(f"Rozpočet: {budget}"), font=("Helvetica",9,"bold"))
        
        population_label=Label(root, text=(f"Počet obyvatel: {new_population}"), font=("Helvetica",9,"bold"))
        
        numbers_of_infected=Label(root,fg="orange", text=(f"Nakažení: {infected}"),font=("Helvetica",9,"bold"))
        number_of_dead=Label(root,fg="red", text=(f"Zemřelý: {dead}"),font=("Helvetica",9,"bold"))

        day_label=Label(root,text=(f"Den: {day}"))

        #vypíše aktualizované údaje
        budget_label.grid(row=1,column=4,columnspan=2)
        
        numbers_of_infected.grid(row=2,column=2,columnspan=2)
        number_of_dead.grid(row=2,column=4)
        population_label.grid(row=2,column=1)
        
        day_label.grid(row=5,column=5)

        #zjistí změny ve zdravotnictví
        medical_press=state["zdravotnictví"]
        #global pozor
        #print("alert",pozor)
        
        
        if medical_press <=0:
            crisis={"Zdravotní krize":True}
            set_for_state.update(crisis)
            global pozor
            pozor=pozor+1
            if pozor <=1:
                health_crisis()
            
           

        if medical_press >=0:
            crisis={"Zdravotní krize":False}
            set_for_state.update(crisis)
            pozor = 0
            print(pozor)
            

        
    
    #pomocí tlačítka roušky, přepisuje jestli jsou roušky aktivní nebo ne
    def masks():
        mask_status=set_for_state["roušky"]
        
        if mask_status == "Ne":
            new_mask={"roušky":"Ano"}
        if mask_status =="Ano":
            new_mask={"roušky":"Ne"}
        set_for_state.update(new_mask)
        mask_status=set_for_state["roušky"]
        mask_label=Label(root,text=mask_status)
        mask_label.grid(row=6,column=0)
        #bez roušek trvalo nakazit všechny kolem 20 dní s v průměru o 10 dní déle

    def quarantine(): #vypínání a zapínání karantény
        isolation=set_for_state["karanténa"]
        
        if isolation==False:
            quarantine_button=Button(root,text=("Karanténa ON"),padx=16,command=quarantine)
            quarantine_button.grid_forget()
            quarantine_button.grid(row=6,column=1)
            new_isolation={"karanténa":True}
            set_for_state.update(new_isolation)
        if isolation==True:
            quarantine_button=Button(root,text=("Karanténa OFF"),padx=15,command=quarantine)
            quarantine_button.grid_forget()
            quarantine_button.grid(row=6,column=1)
            new_isolation={"karanténa":False}
            set_for_state.update(new_isolation)
        return


  
        

            
    #provede prvotní výpočty pro štítky na základě nového setu    
    ill_people=[]
    dead_people=[]
    for i in set_of_people:
        e=i["Nakažený"]
        d=i["stav"]
        ill_people.append(e) 
        dead_people.append(d)
    dead=dead_people.count("Mrtvý")
    infected=ill_people.count(True)
    print(infected)
    
   
    #Definice jednotlivých štítků a tlačítek
    global population_label
    global budget_label
    population_label=Label(root, text=(f"Počet obyvatel: {population}"), font=("Helvetica",9,"bold"))
    name_virus=Label(root,text="Virus: " + virus, font=("Helvetica",9,"bold"))
    
    budget_label=Label(root,fg="green", text=(f"Rozpočet: {budget}"), font=("Helvetica",9,"bold"))
    dissatisfaction_label=Label(root, text=(f"Nespokojenost: {dissatisfaction}"))
    disinformation_label=Label(root, text=(f"Dezinformace: {disinformation}"))
    information_label=Label(root, text=(f"Informovanost: {information}"))
    fear_label=Label(root,text=(f"Strach: {fear}"))
    medical_care_label=Label(root, text=(f"Kapacita zdravotnictví: {medical_care}"))
    empty_label=Label(root,text="")
    name_player=Label(root,text="Jméno: " + starosta, font=("Helvetica",9,"bold"))
    numbers_of_infected=Label(root,fg="orange", text=(f"Nakažení: {infected}"),font=("Helvetica",9,"bold"))
    number_of_dead=Label(root,fg="red", text=(f"Zemřelý: {dead}"),font=("Helvetica",9,"bold"))
    mask_label=Label(root,text=mask_status)
    day_label=Label(root,text=(f"Den: {day}"))
    
    health_button=Button(root,text="Zdravotnictví",command=lambda:health_interface(complet_set))
    quarantine_button=Button(root,text=("Karanténa OFF"),padx=15,command=quarantine)
    
    
   
    next_day_button= Button(root, text ="Další den", command=dalsi_den)
    mask_button=Button(root, text="Roušky", command=masks)
    help_button=Button(root, text="?", command=help_interface)
    
    #vykreslí štítky a tlačítka do rozhraní
    #1. řádek
    help_button.grid(row=0,column=6)

    #2.řádek
    name_player.grid(row=1,column=0,columnspan=2)
    
    name_virus.grid(row=1,column=2,columnspan=2)
 
    budget_label.grid(row=1,column=4,columnspan=2)
    

    #3.řádek
    population_label.grid(row=2,column=1)
    
    numbers_of_infected.grid(row=2,column=2,columnspan=2)
    
    number_of_dead.grid(row=2,column=4)

    #4.řádek
    #empty_label.grid(row=3,column=0)
    dissatisfaction_label.grid(row=3,column=0)
   
    disinformation_label.grid(row=3,column=1)
    
    information_label.grid(row=3, column=2)
    
    fear_label.grid(row=3,column=4)

    empty_label.grid(row=4,column=0)

    #4.řádek
   
    mask_button.grid(row=5,column=0)
    health_button.grid(row=5,column=1)
    
    day_label.grid(row=5,column=5)

    
    quarantine_button.grid(row=6,column=1)
    mask_label.grid(row=6,column=0)
    next_day_button.grid(row=6,column=5)
    
    root.mainloop()
