from flask import Flask, request, jsonify
import requests
from flasgger import Swagger
from bs4 import BeautifulSoup
import json
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
"""
Verifies the username and password for basic authentication.

Parameters:
username (str): The username provided by the client.
password (str): The password provided by the client.

Returns:
str: The username if the credentials are valid, otherwise None.
"""
@auth.verify_password
def verify_password(username, password):
    if username in USERS and USERS[username] == password:
        return username
    return None

USERS ={
    "admin":"secret",
    "user":"password"
}
"""
Verifies the username and password for basic authentication.

Parameters:
username (str): The username provided by the client.
password (str): The password provided by the client.

Returns:
str: The username if the credentials are valid, otherwise None.
"""
@auth.verify_password
def verify_password(username, password):
    if username in USERS and USERS[username] == password:
        return username
    return None

@auth.verify_password
def verify_password(username, password):
    if username in USERS and USERS[username] == password:
        return username
    return None

app = Flask(__name__)
Swagger(app)

items =[]


@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/scrape/producao', methods=['GET'])

@auth.login_required
def scrape_producao():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    try:
        response = requests.get(url)

        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'tb_base tb_dados'})
        rows = table.find_all('tr')
        data = []

        headers = [header.get_text(strip=True) for header in rows[0].find_all('th')]

        for row in rows[1:]:
            cells = row.find_all('td')
            item_data = {headers[i]: cell.get_text(strip=True) for i, cell in enumerate(cells)}
            data.append(item_data)


        return jsonify(data)
    except  Exception as e: 
        return  jsonify({"error": str(e)}), 500


@app.route('/scrape/comercializacao', methods=['GET'])
@auth.login_required
def scrape_comercializacao():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04'
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    try:
        response = requests.get(url)

        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'tb_base tb_dados'})
        rows = table.find_all('tr')
        data = []

        headers = [header.get_text(strip=True) for header in rows[0].find_all('th')]

        for row in rows[1:]:
            cells = row.find_all('td')
            item_data = {headers[i]: cell.get_text(strip=True) for i, cell in enumerate(cells)}
            data.append(item_data)


        return jsonify(data)
    except  Exception as e: 
        return  jsonify({"error": str(e)}), 500        

@app.route('/items', methods=['GET'])
def get_items():
    return  jsonify(items)

@app.route('/items', methods=['POST'])
def create_items():
    data = request.get_json()
    items.append(data)
    return jsonify(data), 201            

if __name__ == '__main__':
    app.run(debug=True)