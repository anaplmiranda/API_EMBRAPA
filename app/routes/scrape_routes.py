from flask import jsonify
from app import app, auth
import requests
from bs4 import BeautifulSoup

@app.route('/scrape/producao', methods=['GET'])
@auth.login_required
def scrape_producao():

    """
    Scrape data about production.
    ---
    tags:
      - Scraping
    responses:
      200:
        description: A JSON list with the production data scraped.
      400:
        description: URL is required.
      500:
        description: Error scraping data.
    """

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

    """
    Scrape data about commercialization.
    ---
    tags:
      - Scraping
    responses:
      200:
        description: A JSON list with the commercialization data scraped.
      400:
        description: URL is required.
      500:
        description: Error scraping data.
    """

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

    """
    Scrape data about importation.
    ---
    tags:
      - Scraping
    parameters:
      - name: tipo
        in: path
        type: string
        required: true
        description: Type of importation (vinho_de_mesa, espumantes, uvas_frescas, uvas_passas, suco_de_uva, data_ano).
    responses:
      200:
        description: A JSON list with the importation data scraped.
      400:
        description: Invalid type of importation.
      500:
        description: Error scraping data.
    """

    vinho_de_mesa = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_05'
    espumantes = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_05'
    uvas_frescas = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_05'
    uvas_passas = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_05'
    suco_de_uva = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_05&opcao=opt_05'
    if tipo not in ['vinho_de_mesa', 'espumantes', 'uvas_frescas', 'uvas_passas', 'suco_de_uva', 'data_ano']:
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

    """
    Scrape data about processing.
    ---
    tags:
      - Scraping
    responses:
      200:
        description: A JSON list with the processing data scraped.
      400:
        description: URL is required.
      500:
        description: Error scraping data.
    """

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

    """
    Scrape data about exportation.
    ---
    tags:
      - Scraping
    parameters:
      - name: tipo_e
        in: path
        type: string
        required: true
        description: Type of exportation (vinho_de_mesa, espumantes, uvas_frescas, suco_de_uva).
    responses:
      200:
        description: A JSON list with the exportation data scraped.
      400:
        description: Invalid type of exportation.
      500:
        description: Error scraping data.
    """

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