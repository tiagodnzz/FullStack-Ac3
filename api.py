import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/api/ac3', methods=['POST'])
def ac3():

    json = request.get_json()
    nome = json['nome'].upper()
    sobrenome = json['sobrenome'].upper()
    cargo = json['cargo'].upper()

    return jsonify(nome=nome, sobrenome=sobrenome, cargo=cargo)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

