import pandas as pd

# Define file paths
input_file_path = '/home/frederico/Downloads/Lista_imoveis_GO.xlsm'
cleaned_excel_path = '/home/frederico/Downloads/cleaned_data.xlsx'
cleaned_csv_path = '/home/frederico/Downloads/cleaned_data.csv'

# Load the spreadsheet
df = pd.read_excel(input_file_path, sheet_name='Lista_imoveis_GO', engine='openpyxl', skiprows=2)

# Rename columns to remove extra spaces or new lines
df.columns = ['N° do imóvel', 'UF', 'Cidade', 'Bairro', 'Endereço', 'Preço', 'Valor de avaliação', 'Desconto', 'Descrição', 'Modalidade de venda', 'Link de acesso']

# Clean up the data
# Remove leading/trailing whitespace from string columns
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Remove completely empty rows
df = df[~df.applymap(lambda x: x == '' if isinstance(x, str) else False).all(axis=1)]

# Drop rows where 'Cidade' is NaN, if necessary
df = df.dropna(subset=['Cidade'])

# Convert columns to appropriate data types
df['Preço'] = pd.to_numeric(df['Preço'], errors='coerce')
df['Valor de avaliação'] = pd.to_numeric(df['Valor de avaliação'], errors='coerce')
df['Desconto'] = pd.to_numeric(df['Desconto'], errors='coerce')

# Save the cleaned data to Excel and CSV files
df.to_excel(cleaned_excel_path, index=False)
df.to_csv(cleaned_csv_path, index=False)

print("Data cleaned and saved successfully.")
