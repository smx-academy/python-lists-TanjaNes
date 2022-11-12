"""
1.Da se napravi programa vo koja korisnikot ke moze da vnese 10 broevi, 
da se dodadat vo list i da se soberat site broevi vo listata"""
lista=[]
for i in range(10):
    x=int(input('vnesi broj: '))
    lista.append(x)
print(lista)
zbir=0
for i in lista:
    zbir+=i 
print(zbir) 

"""2.Da se napravi programa vo koja korisntikot ke moze da vnese proizvolen 
broj na broevi, da se dodadt vo lista i da se najde najgolemiot broj"""

rng=int(input('vnesi br. na elementi '))
lista=[]
for i in range(rng):
    x=int(input('vnesi br. '))
    lista.append(x)
print('lista: ', lista)
lista.sort()
print('sorted', lista)
print('najgolem br.: ', lista[-1])



"""3. Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na 
elementi, da se ispecati listata i korisnikot da moze da izbere kolku 
elementi i koi elementi ke gi izbrise"""

lst=[]
while True:
    x=input('vnesi broj ili k za kraj: ')
    if x=='k':
        break
    else:
        x=int(x)
        lst.append(x)
print('lista: ', lst)
brbr=int(input('kolku elementi sakas da izbrises? '))
for i in range(brbr):
    brsnj=int(input('koj broj ke go trgnes? '))
    lst.remove(brsnj)
print('konecna lista: ', lst)



"""4. Da se napravi programa vo koja korisnikot ke vnese proizvolen broj 
na iminja, da se dodadat vo lista, i da se najde najdolgoto ime"""


lst=[]
while True:
    x=input('vnesi ime ili k za kraj ')
    if x =='k':
            break
    else:
        lst.append(x)
dolz=0
for i in lst:
    a=len(i)
    if a>dolz:
        dolz=a
        ime=i
    else:
        continue
print('najdolgoto ime e: {}, so dolzina {}'. format(ime, dolz))

"""5. Da se napravi programa vo koja korisnikot ke vnese proizvolen broj 
na broevi, da se dodadat vo lista i da se najde vtoriot najgolem broj"""

lst=[]
while True:
    x=input('vnesi broj ili k za kraj: ')
    if x=='k':
        break
    else:
        x=int(x)
        lst.append(x)
print('lista: ', lst)
lst.sort()
print('vtoriot najgolem broj e ', lst[-2])

"""6. Da se napravi programa koja ke bide upotrebuvana vo nekoja prodavnica 
za prodazba. Korisnikot da moze da vnesuva produkti se dodeka ne izbere 
deka saka da plati. Produktitte da se dodavaat vo edna lista, cenite vo 
druga lista. Koga ke izbere deka saka da plati da mu se ispecatat produktite 
i cenite vo nalik na "fiskalna smetka". 
Da ima moznost korisnikot da plati i da se presmeta dali i kolku treba da mu se vrati kusur"""

produkti=[]
ceni=[]
print('vnesuvajte gi baranite podatoci, ili pritisnete K za kraj')
while True:
    x=input('produkt: ') 
    if x=='K' or x=='k':
        break
    else:
        y=int(input('cena: '))
        produkti.append(x)
        ceni.append(y)
br=len(produkti)        
for i in range(br):
    print(produkti[i],"              ", ceni[i])
suma=sum(ceni) 
print('za plakjanje:    ', suma)
iznos=int(input('vnesete go vasiot iznos: '))
kusur=iznos-suma
print('za vrakjanje: ', kusur)

    