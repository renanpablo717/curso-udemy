import requests 

resp = requests.get("https://google.com")

print(resp.status_code)

if resp.status_code < 400:
    #Seguir com o código
elif resp.status_code >= 400 and resp.status_code < 500:
    #Corrigir solicitação do cliente
    # 400 erro na solicitação
    # 401 Falta de autenticação
    # 403 Autenticação negada
    # 404 Recurso não encontrado
    # 405 Método não permitido(GET onde só pode POST)
    # 429 Requisições demasiadas
    print("Erro do cliente")
else:
    # Erro do servidor, execute novamente mais tarde
    print("Erro do servidor")

print(resp.headers)

