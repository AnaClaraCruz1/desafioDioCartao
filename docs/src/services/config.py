import os 
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = ""
    SUBSCRIPTION_KEY = ""
    AZURE_STORAGE_CONNECTION_STRING = ""
    CONTAINER_NAME = "cartoes"