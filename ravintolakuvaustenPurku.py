
# coding: utf-8

#Ravintolakuvausten purkaminen maplantiksen ylläpidolta saadusta jsonista





import json

ravintolat = json.loads(open('ravintolat.json').read())

#luodaan listat kunkin Ravintolapäivän ravintoloista

ravintolat2011_05 = []
ravintolat2011_08 = []
ravintolat2011_11 = []
ravintolat2012_02 = []
ravintolat2012_05 = []
ravintolat2012_08 = []
ravintolat2012_11 = []
ravintolat2013_02 = []
ravintolat2013_05 = []
ravintolat2013_08 = []
ravintolat2013_11 = []
ravintolat2014_02 = []
ravintolat2014_05 = []
ravintolat2014_08 = []
ravintolat2014_11 = []
ravintolat2015_02 = []
ravintolat2015_05 = []
ravintolat2015_08 = []
ravintolat2015_11 = []
ravintolat2016_02 = []
ravintolat2016_05 = []
ravintolat2016_08 = []
ravintolat2016_talvi = []

luku = 0

virheLaskuri = 0

#käydään koko json läpi ja puretaan ravintolakuvaukset ja ravintolan nimi kunkin Ravintolapäivän listaan

while luku < len(ravintolat):
    if '2011-05' in ravintolat[luku]['fields']['date']:
        ravintolat2011_05.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2011-08' in ravintolat[luku]['fields']['date']:
        ravintolat2011_08.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2011-11' in ravintolat[luku]['fields']['date']:
        ravintolat2011_11.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2012-02' in ravintolat[luku]['fields']['date']:
        ravintolat2012_02.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2012-05' in ravintolat[luku]['fields']['date']:
        ravintolat2012_05.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2012-08' in ravintolat[luku]['fields']['date']:
        ravintolat2012_08.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2012-11' in ravintolat[luku]['fields']['date']:
        ravintolat2012_11.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2013-02' in ravintolat[luku]['fields']['date']:
        ravintolat2013_02.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2013-05' in ravintolat[luku]['fields']['date']:
        ravintolat2013_05.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2013-08' in ravintolat[luku]['fields']['date']:
        ravintolat2013_08.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2013-11' in ravintolat[luku]['fields']['date']:
        ravintolat2013_11.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2014-02' in ravintolat[luku]['fields']['date']:
        ravintolat2014_02.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2014-05' in ravintolat[luku]['fields']['date']:
        ravintolat2014_05.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2014-08' in ravintolat[luku]['fields']['date']:
        ravintolat2014_08.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2014-11' in ravintolat[luku]['fields']['date']:
        ravintolat2014_11.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    elif '2015-02' in ravintolat[luku]['fields']['date']:
        ravintolat2015_02.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))    
    elif '2015-05' in ravintolat[luku]['fields']['date']:
        ravintolat2015_05.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))    
    elif '2015-08' in ravintolat[luku]['fields']['date']:
        ravintolat2015_08.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))    
    elif '2015-11' in ravintolat[luku]['fields']['date']:
        ravintolat2015_11.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))    
    elif '2016-02-21' in ravintolat[luku]['fields']['date']:
        ravintolat2016_02.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))    
    elif '2016-05-21' in ravintolat[luku]['fields']['date']:
        ravintolat2016_05.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))    
    elif '2016-08' in ravintolat[luku]['fields']['date']:
        ravintolat2016_08.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))    
    elif '2016-09' in ravintolat[luku]['fields']['date'] or '2016-10' in ravintolat[luku]['fields']['date'] or '2016-11' in ravintolat[luku]['fields']['date'] or '2016-12' in ravintolat[luku]['fields']['date']:
        ravintolat2016_talvi.append((ravintolat[luku]['fields']['title']) + ' ' + (ravintolat[luku]['fields']['description']))
    else:
        virheLaskuri += 1
    luku = luku + 1
        

        


import os
luku = 0

#kirjoitetaan ravintolakuvaukset listoista omiksi tekstitiedostoikseen

paivat = [ravintolat2011_05, ravintolat2011_08, ravintolat2011_11, ravintolat2012_02, ravintolat2012_05, ravintolat2012_08, ravintolat2012_11, ravintolat2013_02, ravintolat2013_05, ravintolat2013_08, ravintolat2013_11, ravintolat2014_02, ravintolat2014_05, ravintolat2014_08, ravintolat2014_11, ravintolat2015_02, ravintolat2015_05, ravintolat2015_08, ravintolat2015_11, ravintolat2016_02, ravintolat2016_05, ravintolat2016_08, ravintolat2016_talvi]
paivatString = ['ravintolat2011_05', 'ravintolat2011_08', 'ravintolat2011_11', 'ravintolat2012_02', 'ravintolat2012_05', 'ravintolat2012_08', 'ravintolat2012_11', 'ravintolat2013_02', 'ravintolat2013_05', 'ravintolat2013_08', 'ravintolat2013_11', 'ravintolat2014_02', 'ravintolat2014_05', 'ravintolat2014_08', 'ravintolat2014_11', 'ravintolat2015_02', 'ravintolat2015_05', 'ravintolat2015_08', 'ravintolat2015_11', 'ravintolat2016_02', 'ravintolat2016_05', 'ravintolat2016_08', 'ravintolat2016_talvi']

kierros = 0

for paiva in paivat:
    for entree in paiva:
        path = os.path.join('./', paivatString[kierros] , entree.split(' ', 1)[0] + entree.split(' ', 2)[1] + '.txt')
        outfile = open(path, mode="w+")
        outfile.write(entree)
        outfile.close()
    
    kierros += 1



