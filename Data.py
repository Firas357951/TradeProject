import pandas as pd


df = pd.read_excel("DATA.xlsx")

Date = []
Price = []

for name in df.iterrows():
    
    X = name[1].to_list()[0].split(',')
    
    date1, date2, price , variation = X[0], X[1], X[2], X[-1]
    
    date = date1 + date2
    price = float(price[1:-1]) 
    Date.append(date)
    Price.append(price)
    
    
df = pd.DataFrame(columns = [Date,Price])
writer = pd.ExcelWriter('TEST.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome')
writer.save()   

    
    
