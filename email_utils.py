import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
import acoes
import helpers
import noticias
from config import EMAIL_REMETENTE, EMAIL_DESTINATARIO, SENHA, SERVIDOR_SMTP, PORTA_SMTP


def criar_mensagem_email(acoes_checar):
    message = MIMEMultipart()
    message['From'] = EMAIL_REMETENTE
    message['To'] = EMAIL_DESTINATARIO
    message['Subject'] = 'Suas ações do dia'

    body = 'Oi! Eu sou o bot STONKS e vim trazer preços das ações que você está de olho.\n'

    for acao in acoes_checar:
        preco_atual, volume = acoes.pega_dados_atuais(acao)
        dados_historicos = acoes.pega_historico(acao)
        helpers.faz_grafico(dados_historicos, acao)
        body += f"O preço da ação {acao} atualmente é R$ {preco_atual} e o volume é {volume}.\n"

    body += "\n"
    body += "Trouxe também algumas notícias:\n"
    body = noticias.pega_noticias(body)

    body += "Vou colocar uns gráficos em anexo para você comparar o preço nos últimos 30 dias."
    message.attach(MIMEText(body, 'plain'))

    anexar_graficos(message, acoes_checar)
    return message


def anexar_graficos(message, acoes_checar):
    for acao in acoes_checar:
        img_path = f'30_dias_{acao}.png'
        if os.path.exists(img_path):
            with open(img_path, 'rb') as img_file:
                img_data = img_file.read()
                img = MIMEImage(img_data, name=os.path.basename(img_path))
                message.attach(img)
        else:
            print(f'Gráfico para a ação {acao} não encontrado.')

def enviar_email(message):
    try:
        with smtplib.SMTP(SERVIDOR_SMTP, int(PORTA_SMTP)) as server:
            server.starttls()
            server.login(EMAIL_REMETENTE, SENHA)
            server.sendmail(EMAIL_REMETENTE, EMAIL_DESTINATARIO, message.as_string())

        return 'E-mail enviado com sucesso!', 200
    except Exception as e:
        return f'Ocorreu um erro: {e}', 500
