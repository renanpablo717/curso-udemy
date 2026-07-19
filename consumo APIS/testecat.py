import requests
from translate import Translator

url = "https://catfact.ninja/fact"
response = requests.get(url)

dados = response.json()

# 1. Pegamos apenas o texto em inglês que está dentro da chave 'fact'
fato_em_ingles = dados.get('fact')

# 2. Configurando o tradutor de Inglês (en) para Português (pt)
translator = Translator(from_lang="en", to_lang="pt")

# 3. Passamos a STRING para o tradutor
translation = translator.translate(fato_em_ingles)

print(f"Fato do gato: {translation}")