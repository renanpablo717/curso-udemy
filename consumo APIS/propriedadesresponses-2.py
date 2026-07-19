import requests 

resp = requests.get("https://google.com")


#Para saber o formato do retorno fazemos o seguinte:

print(resp.headers['Content-Type'])

formato = requests.get('https://blog.back4app.com/wp-content/uploads/2023/05/back4app-python-cover.webp').headers['Content-Type']

print(formato)

history = requests.get("https://google.com", allow_redirects=True).history

print(history)


