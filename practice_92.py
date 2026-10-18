# Sanitize currency and percentage strings using regex patterns in str.replace
import pandas as pd

data = {
    'item': ['Laptop', 'Desk Chair', 'Monitor', 'Keyboard'],
    'raw_price': ['$1,299.99', '$249.50', '$399.00', '$79.95'],
    'discount': ['10%', '15%', '5%', '20%'],
}

df = pd.DataFrame(data)

# 1. Strip currency symbols and commas, then convert to numeric float
df['clean_price'] = (
    df['raw_price'].str.replace(r'[\$,]', '', regex=True).astype(float)
)

# 2. Strip percent symbol and convert into a decimal proportion
df['discount_rate'] = (
    df['discount'].str.replace('%', '', regex=False).astype(float) / 100
)

# 3. Compute net price after discount
df['net_price'] = (df['clean_price'] * (1 - df['discount_rate'])).round(2)

print(df[['item', 'raw_price', 'clean_price', 'discount_rate', 'net_price']])