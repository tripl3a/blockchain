from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


host_ip = "127.0.0.1"

if __name__ == "__main__":
    app.run(host=host_ip, port=5000)
