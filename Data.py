import pandas as pd


df = pd.read_excel("DATA/DATA.xlsx")

Date = []
Price = []
Verif = []

for name in df.iterrows():
    
    X = name[1].to_list()[0].split(',')
    
    date, price  = X[0], float(X[1])
  
    Date.insert(0,date)
    Price.insert(0,price)
    

df = pd.DataFrame({"Date" : Date,"Price" : Price })
writer = pd.ExcelWriter('Data.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome')
writer.save()   

    
    
