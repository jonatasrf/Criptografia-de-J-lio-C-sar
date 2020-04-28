import requests
import json

def send_form():
    POST = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=003c9c9e5cb0af8c1c444471fc3fab6a530ea0b0"
    answer = {'answer': open('answer.json', 'rb')}
    submit = requests.post(POST, files=answer)
    print(submit.headers)

send_form()