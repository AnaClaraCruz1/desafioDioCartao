import os 
import streamlit as st
from ultils.Config import Config
from azure.storage.blob import BlobServiceClient

def upload(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob_file_name)
        return blob_client.url
    except Exception as ex:
        st.error(f"Erro ao enviar o arquivo para AZure Blob Storage: {ex}")
        return None
    