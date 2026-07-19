import requests

cep_requisição = int(input("Digite o CEP (somente números): "))
url = f"https://viacep.com.br/ws/{cep_requisição}/json/"
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    
    if 'erro' in dados:
        print("CEP não encontrado.")
    else:
        print(f"Logradouro: {dados.get('logradouro')}")
        print(f"Complemento: {dados.get('complemento')}")
        print(f"Bairro: {dados.get('bairro')}")
        print(f"Cidade: {dados.get('localidade')}")
        print(f"UF: {dados.get('uf')}")
else:
    print(f"Erro na requisição. Status Code: {response.status_code}")