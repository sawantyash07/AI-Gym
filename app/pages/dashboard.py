import streamlit as st
import pandas as pd
import plotly.express as px
from app.ui.components import metric_card, section_header, user_profile_header

def render_dashboard(db_manager):
    user = db_manager.get_user_by_username(st.session_state['username'])

    user_profile_header(user['username'], user.get('fitness_level', 'Beginner'))
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    workouts = db_manager.get_user_workouts(user['id'], limit=30)
    total_workouts = len(workouts)
    total_calories = sum([w[3] or 0 for w in workouts])
    average_calories = total_calories / total_workouts if total_workouts else 0
    best_workout = max(workouts, key=lambda w: w[3] or 0) if workouts else None

    with st.container():
        st.markdown("<div class='dashboard-shell'>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            metric_card("Total Workouts", str(total_workouts), "Last 30 days")
        with col2:
            metric_card("Calories Burned", f"{total_calories:.0f} kcal", "Estimated")
        with col3:
            metric_card("Avg per Workout", f"{average_calories:.1f} kcal", "Session")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
    section_header("Activity Overview", "Your training metrics, performance trends, and recent sessions in one premium view.")

    if workouts:
        df = pd.DataFrame(workouts, columns=["ID", "Start Time", "End Time", "Calories", "Type"])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['Date'] = df['Start Time'].dt.date
        daily_cals = df.groupby('Date')['Calories'].sum().reset_index()

        fig = px.bar(
            daily_cals,
            x='Date',
            y='Calories',
            title="Calories Burned per Day",
            template="plotly_dark",
            color_discrete_sequence=['#3df5ff'],
        )
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#ffffff'))
        fig.update_xaxes(showgrid=False, color='#c8d3ff')
        fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.08)', color='#c8d3ff')

        st.markdown("<div class='glass-panel animated'>", unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        section_header("Recent Workouts", "Review your last sessions and refine every set with AI guidance.")

        for w in workouts[:5]:
            with st.expander(f"{w[4]} Workout — {w[1].split(' ')[0]}"):
                st.markdown(f"<div class='glass-panel animated' style='padding:16px;'>", unsafe_allow_html=True)
                st.markdown(f"<p style='margin:0.15rem 0; color:#9db1ff;'><strong>Calories:</strong> {w[3] or 0}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='margin:0.15rem 0; color:#9db1ff;'><strong>Started:</strong> {w[1]}</p>", unsafe_allow_html=True)
                if w[2]:
                    st.markdown(f"<p style='margin:0.15rem 0; color:#9db1ff;'><strong>Completed:</strong> {w[2]}</p>", unsafe_allow_html=True)
                logs = db_manager.get_workout_logs(w[0])
                if logs:
                    log_df = pd.DataFrame(logs, columns=["Exercise", "Reps", "Sets", "Accuracy", "AI Feedback", "Time"])
                    st.dataframe(log_df, use_container_width=True)
                else:
                    st.info("No exercise details recorded for this session.")
                st.markdown("</div>", unsafe_allow_html=True)

        if best_workout:
            st.markdown("<div class='glass-panel animated' style='margin-top:20px;'>", unsafe_allow_html=True)
            st.markdown(f"<p class='futuristic-label'>Peak Session</p>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='margin:0.5rem 0 0; color:#ffffff;'>Best workout: {best_workout[4]} with {best_workout[3] or 0} kcal</h4>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='glass-panel animated' style='padding:24px;'>", unsafe_allow_html=True)
        st.info("No workouts found. Head over to the Trainer to get started!")
        st.markdown("</div>", unsafe_allow_html=True)
