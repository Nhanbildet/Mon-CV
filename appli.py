import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)
authenticator.login()

def accueil():
    st.title('Bienvenu sur le Bat site')
if st.session_state["authentication_status"]:
    with st.sidebar:
        st.write('Bienvenue Utilisateur')
        selection = option_menu(
            menu_title= 'Menu',
            options= ['Accueil', 'Photos'],
            icons= ['house', 'camera'],
            menu_icon= 'cast'
                    )
        authenticator.logout("Déconnexion")
# On indique au programme quoi faire en fonction du choix
    if selection == "Accueil": 
        st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés") 
        st.image("Wild.png")
    elif selection == "Photos":
        st.write("Bienvenue dans l'album ")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Le chat")
            st.image("cat.png")

        with col2:
            st.header("le chien")
            st.image("dog.png")

        with col3:
            st.header("le Loup")
            st.image("lou.png")
if st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")
if st.session_state["authentication_status"] is None:
        st.warning('Les champs username et mot de passe doivent être remplie')
# ... et ainsi de suite pour les autres pagess

