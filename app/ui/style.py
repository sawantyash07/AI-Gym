import streamlit as st

def apply_custom_css():
    css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700;800&family=Sora:wght@400;500;600;700;800&display=swap');

        :root {
            color-scheme: dark;
            font-family: 'Inter', sans-serif;
            --bg-primary: #05070f;
            --bg-secondary: rgba(10, 14, 25, 0.92);
            --surface: rgba(255,255,255,0.06);
            --surface-strong: rgba(255,255,255,0.10);
            --border: rgba(255,255,255,0.14);
            --text-primary: #ffffff;
            --text-secondary: #c8d3ff;
            --text-muted: #8b94b1;
            --accent-blue: #3df5ff;
            --accent-purple: #bb6bff;
            --accent-pink: #ff4fd8;
            --accent-alert: #ff4d6d;
            --shadow: 0 28px 120px rgba(0,0,0,0.35);
        }

        html, body, [class*="css"], .stApp {
            background: radial-gradient(circle at top left, rgba(40,109,255,0.16), transparent 25%),
                        radial-gradient(circle at bottom right, rgba(187,107,255,0.14), transparent 24%),
                        linear-gradient(180deg, #04060d 0%, #071025 52%, #0b1221 100%);
            color: var(--text-primary);
            min-height: 100vh;
        }

        body {
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }

        #MainMenu, footer, header, .css-1lsmgbg, .css-hi6a2p {
            visibility: hidden !important;
            height: 0 !important;
        }

        .block-container {
            padding: 20px 24px 24px 24px !important;
            max-width: 1480px;
        }

        .stButton>button {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, rgba(61,245,255,0.95), rgba(187,107,255,0.95));
            border: 1px solid rgba(255,255,255,0.16);
            box-shadow: 0 18px 40px rgba(61,245,255,0.14);
            color: #ffffff;
            border-radius: 18px;
            padding: 14px 28px;
            transition: transform 0.24s ease, box-shadow 0.24s ease, filter 0.24s ease;
            width: 100%;
            letter-spacing: 0.02em;
        }

        .stButton>button:hover {
            transform: translateY(-2px) scale(1.01);
            box-shadow: 0 26px 54px rgba(61,245,255,0.22);
            filter: brightness(1.05);
        }

        .secondary-btn {
            background: rgba(255,255,255,0.05);
            color: #c8d3ff;
            border: 1px solid rgba(255,255,255,0.12);
            box-shadow: inset 0 0 0 1px rgba(255,255,255,0.03);
        }

        .glass-panel,
        .glass-panel-strong,
        .glass-card,
        .auth-shell,
        .dashboard-shell,
        .trainer-shell,
        .settings-shell {
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 28px;
            box-shadow: var(--shadow);
            transition: transform 0.3s ease, border-color 0.3s ease, background 0.3s ease;
        }

        .glass-panel:hover,
        .glass-panel-strong:hover,
        .glass-card:hover,
        .auth-shell:hover,
        .dashboard-shell:hover,
        .trainer-shell:hover,
        .settings-shell:hover {
            transform: translateY(-6px);
            border-color: rgba(255,255,255,0.22);
        }

        .glass-panel-strong {
            background: rgba(9,13,27,0.96);
            border: 1px solid rgba(255,255,255,0.18);
        }

        .hero-shell {
            padding: 38px 36px;
            border-radius: 32px;
            background: linear-gradient(135deg, rgba(8,18,40,0.95), rgba(23,31,60,0.88));
            border: 1px solid rgba(255,255,255,0.08);
            box-shadow: 0 28px 90px rgba(0,0,0,0.38);
            position: relative;
            overflow: hidden;
        }

        .hero-shell::before {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at top left, rgba(61,245,255,0.16), transparent 24%),
                        radial-gradient(circle at bottom right, rgba(187,107,255,0.18), transparent 22%);
            pointer-events: none;
        }

        .hero-shell h1 {
            font-family: 'Space Grotesk', sans-serif;
            font-size: clamp(3rem, 4vw, 5rem);
            color: #ffffff;
            line-height: 1.02;
            margin-bottom: 12px;
        }

        .hero-copy {
            font-family: 'Poppins', sans-serif;
            font-size: 1.12rem;
            color: #d7e0ff;
            max-width: 860px;
            line-height: 1.8;
        }

        .section-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 2.4rem;
            color: #ffffff;
            margin-bottom: 10px;
            letter-spacing: -0.04em;
            text-shadow: 0 0 20px rgba(59,245,255,0.2);
        }

        .section-subtitle {
            color: #94a2d8;
            font-size: 1rem;
            margin-bottom: 24px;
            max-width: 860px;
            line-height: 1.7;
        }

        .sidebar-glass {
            padding: 24px 20px 18px;
            background: rgba(9,13,27,0.92);
            border-radius: 28px;
            border: 1px solid rgba(255,255,255,0.12);
            margin: 12px 8px 24px 8px;
            box-shadow: 0 32px 80px rgba(0,0,0,0.44);
        }

        .sidebar-profile {
            display: grid;
            gap: 14px;
            margin-bottom: 18px;
        }

        .profile-badge {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .profile-avatar {
            width: 54px;
            height: 54px;
            border-radius: 18px;
            display: grid;
            place-items: center;
            background: linear-gradient(135deg, rgba(61,245,255,0.45), rgba(187,107,255,0.3));
            color: #05070f;
            font-weight: 800;
            font-size: 1.35rem;
            border: 1px solid rgba(255,255,255,0.15);
        }

        .profile-status {
            color: #c8d3ff;
            font-size: 0.96rem;
            line-height: 1.6;
        }

        .status-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 12px;
            border-radius: 999px;
            background: rgba(61,245,255,0.12);
            border: 1px solid rgba(61,245,255,0.18);
            color: #3df5ff;
            font-size: 0.86rem;
            font-weight: 600;
        }

        .status-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #3df5ff;
            box-shadow: 0 0 18px rgba(61,245,255,0.35);
        }

        .sidebar-progress {
            position: relative;
            height: 94px;
            border-radius: 24px;
            background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
            padding: 18px;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.12);
        }

        .sidebar-progress:before {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at top right, rgba(187,107,255,0.22), transparent 25%);
            pointer-events: none;
        }

        .progress-label {
            color: #8aa0ff;
            font-size: 0.82rem;
            margin-bottom: 8px;
            letter-spacing: 0.04em;
        }

        .progress-bar {
            height: 10px;
            width: 100%;
            background: rgba(255,255,255,0.06);
            border-radius: 999px;
            overflow: hidden;
        }

        .progress-filled {
            height: 100%;
            width: 72%;
            background: linear-gradient(90deg, rgba(61,245,255,0.95), rgba(187,107,255,0.95));
            box-shadow: 0 0 16px rgba(61,245,255,0.36);
            border-radius: 999px;
            transition: width 0.6s ease;
        }

        .nav-link {
            display: flex;
            align-items: center;
            padding: 14px 16px;
            border-radius: 18px;
            margin-bottom: 10px;
            color: #c8d3ff;
            text-decoration: none;
            background: rgba(255,255,255,0.02);
            border: 1px solid transparent;
            transition: transform 0.24s ease, border-color 0.24s ease, box-shadow 0.24s ease;
        }

        .nav-link:hover {
            transform: translateX(6px);
            border-color: rgba(61,245,255,0.22);
            box-shadow: 0 16px 40px rgba(61,245,255,0.08);
            background: rgba(61,245,255,0.07);
        }

        .nav-link.active {
            border-color: rgba(187,107,255,0.42);
            background: rgba(187,107,255,0.12);
            box-shadow: 0 18px 50px rgba(187,107,255,0.16);
        }

        .nav-link span {
            display: inline-flex;
            align-items: center;
            gap: 12px;
            font-size: 0.96rem;
            font-weight: 600;
        }

        .nav-icon {
            width: 34px;
            height: 34px;
            border-radius: 12px;
            display: grid;
            place-items: center;
            background: rgba(255,255,255,0.08);
            color: #3df5ff;
        }

        .nav-link.active .nav-icon,
        .nav-link:hover .nav-icon {
            background: linear-gradient(135deg, rgba(61,245,255,0.95), rgba(187,107,255,0.95));
            color: #05070f;
        }

        input, textarea, select, .stTextInput>div>div>input, .stNumberInput>div>div>input {
            background: rgba(255,255,255,0.05) !important;
            border: 1px solid rgba(255,255,255,0.12) !important;
            color: #ffffff !important;
            border-radius: 16px !important;
            padding: 14px !important;
            transition: border-color 0.24s ease, box-shadow 0.24s ease !important;
            font-family: 'Inter', sans-serif !important;
        }

        input:focus, textarea:focus, select:focus {
            outline: none !important;
            border-color: rgba(61,245,255,0.65) !important;
            box-shadow: 0 0 0 6px rgba(61,245,255,0.08) !important;
        }

        .stTextInput>div>label, .stNumberInput>div>label, .stSelectbox>div>label, .stCheckbox>div>label {
            color: #d2d8ff;
            font-weight: 600;
            font-size: 0.95rem;
        }

        .stTextInput>div>div>input::placeholder,
        .stNumberInput>div>div>input::placeholder {
            color: rgba(255,255,255,0.45) !important;
        }

        .st-expander {
            background: rgba(255,255,255,0.05) !important;
            border: 1px solid rgba(255,255,255,0.12) !important;
            border-radius: 22px !important;
        }

        .st-expander .streamlit-expanderHeader {
            font-weight: 700 !important;
            color: #ffffff !important;
        }

        .metrics-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 18px;
            margin-top: 14px;
        }

        .hud-panel {
            padding: 22px;
            border-radius: 28px;
            background: rgba(8,15,35,0.82);
            border: 1px solid rgba(255,255,255,0.12);
            box-shadow: 0 18px 40px rgba(0,0,0,0.35);
            overflow: hidden;
        }

        .hud-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            margin-bottom: 18px;
        }

        .hud-item:last-child {
            margin-bottom: 0;
        }

        .hud-label {
            color: #9db1ff;
            font-size: 0.92rem;
            text-transform: uppercase;
            letter-spacing: 0.12em;
        }

        .hud-value {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.9rem;
            font-weight: 800;
            color: #ffffff;
        }

        .floating-badge {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 10px 16px;
            border-radius: 999px;
            background: rgba(61,245,255,0.1);
            border: 1px solid rgba(61,245,255,0.16);
            color: #c8d3ff;
            box-shadow: inset 0 0 0 1px rgba(255,255,255,0.03);
            backdrop-filter: blur(16px);
        }

        .pulse-dot {
            width: 10px;
            height: 10px;
            border-radius: 999px;
            background: #3df5ff;
            box-shadow: 0 0 18px rgba(61,245,255,0.4);
        }

        .camera-shell {
            position: relative;
            border-radius: 28px;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.12);
            background: rgba(6,10,20,0.82);
            box-shadow: 0 24px 72px rgba(0,0,0,0.42);
        }

        .camera-shell::before {
            content: '';
            position: absolute;
            inset: 0;
            pointer-events: none;
            background: radial-gradient(circle at center, rgba(61,245,255,0.06), transparent 30%);
        }

        .camera-frame {
            position: absolute;
            inset: 12px;
            border: 2px solid rgba(61,245,255,0.18);
            border-radius: 26px;
            box-shadow: 0 0 40px rgba(61,245,255,0.12);
            pointer-events: none;
        }

        .camera-hud {
            position: absolute;
            top: 18px;
            left: 18px;
            right: 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
            z-index: 10;
        }

        .hud-pill {
            padding: 10px 14px;
            border-radius: 999px;
            background: rgba(1,14,25,0.82);
            border: 1px solid rgba(255,255,255,0.08);
            color: #b0c6ff;
            font-size: 0.88rem;
            font-weight: 600;
            backdrop-filter: blur(16px);
        }

        .status-active {
            color: #3df5ff;
        }

        .glow-ring {
            display: inline-flex;
            width: 72px;
            height: 72px;
            border-radius: 50%;
            border: 2px solid rgba(61,245,255,0.18);
            position: relative;
            align-items: center;
            justify-content: center;
            box-shadow: 0 0 36px rgba(61,245,255,0.18);
        }

        .glow-ring::after {
            content: '';
            position: absolute;
            inset: 8px;
            border-radius: 50%;
            border: 2px dashed rgba(61,245,255,0.35);
            animation: pulseRing 2.2s infinite ease-in-out;
        }

        @keyframes pulseRing {
            0%, 100% { transform: scale(1); opacity: 0.9; }
            50% { transform: scale(1.08); opacity: 0.5; }
        }

        .progress-track {
            width: 100%;
            height: 14px;
            border-radius: 999px;
            background: rgba(255,255,255,0.05);
            overflow: hidden;
            margin-top: 12px;
            box-shadow: inset 0 0 20px rgba(0,0,0,0.12);
        }

        .progress-fill {
            height: 100%;
            width: 58%;
            background: linear-gradient(90deg, rgba(61,245,255,0.95), rgba(187,107,255,0.95));
            box-shadow: 0 0 18px rgba(61,245,255,0.36);
            transition: width 0.5s ease;
        }

        .button-row {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .button-row .stButton {
            flex: 1;
            min-width: 140px;
        }

        .section-divider {
            height: 1px;
            background: linear-gradient(90deg, rgba(61,245,255,0.14), transparent 50%, rgba(187,107,255,0.14));
            margin: 28px 0;
        }

        .section-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 20px;
        }

        .animated-card {
            transition: transform 0.28s ease, filter 0.28s ease;
        }

        .animated-card:hover {
            transform: translateY(-8px);
            filter: saturate(1.05);
        }

        .futuristic-label {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 10px 16px;
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(61,245,255,0.12);
            border-radius: 999px;
            color: #9db1ff;
            font-size: 0.86rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .button-glow {
            position: relative;
            overflow: hidden;
        }

        .button-glow::after {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(120deg, rgba(61,245,255,0.15), rgba(187,107,255,0.15), rgba(255,79,216,0.12));
            opacity: 0;
            transition: opacity 0.35s ease;
        }

        .button-glow:hover::after {
            opacity: 1;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
