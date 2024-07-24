from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the cleaned CSV file
csv_file_path = '/home/frederico/Downloads/cleaned_data.csv'
df = pd.read_csv(csv_file_path)

# Rename columns if necessary (they should already be clean)
df.columns = ['N° do imóvel', 'UF', 'Cidade', 'Bairro', 'Endereço', 'Preço', 'Valor de avaliação', 'Desconto', 'Descrição', 'Modalidade de venda', 'Link de acesso']

@app.route('/')
def index():
    cities = df['Cidade'].unique()
    return render_template('index.html', cities=cities)

@app.route('/sort', methods=['POST'])
def sort():
    city = request.form.get('city')
    sorted_df = df[df['Cidade'] == city].sort_values(by='Desconto', ascending=False)
    return render_template('report.html', tables=[sorted_df.to_html(classes='data', index=False)], titles=sorted_df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
