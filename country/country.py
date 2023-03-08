from OmaMoodul import *
sõnastik={}
while True:
    v=int(input("1-välju.\n2-Salvestame failisse\n3-loeme failist\n4-Vaata sõnastiku\n5-Näita riigi ja tema pealinna\n6-Paranda viga sõnastikus\n7-Test"))
    if v==1:
        break
    if v==2:
        Kirjuta_failisse('Europa_Riigid.txt')
    elif v==3:  
        sõnastik=Loe_failist('Europa_Riigid.txt')
    elif v==4:
        vaata_sõnastiku('Europa_Riigid.txt')
    elif v==5:
       RP_find('Europa_Riigid.txt')
    elif v==6:
        paranda('Europa_Riigid.txt')