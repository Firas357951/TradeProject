import pandas as pd


df = pd.read_excel("DATA/DATA.xlsx")

Date = []
Price = []
Verif = []

for name in df.iterrows():
    
    X = name[1].to_list()[0].split(',')
    
    date1, date2, price , variation = X[0], X[1], X[2], X[-1]
    
    date = date1 + date2
    price = float(price[1:-1]) 
    verif = float(variation[1:-2]) 
    Date.insert(0,date)
    Price.insert(0,price)
    Verif.insert(0,verif)
    

df = pd.DataFrame({"Date" : Date,"Price" : Price , "Verif" : Verif})
writer = pd.ExcelWriter('Data.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome')
writer.save()   

    
    
