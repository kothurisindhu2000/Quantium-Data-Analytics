import pandas as pd

# Load your merged chip data
df = pd.read_csv('merged_chip_data.csv')

# Show first few rows
print("First few rows of the data:")
print(df.head())

# Total sales by LIFESTAGE and PREMIUM_CUSTOMER
summary = df.groupby(['LIFESTAGE', 'PREMIUM_CUSTOMER'])['TOT_SALES'].sum().reset_index()
print("\nTotal sales by customer segment:")
print(summary)

# Average spend per transaction by customer segment
avg_spend = df.groupby(['LIFESTAGE', 'PREMIUM_CUSTOMER'])['TOT_SALES'].mean().reset_index()
print("\nAverage spend per transaction by segment:")
print(avg_spend)

# Total quantity of chips purchased by customer segment
qty_summary = df.groupby(['LIFESTAGE', 'PREMIUM_CUSTOMER'])['PROD_QTY'].sum().reset_index()
print("\nTotal quantity of chips purchased by segment:")
print(qty_summary)

# Top 10 most frequently purchased chip brands
top_brands = df['BRAND'].value_counts().head(10)
print("\nTop 10 most purchased brands:")
print(top_brands)



