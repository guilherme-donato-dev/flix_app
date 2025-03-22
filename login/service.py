import streamlit as st
from api.service import Auth

#pedindo para o sistema de authentication retornar um token para ele com a função get_token para o usuário que tentou fazer login
def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(
        username=username,
        password=password,
    )
    if response.get('error'):
        st.error(f'Falha ao realizar o login {response.get('error')}')
    else:
        st.session_state.token = response.get('access') #session_state.nomedavariavel. aqui estamos pegando so o token de access
        st.rerun() #rerun é basicamente pra renderizar a tela novamente

#basicamente ela limpa todas as chaves(tokens) que estão no session_state e dps recarrega a pag
def logout():
    for key in st.session_state.key():
        del st.session_state[key]
    st.rerun()