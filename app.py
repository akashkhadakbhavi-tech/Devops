from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello! Flask application is running successfully."


@app.route("/test")
def test():
    return "Jenkins Flask test PASSED"


@app.route("/health")
def health():
    return {
        "status": "UP",
        "message": "Flask application is healthy"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
