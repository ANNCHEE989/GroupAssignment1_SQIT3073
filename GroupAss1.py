import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import seaborn as sb
import squarify

#Import the dataset

df= pd.read_excel(r"C:\Users\qianh\OneDrive\Desktop\UUM\SEM 5\3.6.5.xlsx", sheet_name="YEAR", header=[0,1])

df.columns = pd.MultiIndex.from_tuples([(first, second.replace('Unnamed: 0_level_1', '')) if 'Unnamed: ' in second else 
                                       (first, second) for first, second in df.columns])
df= df.astype(int)

print(df)

# Pareto chart
df.index= df[('Period','')]

color1 = 'steelblue'
color2 = 'red'
line_size = 4

fig, ax = plt.subplots()
ax.bar(df.index, df[('Total major exports','Percentage of total exports')], color=color1)
ax.yaxis.set_major_formatter(PercentFormatter())
ax.set_ylabel('Percentage of total exports (%)')

ax2 = ax.twinx()
ax2.plot(df.index, df[('Total major exports','Value')], color=color2, marker="D", ms=line_size) 
ax2.set_ylabel('Value (RM million)')

ax.tick_params(axis='y', colors=color1)
ax2.tick_params(axis='y', colors=color2)
ax.set_xlabel('Year')
ax.set_title('TOTAL MAJOR EXPORTS FROM 2013 TO 2022')

plt.show()

# Treemap

column_to_sum=[('Natural rubber','Value'),('Saw logs', 'Value'), ('Sawn timber','Value'), ('Palm oil', 'Value'),('Tin3','Value'),('Crude oil','Value'),
                ('Liquefied natural gas','Value')]
sum_values= df[column_to_sum].sum()


tree_map_data = pd.DataFrame({'Major Exports': ["Natural rubber", "Saw logs", "Sawn timber",'Palm oil','Tin3','Crude oil','Liquefied natural gas'],
                                'Total': sum_values})

print(tree_map_data)

tree_map_data = tree_map_data.sort_values(by='Total', ascending=False)
plt.figure(figsize=(10, 6))
axis = squarify.plot(sizes=tree_map_data['Total'],label=tree_map_data.apply(lambda x: f"{x['Major Exports']} \n (RM {x['Total']})",axis=1), color=sb.color_palette("tab20", len(tree_map_data)),
                    ec='white', text_kwargs={'fontsize': 12, 'wrap': True}) 

plt.axis('off') 
plt.title('THE TOTAL VALUE FOR THE MAJOR EXPORTS FROM 2013 TO 2022 (RM million)')


plt.show()


# Pie Chart

list_average = df[[('Palm oil', 'Volume'),('Crude oil', 'Volume'),('Liquefied natural gas', 'Volume')]].mean().round(2)

print(list_average)

labels = list_average.index
values = list_average.values

plt.figure(figsize=(10, 6))
plt.pie(values, labels=['Palm oil','Crude oil','Liquefied natural gas'], autopct='%1.1f%%', startangle=90, colors=['blue','darkorange','skyblue'])
plt.title('AVERAGE VOLUME OF GROSS EXPORTS OF MAJOR AGRICULTURE AND MINING COMMODITIES FROM 2013 TO 2022')
plt.show()


# Group Bar chart Value
df.set_index('Period', inplace=True)
selected_columns = [('Natural rubber', 'Value'),('Saw logs', 'Value'),('Sawn timber', 'Value'), ('Palm oil', 'Value'), ('Tin3', 'Value'),
                    ('Crude oil', 'Value'), ('Liquefied natural gas', 'Value')]

ax = df[selected_columns].plot(kind='bar', width=0.8, figsize=(10, 6))
ax.set_xlabel('Year')
ax.set_ylabel('Value (RM million)')
ax.set_title('VALUE FOR GROSS EXPORTS OF MAJOR AGRICULTURE AND MINING COMMODITIES FROM 2013 TO 2022')
ax.legend(['Natural rubber','Saw logs', 'Sawn timber', 'Palm oil', 'Tin3', 'Crude oil', 'Liquefied natural gas'])

plt.show()




