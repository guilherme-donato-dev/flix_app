import streamlit as st

st.set_page_config(
    page_title='Flix App - sua bíblia dos filmes!',
    page_icon='🦆',
    )
st.title('Flix App')
st.divider()
title = st.text_input("Nome do filme: ", "A trança do careca")
st.button('Salvar')