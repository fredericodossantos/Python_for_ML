from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the spreadsheet
file_path = '/home/frederico/Downloads/Lista_imoveis_GO.xlsm'
df = pd.read_excel(file_path, sheet_name='Lista_imoveis_GO', engine='openpyxl', skiprows=2)

# Rename columns
df.columns = ['N° do imóvel', 'UF', 'Cidade', 'Bairro', 'Endereço', 'Preço', 'Valor de avaliação', 'Desconto', 'Descrição', 'Modalidade de venda', 'Link de acesso']

# Remove rows with \n in any cell
df = df.applymap(lambda x: x if isinstance(x, str) else '').replace('\n', '', regex=True)
df = df[df.apply(lambda x: x.str.contains('\n').any(), axis=1) == False]

@app.route('/')
def index():
    columns = df.columns.tolist()
    return render_template('index.html', columns=columns)

@app.route('/sort', methods=['POST'])
def sort():
    column = request.form.get('column')
    if column in df.columns:
        sorted_df = df.sort_values(by=column, ascending=False)
        return render_template('report.html', tables=[sorted_df.to_html(classes='data', index=False)], titles=sorted_df.columns.values)
    else:
        return "Invalid column name", 400

if __name__ == '__main__':
    app.run(debug=True)
