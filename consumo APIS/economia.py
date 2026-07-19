import requests

# Trocando para uma API que devolve dados estruturados (JSON)
url = "https://economia.awesomeapi.com.br/last/USD-BRL" 
response = requests.get(url)

# Em vez de response.text, usamos .json() para transformar a resposta em um dicionário Python
dados = response.json()

print(dados)

print(f"Nome da moeda: {dados['USDBRL']['name']}")
print(f"Valor de compra: {dados['USDBRL']['bid']}")