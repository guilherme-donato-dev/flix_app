import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorService
from movies.service import MovieService
from genres.service import GenreService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write('Lista de filmes: ')

        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])

        AgGrid(
            data = movies_df,
            reload_data=True,
            key='movies_grid',
            ) #AgGrid só aceita como parÂmetro um DataFrame
    else:
        st.warning('Nenhum filme cadastrado.')

    st.title('Cadastrar um novo filme: ')

    title = st.text_input('Filme')
    release_date = st.date_input(
        label='Data de lançamento',
        value= datetime.today(),
        min_value=datetime(1900,1,1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['name'] : genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Gênero', list(genre_names.keys()))
    
    actors_service = ActorService()
    actors = actors_service.get_actors()
    actor_names = {actor['name'] : actor['id'] for actor in actors}
    selected_actors_names = st.multiselect('Atores/atrizes', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actors_names]

    resume = st.text_area(label='Resumo')

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadastrar. Verifique novamente os campos.')