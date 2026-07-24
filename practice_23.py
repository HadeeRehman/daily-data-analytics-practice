# Add columns, append rows with concat(), and update rows using loc[]
import pandas as pd

data = {'Name':['Hadi', 'Parray','Arsu'],
        'Age': [17, 19, 32]
}

df = pd.DataFrame(data, index=['Employee 1', 'Employee 2','Employee 3'])

# Adding new column
df['Job'] = ['Python', 'Programmer', 'Editor']

# Adding a new rows
new_rows = pd.DataFrame([{'Name': 'Mujtaba', 'Age': 19, 'Job': 'Student'},{'Name': 'Nazim', 'Age': 16, 'Job': 'Master'}], index=['Employee 4', 'Employee 5'])
df = pd.concat([df, new_rows])

new_rows = {'Name':'Alle', 'Age':18, 'Job':'Business Man'}
df.loc['Employee 4'] = new_rows


print(df)