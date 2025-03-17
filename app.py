import streamlit as st


def main():
    st.set_page_config(
        page_title='Flix App - sua bíblia dos filmes!',
        page_icon='🦆',
        )
    st.title('Flix App')

    menu_options = st.sidebar.selectbox(
        'Selecione uma opção:',
        {'Início', 'Gêneros', 'Atores/Atrizes', 'Filmes', 'Avaliações'}
    )

    if menu_options == 'Início':
        st.write('Início')

    if menu_options == 'Gêneros':
        st.write('Gêneros')

    if menu_options == 'Atores/Atrizes':
        st.write('Atores/Atrizes')

    if menu_options == 'Filmes':
        st.write('Filmes')

    if menu_options == 'Avaliações':
        st.write('Avaliações')    

    st.divider()
    st.text_input("Nome do filme: "),
    st.button('Salvar')

if __name__ == '__main__':
    main()