import os
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/hello")
def hello():
    try:
        # Ortam değişkenlerini kontrol et
        host = os.environ.get("POSTGRES_HOST")
        dbname = os.environ.get("POSTGRES_DATABASE")
        user = os.environ.get("POSTGRES_USERNAME")
        password = os.environ.get("POSTGRES_PASSWORD")
        #test
        # Hatalı ya da eksikse logla
        if not all([host, dbname, user, password]):
            return f"Missing environment variables. Host={host}, DB={dbname}, User={user}, Password={'SET' if password else 'MISSING'}"

        # Bağlantı kur
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            sslmode='require'
        )
        cur = conn.cursor()
        cur.execute("SELECT 'Hello from DB!'")
        result = cur.fetchone()[0]
        return result
    except Exception as e:
        return f"Connection failed: {str(e)}"

if __name__ == "__main__":
    app.run()
