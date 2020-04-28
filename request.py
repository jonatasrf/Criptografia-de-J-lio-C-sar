import requests
import json

URL = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=003c9c9e5cb0af8c1c444471fc3fab6a530ea0b0'

r = requests.get(URL).json()

with open('answer.json', 'w', encoding='utf-8') as f:
	json.dump(r, f, ensure_ascii=False, indent=4)
