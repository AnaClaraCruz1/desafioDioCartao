import streamlit as st
from services.blobs.service import upload_blob
from services.credit_card_service import analize_credit_card

def configure_interface():
    st.title("upload de arquivos DIO - desafio 1 -Azure - Fake Docs")
    uploaded_file = st.file_uploader("EScolha um arquivo", type = ["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        fileName = uploaded_file.name
        blob_url = upload_blob(upload_file, fileName)
        if blob_url: 
            st.write(f"Arquivo{fileName} enciado com sucesso para o Azure Blob Storange")
            credit_card_info = analize_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName}para o Azure Blob Storage")    
        
def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption= "imagem enviada", use_column_width=True)
    st.write("Informações de cartão de crédito encontradas: ")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color:green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do titular: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
        st.write(f"Dta de Validade: {credit_card_info['expiry_date']}")
    else:
        st.markdown(f"<h1> style= 'color: red;>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("este não é um cartão de crédito váçido")
        
if __name__ == "__main__":
  configure_interface()       