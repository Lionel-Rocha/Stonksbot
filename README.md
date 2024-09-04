

<div align="center">

![image](https://github.com/user-attachments/assets/4b3f7413-992e-43db-8a38-53e656ad1c17)

  
![Static Badge](https://img.shields.io/badge/Python-3.11-blue?style=flat)
![Static Badge](https://img.shields.io/badge/Status-in_progress-orange?style=flat)
![Static Badge](https://img.shields.io/badge/Gmail-red?style=flat&logo=gmail&logoColor=white&link=mailto%3Alionel.rocha.alves%40gmail.com)

</div>

## Disclaimer
Stonksbot não está associado à Financial Modeling, ao Google ou ao Dados de Mercado. Ele é uma ferramenta open-source, sem uso comercial, e é para uso educacional e de pesquisa. 

## 1. Preparação 
Primeiro, você irá precisar de:
- Uma chave API da Financial Modeling, que pode ser obtido [nesse link](https://intelligence.financialmodelingprep.com/developer/docs);
- Uma app password do Gmail, cujo tutorial pode ser encontrado [aqui](https://support.google.com/mail/answer/185833?hl=en).

Tudo pode ser obtido gratuitamente, e não é necessário pagar para ter uma chave API "plus" (a não ser que mais de mais de 250 chamadas sejam feitas por dia). 

## 2. Configuração do .env
Com o .env em mãos, você deve colocar suas informações nos campos indicados. 

```
smtp_server = 'smtp.gmail.com' #o provedor de email que lidará com as requisições de email
smtp_port = 587 #porta do provedor de email
sender_email = 'email_do_bot@gmail.com.br' #o remetente dos emails do bot. Pode ser uma conta pessoal.
receiver_email = 'seu_email@gmail.com' #o destinatário dos emails do bot. Também pode ser uma conta pessoal, mas diferente da conta do remetente.
password = 'senha de acesso do bot' #app password do Gmail, obtida anteriormente
chave_api = 'chave_api_financial_modeling' #chave API do Financial Modeling
acoes_checar = ACOES_DESEJADAS,SEM_ASPAS #as ações que você quer obter o valor 
palavras_chave="palavras chave para procurar por noticias" #palavras-chave para obter notícias. Exemplo: "petrobras,ibovespa,banco do brasil", sem espaço
horarios_envio="10,13,16" #horários de envio do email pelo bot
```

Remova os # (comentários) antes de fazer o deploy.

> [!WARNING]
> Caso você faça clone e commit desse repositório com suas informações, **não** as torne públicas! Sua chave API e app password são dados sensíveis!

## 3. Deploy da aplicação/disponibilização do endpoint
### Via Dockerfile

Siga os seguintes passos:

``
docker build -t stonksbot:latest .
``

``
docker tag stonksbot:latest seuusuario/stonksbot:latest
``

``
docker push seuusuario/stonksbot:latest 
``

Depois puxe a imagem para seu provedor de serviços favorito.

### Via git clone
Basta clonar o repositório e colocar os arquivos pedidos pelo seu provedor de serviços favorito. Os requirements já estão disponíveis.

## 4. Configuração do monitor

Entre [nesse link](https://dashboard.uptimerobot.com/monitors/new/http) para configurar o bot que irá dar ping no endpoint que você forneceu (supondo que seu serviço não esteja rodando localhost). Então, coloque para ele "pingar" a cada 1 hora (se o intervalo for menor, o stonksbot não vai retornar "sucesso"). Muitas mensagens de erro vão ser retornadas se você configurar no seu .env poucos horários, mas isso é normal. O código prevê apenas uma chamada de endpoint por hora, em horários específicos. Mas é importante que você configure o monitor para receber os emails.

## Contribuição
Issues, stars e forks são bem vindos! Sinta-se à vontade para contribuir com pull requests também. 
