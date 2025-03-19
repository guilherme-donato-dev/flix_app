import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


actors = [
    {
        'id' : 1,
        'name' : 'Dicrapio'
    },

    {
        'id' : 2,
        'name' : 'Suzana'
    },

    {
        'id' : 3,
        'name' : 'Cristian'
    },
]
def show_actors():
    st.write('Lista de atores/atrizes: ')

    AgGrid(
        data = pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid',
        

        ) #AgGrid só aceita como parÂmetro um DataFrame

    st.title('Cadastrar um novo ator/atriz: ')
    name= st.text_input('Nome do ator/atriz')
    if st.button('Cadastrar'):
        st.success(f'Filme {name} cadastrado com sucesso.')