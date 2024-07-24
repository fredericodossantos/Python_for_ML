import pandas as pd

# Update the file path to the correct location
file_path = '/home/frederico/Downloads/Lista_imoveis_GO.xlsm'
df = pd.read_excel(file_path, sheet_name='Lista_imoveis_GO', engine='openpyxl')

import pandas as pd

# Update the file path to the correct location
file_path = '/home/frederico/Downloads/Lista_imoveis_GO.xlsm'
df = pd.read_excel(file_path, sheet_name='Lista_imoveis_GO', engine='openpyxl')

# Display the first few rows to understand the structure
print(df.head())
print(df.columns)
print(df.dtypes)
print(df.shape)


