# Reshape wide DataFrames into tidy long format using pd.melt
import pandas as pd

# Wide-format sales table with quarterly metric columns
data = {
    'product_id': [101, 102, 103],
    'category': ['Audio', 'Video', 'Audio'],
    'Q1': [12000, 15000, 8000],
    'Q2': [14000, 16500, 9500],
    'Q3': [13500, 17000, 11000],
}

df = pd.DataFrame(data)

# Unpivot wide columns into a tidy long format
df_melted = pd.melt(
    df,
    id_vars=['product_id', 'category'],
    value_vars=['Q1', 'Q2', 'Q3'],
    var_name='quarter',
    value_name='revenue',
)

# Sort records for clean sequential reading
df_melted = df_melted.sort_values(by=['product_id', 'quarter']).reset_index(drop=True)

print(df_melted)