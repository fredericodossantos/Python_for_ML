from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the spreadsheet
file_path = '/home/frederico/Downloads/Lista_imoveis_GO.xlsm'
cleaned_csv_path = '/home/frederico/Downloads/cleaned_data.csv'

# Load and clean the data
df = pd.read_csv(cleaned_csv_path)

# Rename columns if necessary
df.columns = ['N° do imóvel', 'UF', 'Cidade', 'Bairro', 'Endereço', 'Preço', 'Valor de avaliação', 'Desconto', 'Descrição', 'Modalidade de venda', 'Link de acesso']

@app.route('/')
def index():
    columns = df.columns.tolist()
    return render_template('index.html', columns=columns)

@app.route('/sort', methods=['POST'])
def sort():
    column = request.form.get('column')
    sorted_df = df.sort_values(by=column, ascending=False)
    return render_template('report.html', tables=[sorted_df.to_html(classes='data', index=False)], titles=sorted_df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
