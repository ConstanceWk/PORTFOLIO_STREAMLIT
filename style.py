def load_css():
    return """
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
            background: rgba(255, 255, 255, 0.6);
            backdrop-filter: blur(10px);
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

        /* Style pour la sidebar */
        .css-1d391kg {
            background: linear-gradient(to bottom, rgba(138, 79, 255, 0.1), rgba(224, 174, 255, 0.1)) !important;
            backdrop-filter: blur(10px);
        }

        .streamlit-expanderHeader {
            background-color: rgba(138, 79, 255, 0.05) !important;
        }

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

        [data-testid="stSidebar"] {
            background: rgba(138, 79, 255, 0.15) !important;
            backdrop-filter: blur(10px);
        }

        section[data-testid="stSidebar"] > div {
            padding: 2rem 1rem;
        }

        .st-emotion-cache-16idsys p {
            font-size: 1.1em;
            color: #6A5ACD;
        }

        .st-emotion-cache-pk3ts8:hover {
            background: rgba(138, 79, 255, 0.2) !important;
            transform: translateX(5px);
        }

        .stApp header {
            display: none !important;
        }

        .stApp > div:first-child {
            margin-top: 0 !important;
        }
    </style>
    """