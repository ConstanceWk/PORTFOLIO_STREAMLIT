import streamlit as st
from components import *

def show_home():
    st.markdown('<h1 class="main-title">Portfolio de Constance Walusiak</h1>', unsafe_allow_html=True)
    
    display_profile_image()
    
    st.markdown("""
    <div class="intro-card">
        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
            <span style="font-size: 2em;">👋</span>
            <h2 style="margin: 0; background: linear-gradient(90deg, #8A4FFF, #E0AEFF); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.8em;">
                Bonjour! Je suis une étudiante en Data et Intelligence Artificielle
            </h2>
        </div>
        <p style="font-size: 1.2em; line-height: 1.6; color: #4a4a4a; margin-bottom: 0; padding-left: 20px; border-left: 4px solid #8A4FFF;">
            👩‍💻 Mon portfolio présente mon parcours professionnel, mais également mes projets en Machine Learning et Intelligence Artificielle. 
            Spécialisée dans l'analyse de données complexes, je développe des solutions innovantes en NLP, Computer Vision et Deep Learning. 
            Découvrez mes réalisations et compétences techniques, illustrant ma passion pour l'intelligence artificielle et sa capacité à résoudre des défis concrets.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="intro-card fun-card" style="background: linear-gradient(145deg, rgba(255,255,255,0.7), rgba(255,255,255,0.4)); border: 2px dashed #8A4FFF; margin-top: 30px;">
        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
            <span style="font-size: 2em;">🚀</span>
            <h3 style="margin: 0; background: linear-gradient(90deg, #8A4FFF, #E0AEFF); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.5em;">
                Pourquoi l'IA et moi, on forme une équipe de choc?
            </h3>
        </div>
        <p style="font-size: 1.1em; line-height: 1.6; color: #4a4a4a; font-style: italic;">
            Imaginez une Data Scientist qui transforme les algorithmes en véritables super-héros du quotidien ! 🦸‍♀️
            <br><br>
            Mon secret ? Je ne me contente pas de coder, je donne vie aux données ! Que ce soit pour prédire le prochain best-seller ou pour comprendre pourquoi votre chat préfère le coussin à son panier, mes modèles sont là pour résoudre vos mystères.
            <br><br>
            <span style="color: #8A4FFF; font-weight: bold;">Ma mission :</span> Rendre l'IA aussi accessible qu'une conversation avec votre meilleur ami, mais en plus intelligent (ne le dites à personne ! 🤫)
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Caractéristiques en grille
    st.markdown("""
    <div class="intro-card fun-card" style="background: linear-gradient(145deg, rgba(255,255,255,0.7), rgba(255,255,255,0.4)); padding: 20px; text-align: center; margin-top: 30px;">
        <div style="font-size: 3em; margin-bottom: 15px;">
            🤖 + 👩 = 💡
        </div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin: 20px 0;">
            <div style="background: rgba(138,79,255,0.1); padding: 15px; border-radius: 10px; text-align: center;">
                <span style="font-size: 2em;">🎯</span>
                <p style="margin: 5px 0; font-weight: bold;">Précision</p>
                <p style="font-size: 0.9em;">99.9% du temps... sauf quand je regarde Netflix 😅</p>
            </div>
            <div style="background: rgba(138,79,255,0.1); padding: 15px; border-radius: 10px; text-align: center;">
                <span style="font-size: 2em;">⚡</span>
                <p style="margin: 5px 0; font-weight: bold;">Rapidité</p>
                <p style="font-size: 0.9em;">Plus rapide que mon café du matin ☕</p>
            </div>
            <div style="background: rgba(138,79,255,0.1); padding: 15px; border-radius: 10px; text-align: center;">
                <span style="font-size: 2em;">🎨</span>
                <p style="margin: 5px 0; font-weight: bold;">Créativité</p>
                <p style="font-size: 0.9em;">Mon IA a plus d'idées que moi un lundi matin 🌈</p>
            </div>
        </div>
        <div style="font-size: 1.2em; color: #8A4FFF; font-weight: bold; margin-top: 20px;">
            Mon super pouvoir ? Transformer le café en code ! ☕→ 💻
        </div>
    </div>
    """, unsafe_allow_html=True)