import streamlit as st
import os
from dotenv import load_dotenv

# Page config must be the first Streamlit command
st.set_page_config(
    page_title="Real-Time AI Gym Trainer",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load environment variables
load_dotenv()

# Import local modules
from app.database.db_manager import DatabaseManager
from app.auth.auth_manager import AuthManager
from app.ui.style import apply_custom_css
from app.pages.landing import render_landing_page
from app.pages.auth_page import render_auth_page
from app.pages.dashboard import render_dashboard
from app.pages.trainer import render_trainer
from app.pages.settings import render_settings

# Apply Custom Global CSS
apply_custom_css()

def init_session_state():
    defaults = {
        "logged_in": False,
        "user_id": None,
        "username": None,
        "email": None,
        "current_workout_id": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()

# Initialize Database and Auth
@st.cache_resource
def get_db_manager():
    return DatabaseManager()

db_manager = get_db_manager()
auth_manager = AuthManager(db_manager)

# Routing Logic
def main():
    if not auth_manager.is_authenticated():
        st.sidebar.title("AI Gym Trainer")
        st.sidebar.caption("Login or register to access your personalized workouts.")
        menu = ["Home", "Login / Register"]
        choice = st.sidebar.selectbox("Navigation", menu)
        
        if choice == "Home":
            render_landing_page()
        elif choice == "Login / Register":
            render_auth_page(auth_manager)
            
    else:
        st.sidebar.title(f"Hello, {st.session_state['username']}")
        st.sidebar.caption("Your fitness dashboard is ready.")
        
        menu = ["Dashboard", "AI Trainer", "Settings", "Logout"]
        choice = st.sidebar.radio("Navigation", menu)
        
        if choice == "Dashboard":
            render_dashboard(db_manager)
            
        elif choice == "AI Trainer":
            render_trainer(db_manager)
            
        elif choice == "Settings":
            render_settings(db_manager)
            
        elif choice == "Logout":
            auth_manager.logout_user()
            st.rerun()

if __name__ == "__main__":
    main()
