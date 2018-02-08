import json
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


with open('config.json', 'r') as f:
    config = json.load(f)

ip_address = config['HOST_IP']['IP_ADDRESS']
port_number = config['HOST_IP']['PORT_NUMBER']

if __name__ == "__main__":
    app.run(host=ip_address, port=port_number)
