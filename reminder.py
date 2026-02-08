import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
#create a spreadsheet & append data for sales persons and sales 
wb = openpyxl.Workbook()
ws = wb.active
ws.append(['Sales Person', 'Sales'])    
ws.append(['Alice', 1000])
ws.append(['Bob', 1500])    
ws.append(['Charlie', 1200])
wb.save('sales_data.xlsx')
#read the data from the spreadsheet using pandas
data = pd.read_excel('sales_data.xlsx')
#plot the data using matplotlib
plt.bar(data['Sales Person'], data['Sales'])
plt.xlabel('Sales Person')
plt.ylabel('Sales')
plt.title('Sales Data')
plt.show()
