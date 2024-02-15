from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    id = 1640702286
    return f'Hello, BU! {id}'

if __name__ == '__main__':
    app.run(debug=False, port=8000)