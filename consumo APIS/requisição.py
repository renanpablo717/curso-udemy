import requests

for num in range(60):
    response = requests.get("https://api.github.com/meta")
    print(f'Requisição {num}, Resposta: {response.status_code}')