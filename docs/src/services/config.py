import os 
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = ""
    SUBSCRIPTION_KEY = ""
    AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=diolabsdocsdeveastus001;AccountKey=wGIf0Cd/nFXGuTxzDUnONCTOlSd12moqrbLUbe/KL1cwB+ncauiDCO6QL6TI7kOipWS8O9F8ln6D+AStYmTMbg==;EndpointSuffix=core.windows.net "
    CONTAINER_NAME = "cartoes"