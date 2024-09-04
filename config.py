import os

EMAIL_REMETENTE = os.getenv("sender_email")
EMAIL_DESTINATARIO = os.getenv("receiver_email")
SENHA = os.getenv("password")
SERVIDOR_SMTP = os.getenv("smtp_server")
PORTA_SMTP = os.getenv("smtp_port")
