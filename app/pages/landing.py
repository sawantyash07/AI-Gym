import streamlit as st
from app.ui.components import section_header

EXERCISES = [
    {"name": "Squat", "icon": "🏋️", "description": "Track lower-body form, depth, and rep cadence for stronger legs."},
    {"name": "Pushup", "icon": "🤸", "description": "Monitor upper-body control and count perfect reps with posture feedback."},
    {"name": "Bicep Curl", "icon": "💪", "description": "Measure arm motion, curl range, and exercise consistency."},
    {"name": "Lunge", "icon": "🏃", "description": "Analyze balance and stability while lowering into each rep."},
    {"name": "Plank", "icon": "🧘", "description": "Detect core alignment and hold duration for safer form."},
    {"name": "Jumping Jack", "icon": "🤸‍♂️", "description": "Measure full-body rhythm, range of motion, and conditioning."},
]

FEATURES = [
    {"title": "Live Exercise Feedback", "detail": "Get immediate coaching cues for reps, posture, and movement efficiency while you work out."},
    {"title": "Workout History", "detail": "Track sessions, calories burned, and form quality over time with a polished dashboard."},
    {"title": "AI Voice Motivation", "detail": "Hear energizing voice guidance that keeps you engaged and breathing correctly."},
]

def render_landing_page():
    st.markdown("<div class='hero-shell'>", unsafe_allow_html=True)
    st.markdown("<h1>AI Gym Trainer for the next generation of performance.</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='hero-copy'>Unlock a premium fitness experience with live posture tracking, adaptive voice coaching, and cinematic progress analytics.</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div class='button-row' style='margin-top:28px;'>"
        "<button class='stButton button-glow' style='width:auto;'>Explore the Dashboard</button>"
        "<button class='stButton secondary-btn button-glow' style='width:auto;'>Start Your Workout</button>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    section_header("Your smart workout partner", "Sign in to start tracking form, reps, and progress in a single modern app.")

    tabs = st.tabs(["Experience", "Exercises", "Why It Works"])

    with tabs[0]:
        st.markdown("<div class='glass-panel interactive-card'>", unsafe_allow_html=True)
        st.markdown("<h3>Train with confidence</h3>", unsafe_allow_html=True)
        st.markdown(
            "<p class='interactive-copy'>Open the AI Trainer to start a workout, let the app count your reps, and get coaching cues in real time.</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div class='feature-pill-row'>"
            "<span class='feature-pill'>Instant form correction</span>"
            "<span class='feature-pill'>Progress dashboard</span>"
            "<span class='feature-pill'>Voice guidance</span>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[1]:
        st.markdown("<div class='exercise-grid'>", unsafe_allow_html=True)
        for exercise in EXERCISES:
            st.markdown(
                f"<div class='exercise-card animated'><div class='exercise-icon'>{exercise['icon']}</div><h4>{exercise['name']}</h4><p>{exercise['description']}</p></div>",
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[2]:
        for feature in FEATURES:
            with st.expander(feature["title"], expanded=False):
                st.write(feature["detail"])

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='glass-panel'>"
        "<h3>Ready to build better workouts?</h3>"
        "<p>Use the sidebar to login or register, then open the AI Trainer to start shaping your form, tracking progress, and improving every set.</p>"
        "</div>",
        unsafe_allow_html=True,
    )
