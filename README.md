# AI Gym Trainer

A futuristic, premium fitness platform built with Streamlit, MediaPipe, SQLite, and AI-driven coaching. This app delivers live webcam-based exercise tracking, form detection, rep counting, voice feedback, workout analytics, and a polished dark glassmorphism UI.

---

## Project Overview

AI Gym Trainer is a full-stack Streamlit application designed for real-time workout monitoring and training. Users can register, log in, select exercises, stream webcam video to the app, and receive live movement analysis and AI coaching. Workout sessions are saved in SQLite and visualized through a modern dashboard.


## Key Features

- **Secure Authentication**
  - User registration and login flows
  - Password hashing with `bcrypt`
  - Session management via `st.session_state`

- **Premium UI/UX**
  - Futuristic dark glassmorphism design
  - Animated cards, neon accent styling, and modern typography
  - Responsive page layout for landing, dashboard, trainer, and settings

- **Live AI Trainer**
  - Webcam-based posture detection using MediaPipe
  - Exercise recognition for Squats, Pushups, Bicep Curls, Lunges, Plank, and Jumping Jacks
  - Real-time rep counting and form accuracy scoring
  - Instant coaching advice with voice guidance

- **AI Voice Coaching**
  - Groq API integration for prompt-based advice
  - Audio playback through `gTTS`
  - Motivational and corrective feedback on performance

- **Workout Analytics**
  - Historical workout data stored in SQLite
  - Interactive dashboard charts powered by Plotly
  - Daily calorie tracking, workout summaries, and session detail views

- **Deployment Ready**
  - Render configuration included via `render.yaml`
  - Supports remote webcam access using `streamlit-webrtc`

---

## Architecture

The app is organized into modular components:

- `streamlit_app.py` — main entrypoint, page routing, auth gating, and app configuration
- `app/auth/auth_manager.py` — authentication and session workflows
- `app/database/db_manager.py` — SQLite database schema and queries
- `app/pages/landing.py` — public marketing and feature showcase
- `app/pages/dashboard.py` — analytics and workout history
- `app/pages/trainer.py` — live trainer experience and webcam streaming
- `app/pages/settings.py` — user profile and preference settings
- `app/detectors/pose_detector.py` — MediaPipe pose extraction and pose utility functions
- `app/detectors/exercise_tracker.py` — exercise-specific tracking, rep counters, and accuracy analysis
- `app/ai/voice_coach.py` — Groq prompt generation and TTS playback
- `app/ui/style.py` — global theme and custom CSS for glassmorphism
- `app/ui/components.py` — reusable UI cards, headers, and styled elements

---

## Project Structure

```text
.
├── README.md
├── render.yaml
├── requirements.txt
├── streamlit_app.py
├── .env.example
├── app
│   ├── ai
│   │   └── voice_coach.py
│   ├── auth
│   │   └── auth_manager.py
│   ├── database
│   │   └── db_manager.py
│   ├── detectors
│   │   ├── exercise_tracker.py
│   │   └── pose_detector.py
│   ├── pages
│   │   ├── auth_page.py
│   │   ├── dashboard.py
│   │   ├── landing.py
│   │   ├── settings.py
│   │   └── trainer.py
│   └── ui
│       ├── components.py
│       └── style.py
```

---

## Requirements

Python dependencies are listed in `requirements.txt`.

- streamlit
- streamlit-webrtc
- opencv-python-headless
- mediapipe
- numpy
- bcrypt
- groq
- httpx
- gTTS
- SpeechRecognition
- plotly
- python-dotenv
- pandas
- SQLAlchemy

---

## Setup

### 1. Clone repository

```bash
git clone https://github.com/yourusername/ai_gym_trainer.git
cd ai_gym_trainer
```

### 2. Create and activate a virtual environment

On macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

On Windows:
```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy or create a `.env` file from `.env.example` and add your API keys:

```bash
copy .env.example .env
```

Required variables:

- `GROQ_API_KEY`

Optional variables can be added to support future deploys and features.

---

## Running Locally

Launch the app with Streamlit:

```bash
streamlit run streamlit_app.py
```

Open `http://localhost:8501` in your browser.

> Note: The live trainer uses webcam access. Allow camera permissions, and use a well-lit environment with your full body visible.

---

## Deployment

This app includes a Render configuration in `render.yaml`.

### Render deployment steps

1. Connect the repository to Render.
2. Create a new Web Service.
3. Render detects `render.yaml` and uses the existing build/start commands.
4. Add the `GROQ_API_KEY` environment variable in Render.
5. Deploy the service.

The deploy uses:

```yaml
buildCommand: pip install -r requirements.txt
startCommand: streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0
```

---

## Usage

- **Home / Landing** — overview of the product and exercise highlights.
- **Login / Register** — secure account creation and authentication.
- **Dashboard** — workout analytics, daily calorie burn, and trends.
- **AI Trainer** — live webcam tracking, rep counting, and coaching feedback.
- **Settings** — profile details and user preferences.

---

## Notes

- `streamlit-webrtc` requires HTTPS for remote deployment and proper browser permission handling.
- The app stores data locally in SQLite and is suitable for prototyping and lightweight deployments.
- For best experience, use a device with a webcam and good lighting.

---

## Future Improvements

- Expand exercise library with advanced movements like deadlifts, pull-ups, and kettlebell routines.
- Add adaptive difficulty, personalized session plans, and workout challenges.
- Integrate audio personalization, music playback, and voice tone selection.
- Add leaderboard, social sharing, and community workout support.

---

## License

This project is ready to adapt to your chosen open-source license or internal distribution policy.
