<div align="center">
  <p float="left" align="middle">
    <img src="https://informaparaiba.com.br/wp-content/uploads/2024/01/Embrapa.svg_.png" alt="Logo Embrapa" width="400"/>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://www.fiap.com.br/wp-content/themes/fiap2016/images/sharing/fiap.png" alt="Logo FIAP" width="300"/>
  </p>
</div>

# API Pública de Consulta de Dados da Embrapa

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://python.org)
[![Flask Version](https://img.shields.io/badge/flask-3.0.3-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-development-orange)](/)
[![Documentation](https://img.shields.io/badge/docs-swagger-green)](/)
[![JWT](https://img.shields.io/badge/security-JWT-brightgreen.svg)](/)
[![BeautifulSoup](https://img.shields.io/badge/scraping-BeautifulSoup4-lightgrey)](https://www.crummy.com/software/BeautifulSoup/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](/)
[![Made with](https://img.shields.io/badge/made%20with-python-blue.svg)](https://python.org)
[![FIAP](https://img.shields.io/badge/FIAP-project-red.svg)](https://www.fiap.com.br)
[![API](https://img.shields.io/badge/API-REST-yellow.svg)](/)
[![Coverage](https://img.shields.io/badge/coverage-85%25-green.svg)](/)
[![Last Commit](https://img.shields.io/badge/last%20commit-november-yellow.svg)](/)

## 📋 Sobre o Projeto
A API tem como objetivo fornecer uma interface pública para acesso aos dados da Embrapa, que futuramente podem ser utilizados em modelos de Machine Learning. Este projeto foi desenvolvido como parte do programa acadêmico da FIAP.

## 📋 Sumário
- [Visão Geral](#visão-geral)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Documentacao](#documentacao)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
- [Uso](#uso)
- [Endpoints](#endpoints)
- [Autenticação](#autenticação)

## 🎯 Visão Geral

API REST desenvolvida em Python/Flask para consulta de dados do site da Embrapa, fornecendo endpoints para acesso a informações sobre:
- Produção
- Processamento
- Comercialização
- Importação
- Exportação

## 📁 Estrutura do Projeto

```
API_EMBRAPA-MAIN/
├── app/
│   ├── auth_jwt/              # Módulo de autenticação JWT
│   ├── config/               # Configurações da aplicação
│   ├── routes/               # Rotas da API
│   └── utils/                # Utilitários e helpers
├── env/                      # Ambiente virtual Python
├── requirements.txt          # Dependências do projeto
└── run.py                    # Arquivo de inicialização
```

## 📁 Documentacao
Swagger: http://54.233.14.210:5000/apidocs/
Deploy: http://54.233.14.210
Server: AWS Server

```
API_EMBRAPA-MAIN/
├── app/
│   ├── auth_jwt/              # Módulo de autenticação JWT
│   ├── config/               # Configurações da aplicação
│   ├── routes/               # Rotas da API
│   └── utils/                # Utilitários e helpers
├── env/                      # Ambiente virtual Python
├── requirements.txt          # Dependências do projeto
└── run.py                    # Arquivo de inicialização
```


## 🛠 Tecnologias

### Core
- Python 3.10
- Flask 3.0.3
- Flask-HTTPAuth 4.8.0
- PyJWT 2.3.0

### Web Scraping
- BeautifulSoup4 4.12.3
- Requests 2.32.3

### Segurança
- cryptography 43.0.3
- MarkupSafe 3.0.2

### Utilitários
- python-dotenv 1.0.1
- PyYAML 6.0.2

## ⚙️ Instalação

1. Clone o repositório:
```bash

git clone https://github.com/anaplmiranda/API_EMBRAPA.git #windows
cd API_EMBRAPA #windows
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv env
source env/bin/activate  # Linux/MacOS
# ou
.\env\Scripts\activate  # Windows

(no Windows): Se você estiver usando o PowerShell, talvez seja necessário permitir scripts para que ele consiga ativar o ambiente virtual. Execute o seguinte comando no PowerShell com permissão de administrador:
powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

## 💻 Uso

Para iniciar o servidor de desenvolvimento:
```bash
python run.py
```

## 🌐 Endpoints

### Autenticação
- `POST /auth/token`: Gera token JWT de acesso

### Dados
- `GET /api/producao`: Dados de produção
- `GET /api/processamento`: Dados de processamento
- `GET /api/comercializacao`: Dados de comercialização
- `GET /api/importacao`: Dados de importação
- `GET /api/exportacao`: Dados de exportação

## 🔐 Autenticação

A API utiliza autenticação JWT (JSON Web Tokens). Para acessar os endpoints protegidos:

1. Obtenha um token através do endpoint de autenticação
2. Inclua o token no header das requisições:
```
Authorization: Bearer <seu-token>
```

Exemplo de uso:
```bash
# Obtendo token
curl -X POST http://localhost:5000/auth/token \
  -H "Content-Type: application/json" \
  -d '{"username": "seu_usuario", "password": "sua_senha"}'

# Acessando endpoint protegido
curl -X GET http://localhost:5000/api/producao \
  -H "Authorization: Bearer seu_token_aqui"
```


#Revisão Documento Ricardo Mororo v3 04-11-2024