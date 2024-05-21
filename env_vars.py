import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    print("Loaded .env file from:", dotenv_path)
else:
    print(".env file not found at:", dotenv_path)

BLASTSCAN_API_KEY = os.getenv("BLASTSCAN_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")