import streamlit as st
from home import *
from projects import *
from skills import *
from parcours import *
from style import *

def main():
    st.set_page_config(
        page_title="Portfolio de Constance",
        page_icon="🚀",
        layout="wide"
    )
    
    # Chargement des styles
    st.markdown(load_css(), unsafe_allow_html=True)
    
    # Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Choisissez une section",
        ["Accueil", "Mon Parcours", "Projets", "Compétences"]
    )
    
    # Routing
    if page == "Accueil":
        show_home()
    elif page == "Mon Parcours":
        show_parcours()
    elif page == "Projets":
        show_projects()
    else:
        show_skills()

if __name__ == "__main__":
    main()