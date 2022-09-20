## Liens

Lien_Action = "https://www.binance.com/fr/trade/LUNC_BUSD"

Lien_Portfeuille = "https://www.binance.com/fr/my/wallet/account/main"

Lien_Conversion = "https://www.binance.com/fr/convert?fromCoin=LUNC"

## Charger la page
import gc
import pandas as pd 
from bs4 import BeautifulSoup as bs
import urllib.request
import time

import urllib.request, urllib.error, urllib.parse

url = Lien_Action


reponse = urllib.request.urlopen(url)
contenu_web = reponse.read().decode('UTF-8')

print(contenu_web.split("change buy"))
gc.collect()







