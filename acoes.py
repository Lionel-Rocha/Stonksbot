import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import yfinance as yf

load_dotenv()
chave_api = os.getenv("chave_api")

def pega_historico(acao):
    global chave_api

    url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{acao}?serietype=line&apikey={chave_api}'
    resposta = requests.get(url)
    dados = resposta.json()

    trinta_dias = datetime.now() - timedelta(days=30)
    dados_historicos = dados['historical']
    dados_recentes = [entry for entry in dados_historicos if datetime.strptime(entry['date'], '%Y-%m-%d') > trinta_dias]

    return dados_recentes

def pega_dados_atuais(acao):
    global chave_api
    url = f'https://financialmodelingprep.com/api/v3/quote-short/{acao}?apikey={chave_api}'

    resposta = requests.get(url)
    dados = resposta.json()

    primeiro_item = dados[0]

    # Extrai os valores
    preco_atual = primeiro_item['price']
    volume = primeiro_item['volume']

    dados_atuais = [preco_atual, volume]

    return dados_atuais
