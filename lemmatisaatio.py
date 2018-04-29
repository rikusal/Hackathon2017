
# coding: utf-8

# In[2]:

#!/usr/bin/env python


import sys
#kerrotaan mistä löytyvät ladatut kirjastot
sys.path.append('home/riku/anaconda3/lib/python3.5/site-packages')
import simplejson as json
import websocket
from pprint import pprint
import os
import time
import re



# In[3]:

#kielentarkistus- ja lemmatisaatiofunktiot


def languageChecker(text):
    success = False
    response = ''
    while success == False:
        try:
            ws = websocket.WebSocket()
            ws.connect("ws://demo.seco.cs.aalto.fi/las/identifyWS")
            message = {"text": text}
            jmsg = json.dumps(message)
            ws.send(jmsg)
            resp =ws.recv()
            response = json.loads(resp)
            ws.close()
            success == True
            break
        except:
            time.sleep(10)
            success == False
            print ('ERROR languageChecker ERROR')
            ws.close()
            break
            
    if response['locale'] == 'en':
        return ('en')
    else:
        return ('fi') 
        
    
    
def lemmatization(text, language):
    success = False
    response = ''
    while success == False:
        try:
            ws = websocket.WebSocket()
            ws.connect("ws://demo.seco.cs.aalto.fi/las/analyzeWS")
            message = {"locale":language,"text": text}
            jmsg = json.dumps(message)
            #pprint(message)
            ws.send(jmsg)
            resp =ws.recv()
            response = json.loads(resp)
            ws.close()
            success == True
            break
        except:
            time.sleep(10)
            success == False
            print ('ERROR lemmatization ERROR')
            ws.close()
            break
    return response
    


# In[6]:

#varsinainen koodi!


#luodaan lista ravintoloiden päivämääristä
#paivamaarat = ['2011_05', '2011_08', '2011_11', '2012_02', '2012_05', '2012_08', '2012_11', '2013_02', '2013_05', '2013_08', '2013_11', '2014_02', '2014_05', '2014_08', '2014_11', '2015_02', '2015_05', '2015_08', '2015_11', '2016_02', '2016_05', '2016_08', '2016_talvi']
paivamaarat = ['2016_05', '2016_08', '2016_talvi']

#avataan iteroiden ravintolakuvaus..


for paivamaara in paivamaarat:

    #näitä muuttujia tarvitaan myöhemmin kirjoitettaessa lemmatisoituja kuvauksia tiedostoiksi
    enLuku = 1
    fiLuku =1

    
    for filename in os.listdir('ravintolat' + paivamaara + '/'):


        infile = open('ravintolat' + paivamaara + '/' + filename)
        text = infile.read()
        infile.close()

        #languageChecker funktiolla tarkistetaan ravintolakuvauksen kieli

        textLan = languageChecker(text)

        #lähetetään text-muuttujaan avattu ravintolakuvaus palvelimille lemmatisoitavaksi


        response = lemmatization(text, textLan)


        #puretaan vastauksena saadusta jsonista talteen lemmamuodot stringiin lemmaKuvaus

        lemmaKuvaus = ''
        for entree in response:
            lemmaKuvaus = lemmaKuvaus + (entree['analysis'][0]['wordParts'][0]['lemma'])


        #käytetään regexiä poistaaksemme rumat ja turhat URLit 

        re_lemmaKuvaus = re.sub(r'http.+', r'', lemmaKuvaus)

        #ja tallennetaan kunkin ravintolan lemmattu kuvaus omaksi tekstiedostokseen

        if textLan == 'en':
            path = os.path.join('./lemmaMuodot/ravintolat' + paivamaara + '/en/' + paivamaara + '_' + str(enLuku) +'.txt')
            outfile = open(path, mode='w')
            outfile.write(re_lemmaKuvaus)
            outfile.close()
            enLuku = enLuku + 1
        else:
            path = os.path.join('./lemmaMuodot/ravintolat' + paivamaara + '/fi/' + paivamaara + '_' + str(fiLuku) +'.txt')
            outfile = open(path, mode='w')
            outfile.write(re_lemmaKuvaus)
            outfile.close()
            fiLuku = fiLuku + 1
            
    print (paivamaara + ' valmis!')


# In[6]:

#regular expression niiden ärsyttävien http-osoitteiden poistamiseksi. Poistaa kaiken osoitteen jälkeen
#mutta onneksi liki kaikki osoitteet vaikuttavat olevan kuvausten lopussa. Olen valmis ottamaan riskin

import re
text = 'Yösnägäri Kakkonen  Toinen yö snägärillä. Kotkankadun snägäri muutti  ·  Toinen yö snägärillä. Kotkankadun snägäri muutti nurkan taakke! Sama meno, uusii makui.Tarjolla mm. C-kassu-DJ ja sammiollinen majojneesia. Ei tappeluita. Porvoonkatu 27, klo 21-23, Ina 044-2856058 http://www.facebook.com/event.php?eid=133908816701871'

re_text = re.sub(r'http.+', r'', text)

print(re_text)






