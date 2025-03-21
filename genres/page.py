import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

genres = [
    {
        'id' : 1,
        'name' : 'ação'
    },

    {
        'id' : 2,
        'name' : 'Comédia'
    },

    {
        'id' : 3,
        'name' : 'Terror'
    },
]
def show_genres():
    st.write('Lista de gêneros: ')

    AgGrid(
        data = pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid',
        

        ) #AgGrid só aceita como parÂmetro um DataFrame

    st.title('Cadastrar um novo gênero: ')
    name= st.text_input('Nome do gênero')
    if st.button('Cadastrar'):
        st.success(f'Gênero {name} cadastrado com sucesso.')