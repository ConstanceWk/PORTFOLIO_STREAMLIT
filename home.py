import streamlit as st
import random
import json

# Configuration de la page
st.set_page_config(
    page_title="Portfolio IA & ML", 
    page_icon="🚀",
    layout="wide"
)

# Style CSS Ultra Avancé
st.markdown("""
<style>
    :root {
        --primary-color: #8A4FFF;
        --secondary-color: #E0AEFF;
        --background-gradient: linear-gradient(
            -45deg, 
            #f3e7e9,    
            #d3d3e7,    
            #c1e1c1,    
            #d1e8e4     
        );
    }

    /* Fond holographique */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at top right, rgba(138,79,255,0.1), transparent 40%),
            radial-gradient(circle at bottom left, rgba(224,174,255,0.1), transparent 40%);
        pointer-events: none;
        z-index: -1;
    }

    /* Animation de particules complexe */
    @keyframes particle-dance {
        0% { 
            transform: translateY(0) rotate(0deg); 
            opacity: 0.3;
        }
        50% { 
            transform: translateY(-50px) rotate(180deg); 
            opacity: 0.7;
        }
        100% { 
            transform: translateY(0) rotate(360deg); 
            opacity: 0.3;
        }
    }

    .particle-layer {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -2;
        overflow: hidden;
    }

    .particle {
        position: absolute;
        background: radial-gradient(circle, 
            rgba(138,79,255,0.5), 
            rgba(224,174,255,0.2)
        );
        border-radius: 50%;
        animation: particle-dance linear infinite;
    }

    /* Effets de cartes 3D */
    .project-card {
        perspective: 1000px;
        transform-style: preserve-3d;
        transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .project-card:hover {
        transform: rotateX(10deg) rotateY(10deg) scale(1.05);
        box-shadow: 
            0 20px 40px rgba(0,0,0,0.15), 
            0 15px 30px rgba(138,79,255,0.1);
    }

    /* Titre holographique */
    @keyframes holographic-title {
        0%, 100% { 
            text-shadow: 
                0 0 10px rgba(138,79,255,0.5),
                0 0 20px rgba(224,174,255,0.3);
        }
        50% { 
            text-shadow: 
                0 0 20px rgba(138,79,255,0.7),
                0 0 40px rgba(224,174,255,0.5);
        }
    }

    .main-title {
        animation: 
            holographic-title 3s infinite alternate,
            title-shimmer 3s infinite alternate;
        background: linear-gradient(
            90deg, 
            var(--primary-color), 
            var(--secondary-color)
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Effets interactifs avancés */
    .interactive-element {
        transition: all 0.4s ease;
        cursor: pointer;
    }

    .interactive-element:hover {
        transform: scale(1.05) rotate(2deg);
    }

    /* Design responsif et dynamique */
    @media (max-width: 768px) {
        .project-card {
            transform: none !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Script JavaScript pour les particules dynamiques
st.markdown("""
<script>
function createParticles() {
    const particleLayer = document.createElement('div');
    particleLayer.classList.add('particle-layer');
    
    for(let i = 0; i < 50; i++) {
        const particle = document.createElement('div');
        particle.classList.add('particle');
        
        particle.style.width = `${Math.random() * 10 + 2}px`;
        particle.style.height = particle.style.width;
        particle.style.top = `${Math.random() * 100}%`;
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.animationDuration = `${Math.random() * 10 + 5}s`;
        particle.style.opacity = Math.random();
        
        particleLayer.appendChild(particle);
    }
    
    document.body.appendChild(particleLayer);
}

// Appel au chargement
createParticles();
</script>
""", unsafe_allow_html=True)

# Base de données de projets enrichie
PROJETS = [
    {
        "titre": "Détection de Sentiment Multilingue",
        "description": "Modèle NLP avancé détectant les nuances émotionnelles dans 15 langues",
        "technologies": ["Transformers", "PyTorch", "Multilingual BERT"],
        "impact": "Précision de 92%",
        "categorie": "NLP",
        "badge": "🌍 Multilingue"
    },
    {
        "titre": "Recommandation IA Personnalisée",
        "description": "Système de recommandation utilisant l'apprentissage par renforcement",
        "technologies": ["TensorFlow", "Keras", "Recommender Systems"],
        "impact": "Augmentation de l'engagement utilisateur de 45%",
        "categorie": "Machine Learning",
        "badge": "🚀 Innovant"
    },
    {
        "titre": "Prédiction de Risques Financiers",
        "description": "Modèle prédictif évaluant les risques d'investissement en temps réel",
        "technologies": ["Scikit-learn", "Pandas", "XGBoost"],
        "impact": "Réduction des pertes de 30%",
        "categorie": "Finance & IA",
        "badge": "💹 Finance"
    }
]

def generate_projects():
    for projet in PROJETS:
        st.markdown(f"""
        <div class="project-card interactive-element" style="
            background: linear-gradient(145deg, rgba(255,255,255,0.7), rgba(255,255,255,0.4));
            backdrop-filter: blur(15px);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
        ">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h3 style="color: var(--primary-color);">{projet['titre']}</h3>
                <span style="background-color: rgba(138,79,255,0.1); padding: 5px 10px; border-radius: 20px;">
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
                    color: var(--primary-color);
                    padding: 5px 10px; 
                    border-radius: 20px;
                ">
                    Impact: {projet['impact']}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-title">Portfolio IA Révolutionnaire</h1>', unsafe_allow_html=True)
    
    # Sections dynamiques
    tab1, tab2, tab3 = st.tabs(["🚀 Projets", "💡 Compétences", "📊 Parcours"])
    
    with tab1:
        st.markdown("## Mes Projets Innovants")
        generate_projects()
    
    with tab2:
        st.markdown("## Compétences Techniques")
        skills = {
            "Machine Learning": 90,
            "Deep Learning": 85,
            "NLP": 80,
            "Computer Vision": 75,
            "Python": 95,
            "TensorFlow": 88
        }
        
        for skill, level in skills.items():
            st.progress(level)
            st.markdown(f"**{skill}** - {level}%")
    
    with tab3:
        st.markdown("## Mon Parcours Professionnel")
        timeline = [
            {"annee": "2020", "poste": "Data Scientist Junior", "entreprise": "TechInnovate"},
            {"annee": "2022", "poste": "Data Scientist Confirmé", "entreprise": "AIHub"},
            {"annee": "2024", "poste": "Lead Data Scientist", "entreprise": "GlobalAI"}
        ]
        
        for exp in timeline:
            st.markdown(f"""
            <div class="interactive-element" style="
                background: rgba(255,255,255,0.5);
                border-left: 4px solid var(--primary-color);
                padding: 10px 20px;
                margin-bottom: 10px;
            ">
                <h4>{exp['annee']} - {exp['poste']}</h4>
                <p>{exp['entreprise']}</p>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()