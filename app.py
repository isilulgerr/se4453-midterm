from flask import Flask
import psycopg2
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

# connect to Azure Key Vault using default credentials
VAULT_URL = "https://hellovaultgr1.vault.azure.net/"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=VAULT_URL, credential=credential)

# retrieve PostgreSQL credentials from Key Vault
PG_HOST = client.get_secret("POSTGRES-HOST").value
PG_USERNAME = client.get_secret("POSTGRES-USERNAME").value
PG_PASSWORD = client.get_secret("POSTGRES-PASSWORD").value
PG_DB = client.get_secret("POSTGRES-DATABASE").value

@app.route("/")
def home():
    # basic home route to confirm the service is running
    return "Hello from Azure App Service 🚀"

@app.route("/hello")
def hello():
    try:
        # attempt to connect to PostgreSQL using secrets from Key Vault
        conn = psycopg2.connect(
            host=PG_HOST,
            dbname=PG_DB,
            user=PG_USERNAME,
            password=PG_PASSWORD,
            connect_timeout=5  # timeout for the connection attempt
        )
        conn.close()
        # return success message if connection is successful
        return "PostgreSQL test endpoint. Hello, 4453 - Midterm Project! from Işıl and Özge 👩‍💻👩‍💻"
    except Exception as e:
        # log and return error message if connection fails
        print("DATABASE CONNECTION ERROR!")
        print(str(e))
        return f"Connection failed: {str(e)}"

if __name__ == "__main__":
    # run the flask app in local development
    app.run()
