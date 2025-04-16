from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Azure App Service 🚀"

@app.route("/db")
def db_check():
    return "PostgreSQL test endpoint 🎯"

if __name__ == "__main__":
    app.run()
