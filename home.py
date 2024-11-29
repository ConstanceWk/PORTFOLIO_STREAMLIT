import streamlit as st
import base64
from PIL import Image
import requests
from io import BytesIO
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuration de la page
st.set_page_config(
    page_title="Portfolio IA & ML", 
    page_icon="🚀",
    layout="wide"
)

# Styles personnalisés avec fond en dégradé
st.markdown("""
<style>
     .stApp {
        background: 
            linear-gradient(217deg, rgba(255,0,0,.1), rgba(255,0,0,0) 70.71%),
            linear-gradient(127deg, rgba(147,112,219,.1), rgba(147,112,219,0) 70.71%),
            linear-gradient(336deg, rgba(178,223,238,.1), rgba(178,223,238,0) 70.71%),
            radial-gradient(circle at 50% 0%, #f5e6ff, transparent 70%),
            radial-gradient(circle at 0% 100%, #e6f0ff, transparent 70%),
            radial-gradient(circle at 100% 100%, #fff0f5, transparent 70%);
        background-size: 400% 400%, 400% 400%, 400% 400%, 200% 200%, 200% 200%, 200% 200%;
        animation: 
            gradient-shift 15s ease infinite,
            pulse 5s ease-in-out infinite;
    }

    @keyframes gradient-shift {
        0% { background-position: 0% 50%, 100% 50%, 50% 100%, 0% 0%, 0% 100%, 100% 100%; }
        50% { background-position: 100% 50%, 0% 50%, 50% 0%, 100% 50%, 100% 0%, 0% 0%; }
        100% { background-position: 0% 50%, 100% 50%, 50% 100%, 0% 0%, 0% 100%, 100% 100%; }
    }

    @keyframes pulse {
        0% { opacity: 0.95; }
        50% { opacity: 1; }
        100% { opacity: 0.95; }
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
            
        
    .interactive-element {
        transform-style: preserve-3d;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .interactive-element:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 12px 20px rgba(0,0,0,0.15);
    }
              
    .intro-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin: 20px 0;
        transform-style: preserve-3d;
        transition: all 0.3s ease;
    }

    .intro-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px 0 rgba(31, 38, 135, 0.15);
    }

    .intro-title {
        margin: 0;
        background: linear-gradient(90deg, #8A4FFF, #E0AEFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 1.8em;
    }

    .intro-text {
        font-size: 1.2em;
        line-height: 1.6;
        color: #4a4a4a;
        margin-bottom: 0;
        padding-left: 20px;
        border-left: 4px solid #8A4FFF;
    }

    /* Style pour la sidebar */
    .css-1d391kg {  /* Classe de la sidebar */
        background: linear-gradient(to bottom, rgba(138, 79, 255, 0.1), rgba(224, 174, 255, 0.1)) !important;
        backdrop-filter: blur(10px);
    }

    .streamlit-expanderHeader {
        background-color: rgba(138, 79, 255, 0.05) !important;
    }

    /* Style pour les boutons radio dans la sidebar */
    .stRadio > label {
        color: #8A4FFF !important;
        font-weight: 500;
    }

    .stRadio > div[role="radiogroup"] > label {
        background-color: rgba(138, 79, 255, 0.1) !important;
        border-radius: 10px;
        padding: 10px 15px;
        margin: 5px 0;
        transition: all 0.3s ease;
    }

    .stRadio > div[role="radiogroup"] > label:hover {
        background-color: rgba(138, 79, 255, 0.2) !important;
        transform: translateX(5px);
    }

    /* Style pour le titre de la sidebar */
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.1) !important;
    }

    .sidebar .sidebar-content h1 {
        color: #8A4FFF !important;
        font-size: 1.5em !important;
        margin-bottom: 20px !important;
        border-bottom: 2px solid rgba(138, 79, 255, 0.2);
        padding-bottom: 10px;
    }
    
         
    .st-emotion-cache-pk3ts8 {
        min-height: 60px !important;
        width: 100% !important;
        background: rgba(138, 79, 255, 0.1) !important;
        padding: 15px !important;
        margin: 8px 0 !important;
        border-radius: 15px !important;
        transition: all 0.3s ease;
    }

    /* Style pour le conteneur de navigation */
    [data-testid="stSidebar"] {
        background: rgba(138, 79, 255, 0.15) !important;
        backdrop-filter: blur(10px);
    }

    section[data-testid="stSidebar"] > div {
        padding: 2rem 1rem;
    }

    /* Style pour le conteneur des boutons radio */
    .st-emotion-cache-16idsys p {
        font-size: 1.1em;
        color: #6A5ACD;
    }

    /* Style hover pour les boutons */
    .st-emotion-cache-pk3ts8:hover {
        background: rgba(138, 79, 255, 0.2) !important;
        transform: translateX(5px);
    }
            



    /* Masquer la barre d'outils */
    .stApp header {
        display: none !important;
    }

    /* Ajuster l'espacement en haut */
    .stApp > div:first-child {
        margin-top: 0 !important;
    }
   
    
</style>
""", unsafe_allow_html=True)

# Fonction pour afficher l'image de profil
def display_profile_image():
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.markdown("""
        <div style="display: flex; justify-content: center;">
            <img src="https://avataaars.io/?avatarStyle=Circle&topType=LongHairStraight&accessoriesType=None&hairColor=Blonde&facialHairType=Blank&clotheType=Hoodie&clotheColor=PastelBlue&eyeType=Default&eyebrowType=Default&mouthType=Smile&skinColor=Light" 
                 alt="Photo de Profil" 
                 class="profile-image"
                 style="width: 250px; height: 250px; object-fit: cover;"
            >
        </div>
        """, unsafe_allow_html=True)


def create_neural_network_viz():
    # Création des nœuds
    num_layers = 4
    nodes_per_layer = [4, 6, 6, 3]
    nodes_x = []
    nodes_y = []
    nodes_z = []
    edge_x = []
    edge_y = []
    edge_z = []
    
    # Positionnement des nœuds
    for i, num_nodes in enumerate(nodes_per_layer):
        layer_x = np.repeat(i, num_nodes)
        layer_y = np.linspace(-1, 1, num_nodes)
        layer_z = np.zeros(num_nodes)
        
        nodes_x.extend(layer_x)
        nodes_y.extend(layer_y)
        nodes_z.extend(layer_z)
        
        # Connexions entre les couches
        if i < len(nodes_per_layer) - 1:
            for j in range(num_nodes):
                for k in range(nodes_per_layer[i + 1]):
                    edge_x.extend([layer_x[j], i + 1, None])
                    edge_y.extend([layer_y[j], np.linspace(-1, 1, nodes_per_layer[i + 1])[k], None])
                    edge_z.extend([0, 0, None])
    
    # Création des traces
    edges_trace = go.Scatter3d(
        x=edge_x, y=edge_y, z=edge_z,
        mode='lines',
        line=dict(color='#8A4FFF', width=1),
        opacity=0.5
    )
    
    nodes_trace = go.Scatter3d(
        x=nodes_x, y=nodes_y, z=nodes_z,
        mode='markers',
        marker=dict(
            symbol='circle',
            size=8,
            color=['#E6E6FA'] * nodes_per_layer[0] +  # Input layer
                  ['#8A4FFF'] * (nodes_per_layer[1] + nodes_per_layer[2]) +  # Hidden layers
                  ['#FF69B4'] * nodes_per_layer[3],  # Output layer
            line=dict(color='#fff', width=0.5)
        ),
        text=(['Input'] * nodes_per_layer[0] +
              ['Hidden'] * (nodes_per_layer[1] + nodes_per_layer[2]) +
              ['Output'] * nodes_per_layer[3])
    )
    
    # Layout
    layout = go.Layout(
        title=dict(
            text='Réseau de Neurones : De la Donnée à l\'Innovation',
            y=0.95,
            font=dict(size=24, color='#8A4FFF')
        ),
        showlegend=False,
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            camera=dict(
                up=dict(x=0, y=0, z=1),
                center=dict(x=0, y=0, z=0),
                eye=dict(x=2, y=2, z=2)
            )
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0)
    )
    
    fig = go.Figure(data=[edges_trace, nodes_trace], layout=layout)
    return fig

def home():
    st.markdown('<h1 class="main-title">Portfolio de Constance Walusiak</h1>', unsafe_allow_html=True)

    display_profile_image()

    st.markdown("""
    <div class="intro-card" style="
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin: 20px 0;
        transform-style: preserve-3d;
        transition: all 0.3s ease;
    ">
        <div style="
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 20px;
        ">
            <span style="font-size: 2em;">👋 </span>
            <h2 style="
                margin: 0;
                background: linear-gradient(90deg, #8A4FFF, #E0AEFF);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size: 1.8em;
            ">Bonjour! Je suis une étudiante en Data et Intelligence Artificielle</h2>
        </div>
        <p style="
            font-size: 1.2em;
            line-height: 1.6;
            color: #4a4a4a;
            margin-bottom: 0;
            padding-left: 20px;
            border-left: 4px solid #8A4FFF;
        ">
            👩‍💻 Mon portfolio présente mon parcours professionnel, mais également mes projets en Machine Learning et Intelligence Artificielle. Spécialisée dans l'analyse de données complexes, je développe des solutions innovantes en NLP, Computer Vision et Deep Learning. Découvrez mes réalisations et compétences techniques, illustrant ma passion pour l'intelligence artificielle et sa capacité à résoudre des défis concrets.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="intro-card fun-card" style="
    background: linear-gradient(145deg, rgba(255,255,255,0.7), rgba(255,255,255,0.4));
    border: 2px dashed #8A4FFF;
    margin-top: 30px;
    ">
    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
        <span style="font-size: 2em;">🚀</span>
        <h3 style="
            margin: 0;
            background: linear-gradient(90deg, #8A4FFF, #E0AEFF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 1.5em;
        ">Pourquoi l'IA et moi, on forme une équipe de choc?</h3>
    </div>
    <p style="
        font-size: 1.1em;
        line-height: 1.6;
        color: #4a4a4a;
        font-style: italic;
    ">
        Imaginez une Data Scientist qui transforme les algorithmes en véritables super-héros du quotidien ! 🦸‍♀️
        <br><br>
        Mon secret ? Je ne me contente pas de coder, je donne vie aux données ! Que ce soit pour prédire le prochain best-seller ou pour comprendre pourquoi votre chat préfère le coussin à son panier, mes modèles sont là pour résoudre vos mystères.
        <br><br>
        <span style="color: #8A4FFF; font-weight: bold;">Ma mission :</span> Rendre l'IA aussi accessible qu'une conversation avec votre meilleur ami, mais en plus intelligent (ne le dites à personne ! 🤫)
    </p>
    </div>
    """, unsafe_allow_html=True)  
    st.markdown("""
    <div class="intro-card fun-card" style="
    background: linear-gradient(145deg, rgba(255,255,255,0.7), rgba(255,255,255,0.4));
    padding: 20px;
    text-align: center;
    margin-top: 30px;
    ">
    <div style="font-size: 3em; margin-bottom: 15px;">
        🤖 + 👩 = 💡
    </div>
    <div style="
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        margin: 20px 0;
    ">
        <div style="
            background: rgba(138,79,255,0.1);
            padding: 15px;
            border-radius: 10px;
            text-align: center;
        ">
            <span style="font-size: 2em;">🎯</span>
            <p style="margin: 5px 0; font-weight: bold;">Précision</p>
            <p style="font-size: 0.9em;">99.9% du temps... sauf quand je regarde Netflix 😅</p>
        </div>
        <div style="
            background: rgba(138,79,255,0.1);
            padding: 15px;
            border-radius: 10px;
            text-align: center;
        ">
            <span style="font-size: 2em;">⚡</span>
            <p style="margin: 5px 0; font-weight: bold;">Rapidité</p>
            <p style="font-size: 0.9em;">Plus rapide que mon café du matin ☕</p>
        </div>
        <div style="
            background: rgba(138,79,255,0.1);
            padding: 15px;
            border-radius: 10px;
            text-align: center;
        ">
            <span style="font-size: 2em;">🎨</span>
            <p style="margin: 5px 0; font-weight: bold;">Créativité</p>
            <p style="font-size: 0.9em;">Mon IA a plus d'idées que moi un lundi matin 🌈</p>
        </div>
    </div>
    <div style="
        font-size: 1.2em;
        color: #8A4FFF;
        font-weight: bold;
        margin-top: 20px;
    ">
        Mon super pouvoir ? Transformer le café en code ! ☕→ 💻
    </div>
    </div>
    """, unsafe_allow_html=True)


    st.markdown('<div class="intro-card">', unsafe_allow_html=True)
    fig = create_neural_network_viz()
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    
    
    PROJETS = [
        {
            "titre": "Détection de Sentiment sur Réseaux Sociaux",
            "description": "Modèle de NLP utilisant BERT pour analyser les sentiments en temps réel",
            "technologies": ["Python", "Transformers", "TensorFlow"],
            "impact": "Précision 95%",
            "badge": "🤖 NLP"
        },
        {
            "titre": "Prédiction de Prix Immobiliers",
            "description": "Système de Machine Learning prédisant les prix avec une précision de 95%",
            "technologies": ["Scikit-learn", "Pandas", "Seaborn"],
            "impact": "+30% ROI",
            "badge": "📈 ML"
        },
        {
            "titre": "Recommandation de Contenu IA",
            "description": "Algorithme de recommandation personnalisé basé sur le filtrage collaboratif",
            "technologies": ["PyTorch", "NumPy", "Recommenders"],
            "impact": "+45% Engagement",
            "badge": "🎯 RecSys"
        }
    ]

    # Remplacez la fonction projets() existante par celle-ci
    def projets():
        st.markdown('<h2 class="section-title">🚀 Mes Projets</h2>', unsafe_allow_html=True)
        
        for projet in PROJETS:
            st.markdown(f"""
            <div class="project-card interactive-element" style="
                background: linear-gradient(145deg, rgba(255,255,255,0.7), rgba(255,255,255,0.4));
                backdrop-filter: blur(15px);
                border-radius: 15px;
                padding: 20px;
                margin-bottom: 20px;
                transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            ">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="color: #8A4FFF;">{projet['titre']}</h3>
                    <span style="
                        background-color: rgba(138,79,255,0.1);
                        padding: 5px 10px;
                        border-radius: 20px;
                        font-size: 0.9em;
                    ">
                        {projet['badge']}
                    </span>
                </div>
                <p>{projet['description']}</p>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <b>Technologies:</b> {", ".join(projet['technologies'])}
                    </div>
                    <div style="
                        background-color: rgba(138,79,255,0.2);
                        color: #8A4FFF;
                        padding: 5px 10px;
                        border-radius: 20px;
                        font-size: 0.9em;
                    ">
                        Impact: {projet['impact']}
                    </div>
                </div>
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