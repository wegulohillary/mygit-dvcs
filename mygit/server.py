from flask import Flask, request

app = Flask(__name__)

@app.route('/push', methods=['POST'])
def push():
    with open('.mygit/objects', 'wb') as f:
        f.write(request.data)
    return "Push successful", 200

@app.route('/pull', methods=['GET'])
def pull():
    with open('.mygit/objects', 'rb') as f:
        data = f.read()
    return data, 200

if __name__ == '__main__':
    app.run(port=5000)
