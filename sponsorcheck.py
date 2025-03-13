from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the Excel file
df = pd.read_excel('2024-US.xlsx')

@app.route('/search', methods=['POST'])
def search_company():
    company_name = request.json['company_name']
    result = 'yes' if company_name in df['C'].values else 'no'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
