import linecache
from random import randint as rand
from Statek import *
class Flota:
    def __init__(self):
        self.flota_1=[] ; self.dodadkowa_1=[] ; self.zniszczone_1=[]
        self.flota_2=[] ; self.dodadkowa_2=[] ; self.zniszczone_2=[]
        for i in range(2,15):
            wiersz = linecache.getline('flota_1.txt', i)
            if int(wiersz.split()[1])!=0:                                                         
                for a in range(int(wiersz.split()[1])): 
                    self.flota_1.append(Statek(wiersz.split()[0]))
        for i in range(2,15):
            wiersz = linecache.getline('flota_2.txt', i)
            if int(wiersz.split()[1])!=0: 
                for a in range(int(wiersz.split()[1])): 
                    self.flota_2.append(Statek(wiersz.split()[0]))
        print('Bitwa', j)
        print('Stan flot na poczatek bitwy:')
        print('Flota1 ma statkow: ',len(self.flota_1),'Flota2 ma statkow: ',len(self.flota_2))
        
        
    def rozgrywka(self):
        """
        for obsługuje strzały z floty 1 do floty 2 i sprawdzane jest czy zyskują kolejny strzał,
        jeśli tak to dodawane są do listy dodatkowych strzałów floty 1.
        while obsługuje dodatkowe strzały floty 1 
        """
        
        for i in range(0,len(self.flota_1)):
            losowa = rand(0,len(self.flota_2)-1)
            wynik=self.flota_1[i].attack(self.flota_2[losowa])
            if wynik==True and self.zniszczone_2.count(losowa)==0:
                self.zniszczone_2.append(losowa)
            elif wynik==False and self.dodadkowa_1.count(losowa)==0:
                self.dodadkowa_1.append(i)
                
        while len(self.dodadkowa_1)>0:
            losowa = rand(0,len(self.flota_2)-1)
            wynik=self.flota_1[self.dodadkowa_1[0]].attack(self.flota_2[losowa])
            aktualna=self.dodadkowa_1[0]
            self.dodadkowa_1.pop(0)
            if wynik==True and self.zniszczone_2.count(losowa)==0:
                self.zniszczone_2.append(losowa)
            elif wynik==False and self.dodadkowa_1.count(losowa)==0:
                self.dodadkowa_1.append(aktualna)
        """
        for obsługuje strzały z floty 1 do floty 2 i sprawdzane jest czy zyskują kolejny strzał,
        jeśli tak to dodawane są do listy dodatkowych strzałów floty 1.
        while obsługuje dodatkowe strzały floty 1 
        """
        for i in range(0,len(self.flota_2)):
            losowa = rand(0,len(self.flota_1)-1)
            wynik=self.flota_2[i].attack(self.flota_1[losowa])
            if wynik==True and self.zniszczone_1.count(losowa)==0:
                self.zniszczone_1.append(losowa)
            elif wynik==False and self.dodadkowa_2.count(losowa)==0:
                self.dodadkowa_2.append(i)
        
        while len(self.dodadkowa_2)>0:
            losowa = rand(0,len(self.flota_1)-1)
            wynik=self.flota_2[self.dodadkowa_2[0]].attack(self.flota_1[losowa])
            aktualna=self.dodadkowa_2[0]
            self.dodadkowa_2.pop(0)
            if wynik==True and self.zniszczone_1.count(losowa)==0:
                self.zniszczone_1.append(losowa)
            elif wynik==False and self.dodadkowa_2.count(losowa)==0:
                self.dodadkowa_2.append(aktualna)
        return self.usuwanie()
        
    def usuwanie(self):
        """Funkcja odpowiedzialna za usuwanie zniszczonych statków"""
        self.zniszczone_1.sort() ; self.zniszczone_2.sort()
        
        while len(self.zniszczone_1) !=0:
            self.flota_1.pop(self.zniszczone_1[-1])
            self.zniszczone_1.pop(-1)
            
        while len(self.zniszczone_2) !=0:
            self.flota_2.pop(self.zniszczone_2[-1])
            self.zniszczone_2.pop(-1)
        return self.zwyciezca()
    
    def odnowa_oslony(self):
        """Funkcja odpowiedzialna za odbudowe osłon"""
        for i in range(len(self.flota_1)):
            self.flota_1[i].odnowa()
        for i in range(len(self.flota_2)):
            self.flota_2[i].odnowa()
            
    def zwyciezca(self):
        """Funkcja sprawdzająca kto wygrał
        1 - gdy wygrała pierwsza flota,
        2 - gdy wygrała druga flota,
        3 - gdy był remis
        """
        if len(self.flota_1)==0: return 2
        elif len(self.flota_2)==0: return 1
        else: 
            self.odnowa_oslony()
            return 3
        
    def wyswietl(self):
        """Funkcja wyświetlająca ilość statków w flocie"""
        print('Flota1 ma statkow: ',len(self.flota_1),'Flota2 ma statkow: ',len(self.flota_2))
        
f1=0;f2=0
for j in range(1,11):       
    f=Flota()
    runda=1
    #print(j)
    for i in range(1,6):
        #print('Runda: ',i)
        f.rozgrywka()
        if f.zwyciezca()==1:
            f1 += 1
            break
        elif f.zwyciezca()==2:
            f2 += 1
            break
        elif (f.zwyciezca()==3 and i==6):
            f1 += 1
            f2 += 1
            break
    print('Stan flot na koniec bitwy:')
    f.wyswietl() 
    print('~~~~~~~~~~~~~~~~~~~~~~')
if(f1<f2):
    print('Wygrywa flota2 stosunkiem', f1 , 'do', f2 , 'wygranych bitew.')
if(f2<f1):
    print('Wygrywa flota1 stosunkiem', f2 , 'do', f1 , 'wygranych bitew.')
if(f1==f2):
    print('Mamy remis')