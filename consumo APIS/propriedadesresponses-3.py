import requests

primeiro = requests.get('https://httpbin.org/status/401').reason

segundo = requests.get('https://google.com/status/400').reason

terceiro = requests.get('https://google.com/status/429').reason

print(primeiro)
print(segundo)
print(terceiro)