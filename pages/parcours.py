import streamlit as st
from components import create_step

def show_parcours():
    st.markdown("""
    <div class="intro-card">
        <h2 style="text-align: center; color: #8A4FFF; margin-bottom: 30px; font-weight: bold;">
            Algorithme d'Apprentissage : Mon Parcours 🧠
        </h2>
    </div>
    """, unsafe_allow_html=True)

    steps = [
        {
            "title": "Cycle Préparatoire - EFREI PARIS PANTHEON ASSAS",
            "metrics": {
                "initialization_phase": "'fondamentaux'",
                "learning_rate": "0.01",
                "base_knowledge": "85%"
            },
            "color": "#8A4FFF",
            "emoji": "🎓"
        },
        {
            "title": "Stage M1 - Data Scientist @ Innowide",
            "metrics": {
                "accuracy_score": "95%",
                "real_world_exp": "True",
                "skills_acquired": "['ML', 'Data']"
            },
            "color": "#FF69B4",
            "emoji": "💼"
        },
        {
            "title": "Data Scientist & ML Engineer",
            "metrics": {
                "expertise_level": "'advanced'",
                "model_status": "'production_ready'",
                "performance": "98%"
            },
            "color": "#4B0082",
            "emoji": "🚀"
        }
    ]

    for step in steps:
        create_step(
            step["title"],
            step["metrics"],
            step["color"],
            step["emoji"]
        )

    # Métriques finales
    st.markdown("""
    <div style="background: rgba(255, 255, 255, 0.7); border-radius: 10px; padding: 20px; margin-top: 30px;">
        <h4 style="text-align: center; color: #8A4FFF; margin-bottom: 20px;">Métriques Finales 📊</h4>
    """, unsafe_allow_html=True)

    cols = st.columns(3)
    metrics = [
        ("Code Quality", "98%", "💻"),
        ("ML Proficiency", "95%", "🤖"),
        ("Data Analysis", "97%", "📈")
    ]
    
    for col, (metric, value, icon) in zip(cols, metrics):
        col.markdown(f"""
        <div style="background: linear-gradient(145deg, #8A4FFF15, #FF69B415); border-radius: 10px; padding: 15px; text-align: center;">
            <div style="font-size: 24px; margin-bottom: 5px;">{icon}</div>
            <div style="color: #8A4FFF; font-weight: bold;">{metric}</div>
            <div style="color: #FF69B4; font-size: 1.2em;">{value}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)