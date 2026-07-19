import requests

url = "https://brasilapi.com.br/api/banks/v1"
response = requests.get(url)
bancos = response.json()

print(f"Total de bancos encontrados: {len(bancos)}\n")

# Vamos listar apenas os 10 primeiros para não travar o terminal, 
# e formatar bonitinho usando f-string
print("--- PRIMEIROS 10 BANCOS DA LISTA ---")
for banco in bancos[:10]: 
    codigo = banco.get('code')
    nome_comum = banco.get('name')
    nome_completo = banco.get('fullName')
    
    print(f"Código: {codigo} | Nome: {nome_comum} ({nome_completo})")