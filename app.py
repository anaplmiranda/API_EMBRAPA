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
    url = 'https://web.archive.org/web/20201203223441/http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
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
    url = 'https://web.archive.org/web/20201203231003/http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04'
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


@app.route('/scrape/importacao/<tipo>', methods=['GET'])
@auth.login_required
def scrape_importacao(tipo):
    vinho_de_mesa = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_05'
    espumantes = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_05'
    uvas_frescas = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_05'
    uvas_passas = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_05'
    suco_de_uva = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_05&opcao=opt_05'
    if tipo not in ['vinho_de_mesa', 'espumantes', 'uvas_frescas', 'uvas_passas', 'suco_de_uva']:
        return jsonify({'error': 'Tipo de importação inválido'}), 400
    match tipo:
        case  "vinho_de_mesa":
            response = requests.get(vinho_de_mesa)

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
        case "espumantes":
            response = requests.get(espumantes)

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
        case "uvas_frescas":
            response = requests.get(uvas_frescas)

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
        case "uvas_passas":
            response = requests.get(uvas_passas)

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
        case "suco_de_uva":
            response = requests.get(suco_de_uva)

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
               
@app.route('/scrape/processamento/<tipo_p>', methods=['GET'])
@auth.login_required
def scrape_processamento(tipo_p):
    viniferas = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_03'
    americanas_hibri = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_03'
    uvas_mesa = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_03'
    sem_classificacao = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_03'
    if tipo_p not in ['viniferas', 'americanas_hibri', 'uvas_mesa', 'uvas_passas', 'sem_classificacao']:
        return jsonify({'error': 'Tipo de importação inválido'}), 400
    match tipo_p:
        case  "viniferas":
            response = requests.get(viniferas)

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
        case "americanas_hibri":
            response = requests.get(americanas_hibri)

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
        case "uvas_mesa":
            response = requests.get(uvas_mesa)

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
        case "sem_classificacao":
            response = requests.get(sem_classificacao)

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


@app.route('/scrape/exportacao/<tipo_e>', methods=['GET'])
@auth.login_required
def scrape_exportacao(tipo_e):
    vinho_de_mesa = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_06'
    espumantes = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_06'
    uvas_frescas = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_06'
    suco_de_uva = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_06'
    if tipo_e not in ['vinho_de_mesa', 'espumantes', 'uvas_frescas', 'suco_de_uva']:
        return jsonify({'error': 'Tipo de importação inválido'}), 400
    match tipo_e:
        case  "vinho_de_mesa":
            response = requests.get(vinho_de_mesa)

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
        case "espumantes":
            response = requests.get(espumantes)

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
        case "uvas_frescas":
            response = requests.get(uvas_frescas)

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
        case "suco_de_uva":
            response = requests.get(suco_de_uva)

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

if __name__ == '__main__':
    app.run(debug=True)