from datetime import datetime, timedelta
from flask import Flask, jsonify
from flask_cors import CORS
import os
from email_utils import criar_mensagem_email, enviar_email


app = Flask(__name__)
CORS(app)

ultima_chamada = None

@app.route("/enviar_email", methods=['HEAD'])
def enviar_email_route():
    global ultima_chamada

    agora = datetime.now()

    hora_atual = agora.hour

    horarios_envio = list(map(int, os.getenv("horarios_envio").split(',')))

    if hora_atual not in horarios_envio:
        return jsonify({"erro": "Este endpoint só pode ser chamado nos horários permitidos."}), 429

    if ultima_chamada is not None:
        tempo_decorrido = agora - ultima_chamada
        if tempo_decorrido < timedelta(hours=1):
            return jsonify({"erro": "Este endpoint só pode ser chamado uma vez por hora."}), 429

    ultima_chamada = agora

    acoes_checar = os.getenv("acoes_checar").split(',')
    mensagem = criar_mensagem_email(acoes_checar)
    return enviar_email(mensagem)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
