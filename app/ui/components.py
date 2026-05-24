import streamlit as st

def glass_card(title, content, icon="✨"):
    html_content = f"""
    <div class="glass-panel animated">
        <div style="display:flex; align-items:center; gap:14px; margin-bottom:18px;">
            <span style="font-size:1.28rem;">{icon}</span>
            <h3 style="margin:0; color:#ffffff; font-family:'Space Grotesk', sans-serif; font-size:1.35rem;">{title}</h3>
        </div>
        <p style="color:#c8d3ff; line-height:1.75; margin:0;">{content}</p>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

def metric_card(label, value, delta=None):
    with st.container():
        st.markdown('<div class="glass-panel animated" style="padding:20px; text-align:left;">', unsafe_allow_html=True)
        st.markdown(f"<p style='margin:0; color:#8aa0ff; font-size:0.9rem; letter-spacing:0.08em; text-transform:uppercase;'>{label}</p>")
        st.markdown(f"<p style='margin:10px 0 0; font-family: Space Grotesk, sans-serif; font-size:2.4rem; color:#ffffff; font-weight:800;'>{value}</p>")
        if delta:
            st.markdown(f"<p style='margin:8px 0 0; color:#9db1ff; font-size:0.98rem;'>{delta}</p>")
        st.markdown('</div>', unsafe_allow_html=True)

def section_header(title, subtitle=None):
    st.markdown(f"<h2 class='section-title animated'>{title}</h2>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p class='section-subtitle animated'>{subtitle}</p>", unsafe_allow_html=True)

def user_profile_header(username, fitness_level):
    html = f"""
    <div class="glass-panel animated" style="display:flex; flex-direction:column; gap:18px; padding:28px;">
        <div style="display:flex; align-items:center; gap:16px;">
            <div style="width:72px; height:72px; border-radius:20px; display:grid; place-items:center; background:linear-gradient(135deg, rgba(61,245,255,0.8), rgba(187,107,255,0.7)); color:#05070f; font-size:2rem; font-weight:800;">{username[0].upper()}</div>
            <div>
                <p style="margin:0; color:#8aa0ff; text-transform:uppercase; letter-spacing:0.12em; font-size:0.8rem;">Athlete Profile</p>
                <h2 style="margin:6px 0 0; color:#ffffff; font-family:'Space Grotesk', sans-serif; font-size:2rem;">{username}</h2>
                <p style="margin:8px 0 0; color:#c8d3ff;">{fitness_level} Level · AI coaching ready</p>
            </div>
        </div>
        <div style="display:flex; align-items:center; justify-content:space-between; gap:16px; padding:16px 18px; border-radius:22px; background:rgba(255,255,255,0.04); border:1px solid rgba(61,245,255,0.12);">
            <div>
                <p style="margin:0; color:#9db1ff; font-size:0.82rem; letter-spacing:0.08em; text-transform:uppercase;">Progress</p>
                <p style="margin:6px 0 0; color:#ffffff; font-size:1.2rem; font-weight:700;">72% weekly goal</p>
            </div>
            <div style="display:grid; place-items:center; width:54px; height:54px; border-radius:50%; background:linear-gradient(135deg, rgba(61,245,255,0.18), rgba(187,107,255,0.18)); border:1px solid rgba(61,245,255,0.3);">
                <span style="color:#3df5ff; font-weight:700;">72%</span>
            </div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
