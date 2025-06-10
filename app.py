import os
from flask import Flask
import psycopg2
#helo
app = Flask(__name__)

@app.route("/hello")
def hello():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("POSTGRES_HOST"),
            dbname=os.environ.get("POSTGRES_DATABASE"),
            user=os.environ.get("POSTGRES_USERNAME"),
            password=os.environ.get("POSTGRES_PASSWORD")
        )
        cur = conn.cursor()
        cur.execute("SELECT 'Hello from DB!'")
        result = cur.fetchone()[0]
        return result
    except Exception as e:
        return f"Connection failed: {str(e)}"


if __name__ == "__main__":
    app.run()
