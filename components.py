import streamlit as st

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

def create_step(title, metrics, color, emoji):
    st.markdown(f"""
    <div style="
        background: linear-gradient(145deg, {color}15, {color}05);
        border-left: 4px solid {color};
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
        position: relative;
        transition: transform 0.3s ease-in-out;
    ">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 24px; margin-right: 10px;">{emoji}</span>
            <h3 style="color: {color}; margin: 0; font-weight: bold;">{title}</h3>
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px;">
    """, unsafe_allow_html=True)

    cols = st.columns(len(metrics))
    for col, (metric, value) in zip(cols, metrics.items()):
        col.markdown(f"""
        <div style="
            background: {color}15;
            padding: 8px 12px;
            border-radius: 20px;
            font-size: 0.9em;
            color: {color};
            text-align: center;
        ">
            {metric} = {value}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)