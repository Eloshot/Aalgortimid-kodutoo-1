import math
arvud = [1,2,3,4,5,6,7,8,9]
otsitav_arv = 4

def binaarne_otsing(a,n): #a on otsitava arvu vaartus ja n on loend kust otsime
    vasak = arvud[0]
    parem = arvud[len(n) -1] #leiame viimase numbri indeksi
    kesk = round((parem + vasak) /2) # võtame keskmise punkti ja kui vaja ümardame
    while True:
        print(vasak, kesk, parem) # et näeks mida programm teeb
        if kesk == a:
            return kesk #leitsime punkti
        elif kesk < a:
            vasak = kesk
            kesk = math.floor((parem + vasak) /2) # kui otsitav arv on suurem keskmisest, teeme kpreaguse keskmise uue vasak punktist, kuna arv on paremal
            
        else:
            parem = kesk
            kesk = math.floor((parem + vasak) /2) # kui otsitav on vaiksem kui keskmine siis teeme parema uueks keskmisest,kuna arv on vasakul.
            
print(binaarne_otsing(otsitav_arv,arvud))
    






