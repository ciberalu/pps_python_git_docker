from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, mundo'

def frotar(n_frases: int = 1) -> list:
    return ["Esta es tu fortuna."] * n_frases

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def get_frases(n_frases):
    frases = frotar(n_frases)
    return jsonify(frases)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
