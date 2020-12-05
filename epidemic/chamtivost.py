import random


mince=("panna","orel")
vyhra=0
for i in range (1,100):
    
    vklad=100
    for i in range(1,100):
        strana=random.choice(mince)
        
        if strana =="panna":
            vklad=vklad*1.5
        if strana =="orel":
            vklad=vklad*0.6
        
        
        
    print("celkem",vklad)
    if vklad>=100:
        vyhra=vyhra+1
print(vyhra)
    
        
