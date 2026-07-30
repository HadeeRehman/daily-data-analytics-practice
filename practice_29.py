# Summarize monthly sales data using pivot tables with totals and averages
import pandas as pd
import io

csv_data = """name,dept,month,sales
Alice,Sales,Jan,5000
Bob,IT,Jan,3000
Alice,Sales,Feb,6000
Charlie,Sales,Jan,4500
Bob,IT,Feb,3500
Diana,HR,Jan,2000
Charlie,Sales,Feb,5500
Diana,HR,Feb,2500
Alice,Sales,Mar,7000
Bob,IT,Mar,4000"""

df = pd.read_csv(io.StringIO(csv_data))

# pivot_table : "Create a summary table from my DataFrame."

pivot_df = pd.pivot_table(df, index='name', columns='month', values='sales', aggfunc='sum', margins=True)

average = pd.pivot_table(df,  margins=True, index='dept', columns='month', values='sales', aggfunc='mean') 

average.fillna(0, inplace=True) 
print(average)
print(pivot_df)