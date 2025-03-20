import requests


class Auth:

    def __init__(self): #método init o py reconhece que o método inicializador da classe
        self.__base_url='donatodev.pythonanywhere.com/api/v1/' #a pep 8 recomenda que quando o método for utilizado somente dentro da própria classe, se começa com __ dois underline
        self.__auth_url=f'{self.__base_url}authentication/token/'

    def get_token(self, username, password):
        auth_payload = {
            'username' : username,
            'password' : password,
        }
        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )
        if auth_payload.status_code == 200:
            return auth_response.json()
        return{'error' : f'Erro ao autenticar. Status code: {auth_response.status_code}'}