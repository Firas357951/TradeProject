from pydoc import describe
import pandas as pd

df = pd.read_excel("Data.xlsx")


Money = [100]

Actif = [0]

Decision = ['S']

Memoire = [1.0903]

for name in df.iterrows():
    
        
    price = name[1][2]
    indice = name[1][3]
    
    if ((price >= Memoire[-1]*1.02)) and (Decision[-1] == 'B'):
        Memoire.append(price)
        Decision.append('S')
        Money.append(Actif[-1]*price)
        Actif.append(0)
        
    if (price <= Memoire[-1]*0.98) and (Decision[-1] == 'S'):
        Memoire.append(price)
        Decision.append('B')
        Actif.append(Money[-1]/price)
        Money.append(0)
        
    else:
        Decision.append(Decision[-1])
        Money.append(Money[-1])
        Actif.append(Actif[-1])
    
    
            
print(Money)







