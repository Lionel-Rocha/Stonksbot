from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def faz_grafico(dados_recentes, acao):
    dates = [entry['date'] for entry in dados_recentes]
    prices = [entry['close'] for entry in dados_recentes]
    dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker='o', linestyle='-', color='b')
    plt.title(f'Preços de {acao} nos últimos 30 Dias')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(f'30_dias_{acao}.png')

    # Limpa a figura para evitar sobreposição com gráficos futuros
    plt.clf()

