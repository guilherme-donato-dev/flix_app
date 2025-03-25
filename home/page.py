import streamlit as st
from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Estatística de filmes')

    st.subheader('Total de filmes cadastrados: ')
    st.write(movie_stats['total_movies'])

    st.subheader('Média geral de estrelas nas avaliações: ')
    st.write(movie_stats['average_stars'])