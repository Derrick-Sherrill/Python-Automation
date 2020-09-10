import pandas as pd
import plotly.express as px

excel_book_1_relative_path = 'Purchases - Home B.xlsx'
excel_book_prices = 'PriceBook.xlsx'

df_prices = pd.read_excel(excel_book_prices)
df_home_1 = pd.read_excel(excel_book_1_relative_path)

#print(df_prices, df_home_1)

df_total = df_home_1.merge(df_prices, on='ID')

df_total['Total Price'] = df_total['PURCHASED AMOUNT'] * df_total['Price']

#print(df_total)

fig = px.pie(df_total[['MATERIAL', 'Total Price']], values='Total Price', names='MATERIAL')
fig.show()
