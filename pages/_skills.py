import streamlit as st

def show_skills():
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