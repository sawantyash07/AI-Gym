import streamlit as st
from app.ui.components import section_header

def render_settings(db_manager):
    section_header("Settings", "Manage your profile, preferences, and AI coaching options.")

    user = db_manager.get_user_by_username(st.session_state['username'])

    st.markdown("<div class='glass-panel animated'>", unsafe_allow_html=True)
    st.subheader("Account Details")
    st.markdown(f"<p style='color:#9db1ff; margin:0.2rem 0;'><strong>Username:</strong> {user['username']}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#9db1ff; margin:0.2rem 0;'><strong>Email:</strong> {user.get('email', 'Not available')}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#9db1ff; margin:0.2rem 0;'><strong>Fitness Level:</strong> {user.get('fitness_level', 'Beginner')}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='glass-panel animated'>", unsafe_allow_html=True)
    st.subheader("Profile Information")

    col1, col2 = st.columns(2)
    with col1:
        height = st.number_input(
            "Height (cm)",
            min_value=0.0,
            max_value=300.0,
            value=user.get('height_cm') or 0.0,
        )
        weight = st.number_input(
            "Weight (kg)",
            min_value=0.0,
            max_value=500.0,
            value=user.get('weight_kg') or 0.0,
        )
    with col2:
        fitness_level = st.selectbox(
            "Fitness Level",
            ["Beginner", "Intermediate", "Advanced"],
            index=["Beginner", "Intermediate", "Advanced"].index(user.get('fitness_level', 'Beginner')),
        )

    if st.button("Update Profile"):
        success = db_manager.update_user_profile(user['id'], height, weight, fitness_level)
        if success:
            st.success("Profile updated successfully!")
        else:
            st.error("Failed to update profile.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='glass-panel animated'>", unsafe_allow_html=True)
    st.subheader("Preferences")
    st.markdown("<div class='futuristic-label'>AI Coaching</div>", unsafe_allow_html=True)
    st.info("Future releases will add voice options, difficulty scaling, and workout reminders.")
    st.markdown("</div>", unsafe_allow_html=True)
