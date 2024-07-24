import pandas as pd
import matplotlib.pyplot as plt

# Load the spreadsheet
file_path = '/home/frederico/Downloads/Lista_imoveis_GO.xlsm'
df = pd.read_excel(file_path, sheet_name='Lista_imoveis_GO', engine='openpyxl', skiprows=2)

# Rename columns
df.columns = ['N° do imóvel', 'UF', 'Cidade', 'Bairro', 'Endereço', 'Preço', 'Valor de avaliação', 'Desconto', 'Descrição', 'Modalidade de venda', 'Link de acesso']

# Display the first few rows to understand the structure
print(df.head())

# Display summary statistics
print(df.describe())

# Display info about data types and missing values
print(df.info())

# Clean the data
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df['Preço'] = pd.to_numeric(df['Preço'], errors='coerce')
df['Valor de avaliação'] = pd.to_numeric(df['Valor de avaliação'], errors='coerce')
df['Desconto'] = pd.to_numeric(df['Desconto'], errors='coerce')

# Basic statistics
print(df[['Preço', 'Valor de avaliação', 'Desconto']].describe())

# Group by 'Cidade' and calculate average price
avg_price_by_city = df.groupby('Cidade')['Preço'].mean()
print(avg_price_by_city)

# Visualize the distribution of 'Preço'
df['Preço'].hist()
plt.title('Distribution of Prices')
plt.xlabel('Preço')
plt.ylabel('Frequency')
plt.show()

# Save to a new Excel file
df.to_excel('/home/frederico/Downloads/path_to_save_analysis.xlsx', index=False)

# Save to a CSV file
df.to_csv('/home/frederico/Downloads/path_to_save_analysis.csv', index=False)
