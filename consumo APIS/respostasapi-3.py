import requests
import json

resp = requests.get('https://api.github.com/events')

print(resp)

with open('github_events.json', 'w') as file:
    json.dump(resp.json(), file, indent=4)