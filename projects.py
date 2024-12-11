import streamlit as st

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

def show_projects():
    st.markdown('<h2 class="section-title">🚀 Mes Projets</h2>', unsafe_allow_html=True)
    
    for projet in PROJETS:
        st.markdown(f"""
        <div class="project-card interactive-element">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h3 style="color: #8A4FFF;">{projet['titre']}</h3>
                <span style="background-color: rgba(138,79,255,0.1); padding: 5px 10px; border-radius: 20px; font-size: 0.9em;">
                    {projet['badge']}
                </span>
            </div>
            <p>{projet['description']}</p>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <b>Technologies:</b> {", ".join(projet['technologies'])}
                </div>
                <div style="background-color: rgba(138,79,255,0.2); color: #8A4FFF; padding: 5px 10px; border-radius: 20px; font-size: 0.9em;">
                    Impact: {projet['impact']}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)