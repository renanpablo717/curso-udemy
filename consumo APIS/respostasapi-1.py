import requests

#resp = requests.get('https://google.com')
# O código faz uma requisição GET para o site do Google
#print(resp)


resp = requests.get('https://api.github.com/events')  # Faz uma requisição GET para a URL especificada
print(resp.json())  # Retorna o conteúdo da resposta em formato JSON (se aplicável )
# TIPOS DE RESPOSTAS:

#print(resp.text)  # Retorna o conteúdo da resposta em texto

#with open('google.html', 'wb') as file:
  #  st = resp.content.decode('latin-1')  # Decodifica o conteúdo da resposta em bytes para string
   # file.write(st.encode('utf-8'))  # Re-encode para UTF-8

#with open('google.html', 'w') as file:
  #  file.write(resp.text)  # Escreve o conteúdo da resposta em texto no arquivo

