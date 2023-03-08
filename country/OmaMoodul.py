from random import *

sõnastik={}

def Kirjuta_failisse(fail:dict):
    '''
    sisetab failise
    '''
    file=open(fail,'r',encoding='utf-8-sig')
    for line in file:
        k, v=line.strip().split('-')
        sõnastik[k.strip()] = v.strip()    
    riik=input('Lisa riik: ')
    pealinn=input('Tema pealinn: ')
    sõnastik.update({riik:pealinn})
    file.close()
    print(sõnastik)
    return sõnastik

def Loe_failist(fail:dict):
    '''
    loeb failist
    '''
    file=open(fail,'r',encoding='utf-8-sig')
    for line in file:
        k, v=line.strip().split('-')
    file.close()
    print(sõnastik)

def vaata_sõnastiku(fail:dict):
    r={}
    p={}
    file=open(fail,'r',encoding='utf-8-sig')
    for line in file:
        k, v=line.strip().split('-')       
        r[k]=v
        p[v]=k
    file.close()
    print(r, p)   
    return r, p

def RP_find(fail:dict):
    file=open('Europa_Riigid.txt','r',encoding='utf-8-sig')
    for line in file:
        k, v=line.strip().split('-')
        sõnastik[k.strip()] = v.strip()
    file.close()
    Riigid = list(sõnastik.keys())
    Pealinnad = list(sõnastik.values())
    RvP=input('Otsime riik või pealinn: ')
    while RvP not in ["riik","pealinn"]:
        RvP=input('riik või pealinn: ')
    if RvP=='riik':
        OtsimeR=input('Kirjuta riigi nimi: ')
        while OtsimeR not in Riigid:
            OtsimeR=input('Kirjuta riigi õigesti: ')
        num1=Riigid.index(OtsimeR)
        if OtsimeR == Riigid[num1]:
            print(OtsimeR,Pealinnad[num1])
    elif RvP=='pealinn':
        OtsimeP=input('Kirjuta pealinna nimi: ')
        while OtsimeP not in Pealinnad:
            OtsimeP=input('Kirjuta riigi õigesti: ')
        num1=Pealinnad.index(OtsimeP)
        if OtsimeP == Pealinnad[num1]:
            print(OtsimeP,'-',Riigid[num1])
          

def paranda(fail: dict):
    f=open(fail, 'w', encoding='utf-8-sig')
    for line in file:
        k, v = line.strip().split('-')
        sõnastik[k.strip()] = v.strip()

    while True:
        riik_või_pealinn = input('Kas soovite muuta riigi nime või pealinna nime? (r/p): ').lower()
        if riik_või_pealinn not in ['r', 'p']:
            print('Palun sisestage "r" või "p".')
        else:
            break
    
    if riik_või_pealinn == 'r':
        Rparanda = input('Millist riigi soovite parandada? ')
        while Rparanda not in sõnastik:
            Rparanda = input('Kirjutage õige riigi nimi: ')

        Rparandatud = input('Kirjutage parandatud riigi nimi: ')
        while not Rparandatud.isalpha():
            Rparandatud = input('Kirjutage riigi nimi: ')

        sõnastik[Rparandatud] = sõnastik.pop(Rparanda)

    else:
        Pparanda = input('Millist pealinna soovite parandada? ')
        while Pparanda not in sõnastik.values():
            Pparanda = input('Kirjutage õige pealinna nimi: ')

        Pparandatud = input('Kirjutage parandatud pealinna nimi: ')
        while not Pparandatud.isalpha():
            Pparandatud = input('Kirjutage pealinna nimi: ')

        for key, value in sõnastik.items():
            if value == Pparanda:
                sõnastik[key] = Pparandatud
                break
    
    f=open(fail, 'w', encoding='utf-8-sig')
    for key, value in sõnastik.items():
        f.write(f'{key}-{value}\n')
    print(sõnastik)


#def test(fail:dict):
#    a=[]
#    vale=õige=0
#    game=[]
#    file=open('Europa_Riigid','r',encoding='utf-8-sig')
#    for line in file:
#        k, v=line.strip().split('-')
#        sõnastik[k.strip()] = v.strip()
#    file.close()
#    Riigid = list(sõnastik.keys())
#    Pealinnad = list(sõnastik.values())