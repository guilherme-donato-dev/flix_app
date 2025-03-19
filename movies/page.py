import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


movies = [
    {
        'id' : 1,
        'name' : 'A felicidade não se compra'
    },

    {
        'id' : 2,
        'name' : 'Central do Brasil'
    },

    {
        'id' : 3,
        'name' : 'UM morto MUITO louco'
    },
]
def show_movies():
    st.write('Lista de filmes: ')

    AgGrid(
        data = pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid',
        

        ) #AgGrid só aceita como parÂmetro um DataFrame
