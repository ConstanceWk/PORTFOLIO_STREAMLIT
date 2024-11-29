import streamlit as st
import base64
from PIL import Image
import requests
from io import BytesIO

# Configuration de la page
st.set_page_config(
    page_title="Portfolio IA & ML", 
    page_icon="🚀",
    layout="wide"
)

# Styles personnalisés avec fond en dégradé
st.markdown("""
<style>
    /* Fond en dégradé pour toute la page */
    .stApp {
        background: linear-gradient(
            -45deg, 
            #f3e7e9,    /* Rose très doux */
            #d3d3e7,    /* Lilas pastel */
            #c1e1c1,    /* Vert menthe très pâle */
            #d1e8e4     /* Turquoise ultra léger */
        );
        background-size: 400% 400%;
        animation: gradient-animation 20s ease infinite;
        height: 100vh;
    }

    /* Animation du dégradé */
    @keyframes gradient-animation {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .main-title {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #8A4FFF, #E0AEFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 20px 0;
    }
    .section-title {
        color: #6A5ACD;
        border-bottom: 3px solid rgba(106, 90, 205, 0.3);
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .project-card {
        background: rgba(255, 255, 255, 0.6);  /* Légère transparence pour laisser voir le dégradé */
        backdrop-filter: blur(10px);  /* Effet de verre */
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.2);
    }
    .project-card:hover {
        transform: scale(1.03);
        background: rgba(255, 255, 255, 0.8);
        box-shadow: 0 8px 15px rgba(0,0,0,0.15);
    }
    
    /* Style pour l'image de profil */
    .profile-image {
        border-radius: 50%;
        border: 4px solid white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: transform 0.3s ease;
    }
    .profile-image:hover {
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# Fonction pour afficher l'image de profil
def display_profile_image():
    # Utilisation d'un placeholder, remplacez par votre propre image
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.markdown("""
        <div style="display: flex; justify-content: center;">
            <img src="https://avataaars.io/?avatarStyle=Circle&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=Heather&eyeType=Happy&eyebrowType=Default&mouthType=Smile&skinColor=Light" 
                 alt="Photo de Profil" 
                 class="profile-image"
                 style="width: 250px; height: 250px; object-fit: cover;"
            >
        </div>
        """, unsafe_allow_html=True)

# Reste du code identique aux versions précédentes
def home():
    st.markdown('<h1 class="main-title">Portfolio de Machine Learning & IA</h1>', unsafe_allow_html=True)
    
    display_profile_image()
    
    st.markdown("""
    ### 👋 Bonjour! Je suis un Data Scientist passionné par l'Intelligence Artificielle
    
    Bienvenue dans mon univers de données et d'apprentissage automatique. Je transforme des problèmes complexes en solutions innovantes grâce à l'IA et au Machine Learning.
    """)

# Section Projets
def projets():
    st.markdown('<h2 class="section-title">🚀 Mes Projets</h2>', unsafe_allow_html=True)
    
    projets_list = [
        {
            "titre": "Détection de Sentiment sur Réseaux Sociaux",
            "description": "Modèle de NLP utilisant BERT pour analyser les sentiments en temps réel",
            "technologies": ["Python", "Transformers", "TensorFlow"]
        },
        {
            "titre": "Prédiction de Prix Immobiliers",
            "description": "Système de Machine Learning prédisant les prix avec une précision de 95%",
            "technologies": ["Scikit-learn", "Pandas", "Seaborn"]
        },
        {
            "titre": "Recommandation de Contenu IA",
            "description": "Algorithme de recommandation personnalisé basé sur le filtrage collaboratif",
            "technologies": ["PyTorch", "NumPy", "Recommenders"]
        }
    ]
    
    for projet in projets_list:
        st.markdown(f"""
        <div class="project-card">
            <h3>{projet['titre']}</h3>
            <p>{projet['description']}</p>
            <b>Technologies:</b> {', '.join(projet['technologies'])}
        </div>
        """, unsafe_allow_html=True)

# Section Compétences
def competences():
    st.markdown('<h2 class="section-title">💡 Compétences</h2>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    skills = [
        ("Machine Learning", 90),
        ("Deep Learning", 85), 
        ("Python", 95),
        ("TensorFlow", 80),
        ("NLP", 75),
        ("Data Visualization", 85)
    ]
    
    for i, (skill, level) in enumerate(skills):
        cols[i % 3].markdown(f"""
        <div class="project-card" style="text-align:center;">
            <h4>{skill}</h4>
            <div style="background-color: #E6E6FA; border-radius: 10px;">
                <div style="width:{level}%; background-color: #8A4FFF; height:20px; border-radius: 10px;"></div>
            </div>
            <p>{level}%</p>
        </div>
        """, unsafe_allow_html=True)

# Navigation principale
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choisissez une section", 
                             ["Accueil", "Projets", "Compétences"])
    
    if page == "Accueil":
        home()
    elif page == "Projets":
        projets()
    else:
        competences()

if __name__ == "__main__":
    main()