import requests

def push(remote_url):
    with open('.mygit/objects', 'rb') as f:
        response = requests.post(f"{remote_url}/push", data=f.read())
        print(response.text)

def pull(remote_url):
    response = requests.get(f"{remote_url}/pull")
    if response.status_code == 200:
        with open('.mygit/objects', 'wb') as f:
            f.write(response.content)
        print("Pulled changes successfully.")
