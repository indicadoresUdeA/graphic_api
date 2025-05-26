from flask import Flask, request
from . import main

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return (
        "Servicio de gráficos.\n"
        "POST /service/<module> con JSON."
    )

@app.route('/service/<module>', methods=['POST'])
def service(module):
    data = request.get_json(force=True) or {}
    try:
        return main.execute(module, data)
    except ValueError:
        return 'Module not found', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
