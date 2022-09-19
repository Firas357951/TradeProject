## Liens

Lien_Action = "https://www.binance.com/fr/trade/LUNC_BUSD"

Lien_Portfeuille = "https://www.binance.com/fr/my/wallet/account/main"

Lien_Conversion = "https://www.binance.com/fr/convert?fromCoin=LUNC"

## Charger la page

import pandas as pd 
from bs4 import BeautifulSoup as bs
import urllib.request
import time

while True:
    page = urllib.request.urlopen(Lien_Action)
    soup = bs(page)
    

    A = soup.find_all('title')

    Valeur_Actif = float(str(A[0]).split(":")[1].split('|')[0])

    page.refresh()
    print(Valeur_Actif)












