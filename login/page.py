import streamlit as st
from login.service import login


def show_login():
    st.title('Login')

    username = st.text_input('Usuário')
    password = st.text_input(
        label='Senha',
        type='password',
    )

    #aqui quando o usuário clicar no button, ele vai chamar a def login, com os usuários passados lá.
    if st.button('Login'):
        login(
            username=username,
            password=password
        )