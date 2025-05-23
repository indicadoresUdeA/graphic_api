from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return r"Send a POST request to /login with this body: \{\"user\": \"your_user_here\", \"password\": \"your_password_here\"\}"
