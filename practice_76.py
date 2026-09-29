# Unpivot wide-format DataFrame into tidy long format using pd.melt

import pandas as pd

# Wide-format DataFrame (typical in spreadsheets and reports)
data = {
    'student': ['Alice', 'Bob', 'Charlie'],
    'math': [88, 72, 95],
    'science': [90, 85, 92],
    'english': [85, 78, 88],
}

df = pd.DataFrame(data)

# Unpivot from wide format to tidy long format
long_df = pd.melt(
    df,
    id_vars=['student'],
    value_vars=['math', 'science', 'english'],
    var_name='subject',
    value_name='score'
)

print("Original (Wide format):")
print(df)
print("\nTidy (Long format):")
print(long_df)