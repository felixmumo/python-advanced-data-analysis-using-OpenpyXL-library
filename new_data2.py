from openpyxl import Workbook
wb=Workbook()
ws=wb.active
ws.append(['Fruit', 'Quantity'])
ws.append(['Apple', 30])
ws.append(['Banana', 20])
ws.append(['Orange', 15])
ws.append(['Grapes', 25])
#create a new Excel file with the data from python
wb.save('new_data.xlsx')
import pandas as pd
import matplotlib.pyplot as plt 
import openpyxl
# Read data from Excel file
data = pd.read_excel('new_data.xlsx')
# Display the data
print(data)
# mean for Quantity column
mean_quantity = data['Quantity'].mean()
print("Mean Quantity is:", mean_quantity)
highest_quantity = data['Quantity'].max()
print("Highest Quantity is:", highest_quantity)
lowest_quantity = data['Quantity'].min()
print("Lowest Quantity is:", lowest_quantity)
standard_deviation_quantity = data['Quantity'].std()
print("Standard Deviation of Quantity is:", standard_deviation_quantity)
#bar chart
plt.figure(figsize=(10, 6))
plt.bar(data['Fruit'], data['Quantity'], color='lightblue')
plt.title('Bar Chart from Excel Data')
plt.xlabel('Fruit')
plt.ylabel('Quantity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar_chart2.png', dpi=300)
plt.show()

