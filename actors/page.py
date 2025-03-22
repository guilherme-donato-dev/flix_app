import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from datetime import datetime
from .service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de atores/atrizes: ')
        actors_df = pd.json_normalize(actors) #função do pandas que transformajson em dataframe, que é o que o AgGrid aceita
        AgGrid(
            data = actors_df,
            reload_data=True,
            key='actors_grid',
            ) #AgGrid só aceita como parÂmetro um DataFrame
    else:
        st.warning('Nenhum ator/atriz encontrado')

    st.title('Cadastrar um novo ator/atriz: ')
    name= st.text_input('Nome do ator/atriz')
    birthday = st.date_input(
        label='Data de nascimento: ',
        value= datetime.today(),
        min_value=datetime(1600,1,1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    nationality_dropdown = ['BRAZIL', 'USA', 'SPAIN', 'ENGLAND']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown,
    )
    if st.button('Cadastrar'):
        new_actor = actor_service.create_actors(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar. Verifique novamente os campos')