import requests
import streamlit as st
from login.service import logout


class MovieRepository:
    def __init__(self):
        self.__base_url =  'https://donatodev.pythonanywhere.com/api/v1/'
        self.__movies_url = f'{self.__base_url}movies/'
        self.__headers = {
            'Authorization' : f'Bearer {st.session_state.token}' #aqui ele está passando o token, que está salvo no session_state, até ele vencer, depois de 24 horas.
        }

    def get_movies(self):
        response = requests.get(
            self.__movies_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
        raise Exception(f'Erro ao obter os dados da API. Status code: {response.status_code}')
    
    def create_movie(self, movie):
        response = requests.post(
            self.__movies_url,
            headers=self.__headers,
            data=movie,
        )
        if response.status_code == 201:  #muda para 201 que o status.code 201 é created com sucesso 
            return response.json()
        if response.status_code == 401:
            logout()
        raise Exception(f'Erro ao obter os dados da API. Status code: {response.status_code}')
    
    def get_movie_stats(self):
        response = requests.get(
            f'{self.__movies_url}stats/',
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
        raise Exception(f'Erro ao obter os dados da API. Status code: {response.status_code}')