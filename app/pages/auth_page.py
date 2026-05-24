import streamlit as st
from app.ui.components import section_header

def render_auth_page(auth_manager):
    st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("<div class='auth-shell animated' style='padding:32px;'>", unsafe_allow_html=True)
        section_header("Welcome to AI Gym", "Sign in or create an account to launch your premium training experience.")

        tab1, tab2 = st.tabs(["Login", "Register"])

        with tab1:
            st.markdown("<div class='glass-panel animated' style='padding:24px;'>", unsafe_allow_html=True)
            login_username = st.text_input("Username", key="login_username")
            login_password = st.text_input("Password", type="password", key="login_password")

            if st.button("Login", key="login_btn"):
                success, msg = auth_manager.login_user(login_username, login_password)
                if success:
                    st.success(msg)
                    st.rerun()
                else:
                    st.error(msg)
            st.markdown("</div>", unsafe_allow_html=True)

        with tab2:
            st.markdown("<div class='glass-panel animated' style='padding:24px;'>", unsafe_allow_html=True)
            reg_username = st.text_input("Username", key="reg_username")
            reg_email = st.text_input("Email", key="reg_email")
            reg_password = st.text_input("Password", type="password", key="reg_password")
            reg_confirm = st.text_input("Confirm Password", type="password", key="reg_confirm")

            if st.button("Register", key="reg_btn"):
                success, msg = auth_manager.register_user(reg_username, reg_email, reg_password, reg_confirm)
                if success:
                    st.success(msg + " You can now login.")
                else:
                    st.error(msg)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
