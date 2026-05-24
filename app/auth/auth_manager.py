import bcrypt
import streamlit as st
import re

class AuthManager:
    def __init__(self, db_manager):
        self.db = db_manager

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def verify_password(self, password, hashed):
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

    def is_valid_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def is_strong_password(self, password):
        # Minimum 8 characters, at least one letter and one number
        if len(password) < 8:
            return False, "Password must be at least 8 characters long."
        if not re.search(r"[A-Za-z]", password):
            return False, "Password must contain at least one letter."
        if not re.search(r"\d", password):
            return False, "Password must contain at least one number."
        return True, ""

    def register_user(self, username, email, password, confirm_password):
        if not username or not email or not password:
            return False, "All fields are required."
        
        if password != confirm_password:
            return False, "Passwords do not match."
            
        if not self.is_valid_email(email):
            return False, "Invalid email format."
            
        is_strong, msg = self.is_strong_password(password)
        if not is_strong:
            return False, msg

        hashed_pw = self.hash_password(password)
        success, msg = self.db.create_user(username, email, hashed_pw)
        return success, msg

    def login_user(self, username, password):
        if not username or not password:
            return False, "Username and password are required."
            
        user = self.db.get_user_by_username(username)
        if user and self.verify_password(password, user['password_hash']):
            # Set session state
            st.session_state['logged_in'] = True
            st.session_state['user_id'] = user['id']
            st.session_state['username'] = user['username']
            st.session_state['email'] = user['email']
            return True, "Login successful."
            
        return False, "Invalid username or password."

    def logout_user(self):
        for key in ['logged_in', 'user_id', 'username', 'email', 'current_workout_id']:
            if key in st.session_state:
                del st.session_state[key]
        
    def is_authenticated(self):
        return st.session_state.get('logged_in', False)
        
    def get_current_user(self):
        if self.is_authenticated():
            return {
                'id': st.session_state.get('user_id'),
                'username': st.session_state.get('username'),
                'email': st.session_state.get('email')
            }
        return None
