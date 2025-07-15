import pandas as pd

df = pd.read_csv('merged_chip_data.csv')

print("First few rows of the data:")
print(df.head())

summary = df.groupby(['LIFESTAGE', 'PREMIUM_CUSTOMER'])['TOT_SALES'].sum().reset_index()
print("\nTotal sales by customer segment:")
print(summary)

avg_spend = df.groupby(['LIFESTAGE', 'PREMIUM_CUSTOMER'])['TOT_SALES'].mean().reset_index()
print("\nAverage spend per transaction by segment:")
print(avg_spend)

qty_summary = df.groupby(['LIFESTAGE', 'PREMIUM_CUSTOMER'])['PROD_QTY'].sum().reset_index()
print("\nTotal quantity of chips purchased by segment:")
print(qty_summary)

top_brands = df['BRAND'].value_counts().head(10)
print("\nTop 10 most purchased brands:")
print(top_brands)



