from random import randrange
from tkinter import *
#from epidemie_prubeh2 import zalozeni

from PIL import ImageTk, Image
#založení nového setu obyvatel
def zalozeni ():
    citizens=[]
    state={"populace":10000,"roušky":"Ne","rozpočet":100000,"nespokojenost":0,"dezinformace":0,"informovanost":0,"zdravotnictví":100,"karanténa":False,"testování":0,"strach":0,"Zdravotní krize":False,"Laboratoře":0}
    for i in range (0,10000): #vytvoří startovací balíček osob
        jedinec={}
        jedinec["osoba"]=i
        citizens.append(jedinec)
        sance=randrange(0,1000)
        if sance <1: #určí jestli je jedinec nakažený
            jedinec["Nakažený"]=True
            jedinec["Zbyv.delka.nem"]=20
            chance_symptoms=randrange(0,100)
            if chance_symptoms <8:
                jedinec["Symptomy"]="Mírné"
            else:
                jedinec["Symptomy"]="Žádné"
        else:
            jedinec["Nakažený"]=False
            jedinec["Zbyv.delka.nem"]=0
            jedinec["Symptomy"]="Žádné"
        jedinec["Odhalený"]=False
        jedinec["Imunita"]=False
        jedinec["Zbývá imunity"]=0
        jedinec["rouška"]="Ne"
        jedinec["stav"]="Živý"
        #jedinec["stav"]="OK"
        jedinec["karantena"]=False
        #jedinec["dní v kritickém stavu"]=0
        #chtělo by to zařadit zda má nakažený symptomy == přetvořit stav na symptomy - 4 stupně(žádné, mírné, vážné, velmi vážné)
    

    return(citizens,state)
       

#upravuje set obyvatel a určuje kdo se nakazil případně zemřel
def new_day(complet_set):
    set_of_people=complet_set[0]
    set_for_state=complet_set[1]
    mask_for_all=set_for_state["roušky"]
    medical_care=set_for_state["zdravotnictví"]
    test_rate=set_for_state["testování"]
    isolation=set_for_state["karanténa"]

    crisis=set_for_state["Zdravotní krize"]
    print(crisis)
    test_rate=int(test_rate)
    #nutnost přidat infekci z venčí a lockdown města
    risk=60
    for i in set_of_people:
        infected=i["Nakažený"]
        stav=i["stav"]
        symptoms=i["Symptomy"]
        imunity=i["Imunita"]
        if stav == "Živý":
            rest_imunity=i["Zbývá imunity"] #spočítá kolik jedinci zbývá imunity
            if rest_imunity !=0:
                rest_imunity=rest_imunity-1
                new_imunity={"Zbývá imunity": rest_imunity}
                if rest_imunity==0:
                    new_imunity={"Zbývá imunity": rest_imunity, "Imunita":False}
                i.update(new_imunity)
            #zajištění izolace - jedinec se může dát dobrovolně do karantény i když má jen mírné symptomy a zároveň se může dát dobrovolně testovat



            test_chance=randrange(0,100)
            if test_chance <=test_rate and infected==True:
                tested={"testovany":True}
                if isolation == True:
                    isolated={"karantena":True}
                    i.update(isolated)
                #print(tested)
                i.update(tested)
            isolated=i["karantena"]
            uncovered=i["Odhalený"]
            skip=0
            #testování upravit na odhalení - pokud má jedinec symptomy, tak se nechá ochotněji testovat při vyšší informovanosti. Testování bude podkategorie odhalení
            #nevím jak to mám teď, ale člověk ve vážném stavu by měl být vyřazen z možnosti nakazit
            if isolated == True:
                skip=skip+1
            if imunity== True:
                skip=skip+1
            if stav=="Mrtvý":
                skip=skip+1

            if skip==0: #mělo by zajistit, že u pozitivně testovaných dojde k překočení fáze nakažení
                #podle aktuálního nařízení nasadí nebo odloží roušku
                if mask_for_all =="Ano":
                    mask_on={"rouška":"rouška"}
                    i.update(mask_on)
                if mask_for_all =="Ne":
                    mask_on={"rouška":"ne"}
                    i.update(mask_on)

                #ověří si jakou má dotyčný ochranu a upraví risk
        
                masked=i["rouška"]
            
            
        
                if masked=="rouška":
                    risk=5


                numbers=[] #zvolí které obyvatel potkala osoba A kde by mohlo dojít k přenosu
                for e in range(1,4):
                    e=randrange(0,9999)
                    numbers.append(e) #vybere lidi se kterými přišel člověk do rizikového kontaktu
        
                for number in numbers: #pro jednotlivé obyvatele spočítá jestli došlo k nakažení
                    meet=set_of_people[number]
                    meet_infected=meet["Nakažený"]
                    meet_isolated=meet["karantena"]
                    meet_imunity=meet["Imunita"]
                    meet_death=meet["stav"]
                    skip=0
                    if meet_isolated==True:
                        skip=skip+1
                    if meet_imunity==True:
                        skip=skip+1
                    if meet_death =="Mrtvý":
                        skip=skip+1

                    if skip==0:

                        if infected == True and meet_infected == False: #určí jestli došlo k přenosu z osoby A na osobu B
                
                            chance=randrange(0,500)
                            if chance<risk:
                                new_infection={"Nakažený":True,"Zbyv.delka.nem":20}
                                meet.update(new_infection)
                        #zjistí jestli má osoba B roušku
                        meet_mask=meet["rouška"]
                        if meet_mask=="rouška":
                            risk=50

                        if infected == False and meet_infected == True:  #určí jestli došlo k přenosu z osoby B na osobu A 
                
                            chance=randrange(0,500)
                            if chance<risk:
                                new_infection={"Nakažený":True,"Zbyv.delka.nem":20}
                                i.update(new_infection) #u lidí s rizikovým kontaktem podle parametrů zvolí zda byli neby nebyli nakažení
                    else:
                        pass
            else:
                pass

     





            if infected == True: #určí jestli došlo ke zhoršení zdravotního stavu. Jedinec ve vážném stavu se stane izolovaným

                    rest=i["Zbyv.delka.nem"] #odečítá dny nakažení a po uplynutí dané doby se vyléčí
                    rest=rest-1

                    if rest==0 and (symptoms == "Vážné" or symptoms == "Velmi vážné"):
                         health={"Nakažený":False,"Symptomy":"Žádné","Imunita":True,"Zbývá imunity":60,"Zbyv.delka.nem":rest}
                         medical_care=medical_care+1
                         i.update(health)


                    elif rest==0 and (symptoms == "Žádné" or symptoms == "Mírné"):
                        health={"Nakažený":False,"Symptomy":"Žádné","Imunita":True,"Zbývá imunity":60,"Zbyv.delka.nem":rest}
                        i.update(health)

                    else: #pokud se ještě nedoléčil přeskočí se na případné zhrošení stavu
                        new_rest={"Zbyv.delka.nem":rest}
                        i.update(new_rest)

                        symptoms=i["Symptomy"]
                        chance=randrange(0,100)

                        if chance <2 and (symptoms == "Žádné" or symptoms == "Mírné"):
                            new_stav={"Symptomy":"Vážné"}
                            medical_care=medical_care-1
                            i.update(new_stav)


                
       

                        symptoms=i["Symptomy"]
                        if symptoms == "Vážné": #určí zda člověk ve vážném stavu zemřel nebo se jeho stav zlepšil
                                chance=randrange(0,100)
           

                                if crisis==True and chance <20:
                                    new_status={"Symptomy":"Velmi vážné"}
                                    i.update(new_status)

                                if crisis==False and chance <3:
                                    new_status={"Symptomy":"Velmi vážné"}
                                    i.update(new_status)

                                if crisis==True and chance <10:
                                    new_status={"Nakažený":False,"stav":"Mrtvý","Symptomy":"Žádné"}
                                    medical_care=medical_care+1 
                                    i.update(new_status)

                                if chance >75 and stav != "Mrtvý":
                                    new_status={"Symptomy":"Mírné"}
                                    medical_care=medical_care+1
                                    i.update(new_status)

                        if symptoms =="Velmi vážné": #spočítá zda se pacient v kritickém stavu zlepšil nebo umřel
                                chance=randrange(0,100)

                                if crisis == True and chance <30 :
                                    new_status={"Nakažený":False,"stav":"Mrtvý","Symptomy":"Žádné"}
                                    i.update(new_status)
                                    medical_care=medical_care+1

                                if crisis == False and chance <90 :
                                    new_status={"Nakažený":False,"stav":"Mrtvý","Symptomy":"Žádné"}
                                    i.update(new_status)
                                    medical_care=medical_care+1

                                if crisis==False and chance > 60:
                                    new_status={"Symptomy":"Vážné"}
                                    i.update(new_status)

                                if crisis==True and chance >98:
                                    new_status={"Symptomy":"Vážné"}
                                    i.update(new_status)
    
    MC={"zdravotnictví":medical_care}
    print(MC,"medical")
    set_for_state.update(MC)
    #m1=set_of_people[100]
    #m2=set_of_people[300]
    #m3=set_of_people[500]
    #m4=set_of_people[800]
    #m5=set_of_people[900]
    #print(m1)
    #print(m2)
    #print(m3)
    #print(m4)
    #print(m5)
    return(complet_set)

