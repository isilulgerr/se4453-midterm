from flask import Flask
import psycopg2
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

# Azure Key Vault bağlantısı
VAULT_URL = "https://hellovaultgr1.vault.azure.net/"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=VAULT_URL, credential=credential)

# PostgreSQL bilgileri vault’tan çekiliyor
PG_HOST = client.get_secret("POSTGRES-HOST").value
PG_USERNAME = client.get_secret("POSTGRES-USERNAME").value
PG_PASSWORD = client.get_secret("POSTGRES-PASSWORD").value
PG_DB = client.get_secret("POSTGRES-DATABASE").value

@app.route("/")
def home():
    return "Hello from Azure App Service 🚀"

@app.route("/db")
def db_test():
    try:
        conn = psycopg2.connect(
            host=PG_HOST,
            dbname=PG_DB,
            user=PG_USERNAME,
            password=PG_PASSWORD
        )
        conn.close()
        return "PostgreSQL test endpoint 🎯"
    except Exception as e:
        print("💥 DATABASE CONNECTION ERROR 💥")
        print(str(e))
        return f"Connection failed: {str(e)}"

if __name__ == "__main__":
    app.run()
