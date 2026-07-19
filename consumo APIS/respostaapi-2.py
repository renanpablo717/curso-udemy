import requests

img = "https://blog.back4app.com/wp-content/uploads/2023/05/back4app-python-cover.webp"

resp = requests.get(img)

print(resp.status_code)

with open("image.webp", "wb") as webp:
    webp.write(resp.content)