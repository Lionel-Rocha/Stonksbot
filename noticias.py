import os

import requests
from bs4 import BeautifulSoup

def pega_noticias(body):
    keywords = os.getenv("palavras_chave").split(',')

    resultados_filtrados = []

    # Percorrer as páginas de 1 a 10 do site.
    for page in range(1, 5):
        url = f"https://www.dadosdemercado.com.br/ultimas-noticias/{page}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            links = soup.find_all('a', href=True)

            for link in links:
                text = link.get_text().strip().lower()
                href = link['href']

                if any(keyword in text for keyword in keywords):
                    resultados_filtrados.append((text, href))
        else:
            print(f"Falha ao acessar {url}")

    contador = 0
    for result in resultados_filtrados:
        if contador == 11:
            break
        else:
            body += f"Notícia: {result[0]} \nLink: {result[1]}"
            body += "\n"
            body += "-" * 40
            body += "\n"
        contador +=1
    body += "\n"
    return body