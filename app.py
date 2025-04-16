from flask import Flask
import psycopg2
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

# Azure Key Vault bağlantısı
VAULT_URL = "https://hellovaultgr1.vault.azure.net/"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=VAULT_URL, credential=credential)

# PostgreSQL bilgilerimizi vault'tan çekiyoruz
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
            host=db_host,
            dbname=db_name,
            user=db_user,
            password=db_pass
        )
        conn.close()
        return "PostgreSQL test endpoint 🎯"
    except Exception as e:
        print("💥 DATABASE CONNECTION ERROR 💥")
        print(str(e))  # hata detayını log stream'e bastırır
        return f"Connection failed: {str(e)}"


if __name__ == "__main__":
    app.run()
