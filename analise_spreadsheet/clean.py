import pandas as pd

# Paths
input_file_path = '/home/frederico/Downloads/Lista_imoveis_GO.xlsm'
output_file_path = '/home/frederico/Downloads/cleaned_data.csv'

# Load the spreadsheet
df = pd.read_excel(input_file_path, sheet_name='Lista_imoveis_GO', engine='openpyxl', skiprows=2)

# Rename columns
df.columns = ['N° do imóvel', 'UF', 'Cidade', 'Bairro', 'Endereço', 'Preço', 'Valor de avaliação', 'Desconto', 'Descrição', 'Modalidade de venda', 'Link de acesso']

# Clean up newlines and extra spaces
def clean_text(text):
    if isinstance(text, str):
        text = text.replace('\n', ' ').replace('\r', '')
        text = ' '.join(text.split())
    return text

df = df.applymap(clean_text)

# Save cleaned data to CSV
df.to_csv(output_file_path, index=False)
print("Data cleaned and saved successfully.")
