import streamlit as st
import requests
from login.service import logout


class ActorRepository:
    
    def __init__(self):
        self.__base_url = 'https://donatodev.pythonanywhere.com/api/v1/'
        self.__actors_url= f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization' : f'Bearer {st.session_state.token}' #aqui ele está passando o token, que está salvo no session_state, até ele vencer, depois de 24 horas.
        }

    def get_actors(self):
        response = requests.get(
            self.__actors_url,
            headers=self.__headers,  #o headers eu passo o token que eu pegue na def __init__
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
        raise Exception(f'Erro ao obter os dados da API. Status code: {response.status_code}')
    
    def create_actor(self, actor):
        response = requests.post(
            self.__actors_url,
            headers=self.__headers,
            data=actor,
        )
        if response.status_code == 201:  #muda para 201 que o status.code 201 é created com sucesso 
            return response.json()
        if response.status_code == 401:
            logout()
        raise Exception(f'Erro ao obter os dados da API. Status code: {response.status_code}')