from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return (
        "Servicio de gráficos.\n"
        "1. POST /login    → obtiene un JWT.\n"
        "2. POST /service/<pie-chart|radar-chart|...> con JSON y header Bearer token."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)