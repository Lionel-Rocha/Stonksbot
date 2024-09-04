# Use uma imagem base
FROM python:3.9-slim

# Configura o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define o comando a ser executado quando o contêiner iniciar
CMD ["python", "main.py"]
