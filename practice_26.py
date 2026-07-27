# Find and remove duplicate order records using duplicated() and drop_duplicates()
import pandas as pd
import io

csv_data = """order_id,customer,product,amount
1,Alice,Laptop,800
2,Bob,Phone,400
3,Alice,Laptop,800
4,Charlie,Tablet,300
5,Bob,Phone,400
6,Diana,Laptop,800
7,Alice,Laptop,800
8,Charlie,Tablet,300"""

df = pd.read_csv(io.StringIO(csv_data))

shape = df.shape[0]
 
duplcates = df.duplicated(subset=['customer', 'product','amount']).sum() 

df = df.drop_duplicates(subset=['customer', 'product', 'amount'])

duplcate_on_name = df.drop_duplicates(subset=['customer'], keep='last') 

droped_shape = df.shape[0]

print(duplcate_on_name)