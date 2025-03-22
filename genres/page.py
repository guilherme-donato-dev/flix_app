import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from .service import GenreService

def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de gêneros: ')
        genres_df = pd.json_normalize(genres) #transforma um json em um dataframe, que é só o que a AgGrid aceit
        AgGrid(
            data = genres_df,
            reload_data=True,
            key='genres_grid',
            ) #AgGrid só aceita como parÂmetro um DataFrame
    else:
        st.warning('Nenhum gênero cadastrado.')

    st.title('Cadastrar um novo gênero: ')
    name= st.text_input('Nome do gênero')
    if st.button('Cadastrar'):
        new_genre = genre_service.create_genres(
            name=name,
        )
        if new_genre:
            st.rerun()
        else:
            st.error('Erro ao cadastrar, verifique os campos')