import streamlit as st
from PIL import Image

st.set_page_config(page_title='Em_Desenvolvimento', layout="centered", initial_sidebar_state="auto")
image = Image.open('desenvolvimento.jpg')    
st.image(image, width=600)
st.title("Desenvolvedor: Massaki Igarashi")                 
