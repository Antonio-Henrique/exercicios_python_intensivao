import requests
#estabelecendo a conexão com a api
res = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')

#acessando as informações da api
res_json = res.json()

#cotação do dólar
cotacao_dolar = float(res_json["USDBRL"]["bid"])
#cotação do euro
cotacao_euro = float(res_json["EURBRL"]["bid"])
    

print('CONVERSOR DE MOEDAS')
print('-' * 45)
real = float(input('Quantos reais você tem: R$'))
dolar = real / cotacao_dolar
euro = real / cotacao_euro
print('-' * 45)
print(f'''R${real:.2f }= USD{dolar:.2f}
R${real:.2f} = EUR{euro:.2f}''')
print('-' * 45)
print(f'''A cotação atual do dólar é: R${cotacao_dolar}
A cotação atual do euro é: R${cotacao_euro}''')















