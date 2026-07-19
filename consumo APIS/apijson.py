import requests

# Trocando para uma API que devolve dados estruturados (JSON)
url = "https://api.github.com/users/renanpablo717" # ou qualquer outro usuário do GitHub
response = requests.get(url)

# Em vez de response.text, usamos .json() para transformar a resposta em um dicionário Python
dados = response.json()

# Agora conseguimos acessar chaves específicas!
print(f"Nome no GitHub: {dados.get('name')}")
print(f"Bio: {dados.get('bio')}")
print(f"Repositórios públicos: {dados.get('public_repos')}")

print(dados)