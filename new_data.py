import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
# Read data from Excel file
data = pd.read_excel('pie_chart_data.xlsx')
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
plt.bar(data['Fruit'], data['Quantity'], color='lightgreen')
plt.title('Bar Chart from Excel Data')
plt.xlabel('Fruit')
plt.ylabel('Quantity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar_chart.png', dpi=300)
plt.show()
# pie chart
plt.figure(figsize=(8, 8))
plt.pie(data['Quantity'], labels=data['Fruit'], autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue', 'lightgreen', 'lightyellow'])
plt.title('Pie Chart from Excel Data')
plt.savefig('pie_chart.png', dpi=300)
plt.show()
