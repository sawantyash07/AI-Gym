import streamlit as st
import av
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
from app.detectors.pose_detector import PoseDetector
from app.detectors.exercise_tracker import ExerciseTracker
from app.ai.voice_coach import AIVoiceCoach
from app.ui.components import section_header

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

EXERCISE_OPTIONS = [
    "Squat",
    "Pushup",
    "Bicep Curl",
    "Lunge",
    "Plank",
    "Jumping Jack",
]


def init_trainer_session_state():
    defaults = {
        'detector': PoseDetector(),
        'tracker': ExerciseTracker(),
        'ai_coach': AIVoiceCoach(),
        'current_exercise': 'Squat',
        'last_ai_feedback': 'Ready to train.',
        'workout_started': False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


class VideoTransformer:
    def __init__(self, detector=None, tracker=None):
        self.detector = detector or PoseDetector()
        self.tracker = tracker or ExerciseTracker()
        self.exercise_type = "Squat"

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = self.detector.find_pose(img)
        self.detector.find_position(img)

        if self.exercise_type == "Squat":
            img, reps, feedback, accuracy = self.tracker.analyze_squat(self.detector, img)
        elif self.exercise_type == "Pushup":
            img, reps, feedback, accuracy = self.tracker.analyze_pushup(self.detector, img)
        elif self.exercise_type == "Bicep Curl":
            img, reps, feedback, accuracy = self.tracker.analyze_bicep_curl(self.detector, img)
        elif self.exercise_type == "Lunge":
            img, reps, feedback, accuracy = self.tracker.analyze_lunge(self.detector, img)
        elif self.exercise_type == "Plank":
            img, reps, feedback, accuracy = self.tracker.analyze_plank(self.detector, img)
        elif self.exercise_type == "Jumping Jack":
            img, reps, feedback, accuracy = self.tracker.analyze_jumping_jack(self.detector, img)
        else:
            img, reps, feedback, accuracy = self.tracker.analyze_squat(self.detector, img)

        return av.VideoFrame.from_ndarray(img, format="bgr24")


def render_trainer(db_manager):
    section_header("Live AI Trainer", "Position your camera so your full body is visible.")

    init_trainer_session_state()

    col1, col2 = st.columns([3, 1], gap='large')

    with col1:
        st.markdown("<div class='camera-shell'>", unsafe_allow_html=True)
        ctx = webrtc_streamer(
            key="gym-trainer",
            mode=WebRtcMode.SENDRECV,
            rtc_configuration=RTC_CONFIGURATION,
            video_processor_factory=lambda: VideoTransformer(
                st.session_state['detector'], st.session_state['tracker']
            ),
            media_stream_constraints={"video": True, "audio": False},
            async_processing=True,
        )
        st.markdown("<div class='camera-frame'></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='glass-panel animated' style='margin-top:18px;'>", unsafe_allow_html=True)
        st.markdown("<div class='hud-item'>", unsafe_allow_html=True)
        st.markdown("<div><p class='hud-label'>Exercise</p><p class='hud-value'>" + st.session_state['current_exercise'] + "</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='pulse-dot'></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div class='hud-item'>", unsafe_allow_html=True)
        st.markdown("<div><p class='hud-label'>Reps</p><p class='hud-value'>" + str(st.session_state['tracker'].counter) + "</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='glow-ring'></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        if ctx.video_processor:
            ctx.video_processor.exercise_type = st.session_state['current_exercise']
            st.success("Live trainer is tracking your form.")
        elif ctx.state.playing:
            st.warning("Waiting for camera feed...")
        else:
            st.info("Allow webcam access to start live tracking.")

    with col2:
        st.markdown("<div class='glass-panel animated'>", unsafe_allow_html=True)
        exercise = st.selectbox(
            "Select Exercise",
            EXERCISE_OPTIONS,
            index=EXERCISE_OPTIONS.index(st.session_state['current_exercise']),
        )

        if exercise != st.session_state['current_exercise']:
            st.session_state['current_exercise'] = exercise
            st.session_state['tracker'].reset()

        st.markdown("<div class='button-row' style='margin-bottom:18px;'>", unsafe_allow_html=True)
        if st.button("Start Workout", key="start_workout"):
            workout_id = db_manager.start_workout(st.session_state['user_id'], workout_type=exercise)
            st.session_state['current_workout_id'] = workout_id
            st.session_state['workout_started'] = True
            st.success(f"{exercise} workout started.")
        if st.button("Reset Counter", key="reset_trainer"):
            st.session_state['tracker'].reset()
            st.success("Counter reset.")
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("Get AI Advice", key="ai_advice"):
            reps = st.session_state['tracker'].counter
            acc = st.session_state['tracker'].accuracy
            msg = st.session_state['ai_coach'].generate_feedback(exercise, reps, acc)
            st.session_state['last_ai_feedback'] = msg
            st.info(msg)
            st.session_state['ai_coach'].play_feedback(msg)

        st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
        st.markdown("<h4>Session Summary</h4>", unsafe_allow_html=True)
        st.markdown(f"<p class='hud-label'>Exercise</p><p class='hud-value'>{exercise}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='hud-label'>Reps</p><p class='hud-value'>{st.session_state['tracker'].counter}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='hud-label'>Form Accuracy</p><p class='hud-value'>{st.session_state['tracker'].accuracy:.0f}%</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='hud-label'>Coach Feedback</p><p class='hud-value' style='font-size:1rem; font-weight:500;'>{st.session_state['last_ai_feedback']}</p>", unsafe_allow_html=True)
        status_text = "Active" if st.session_state.get('workout_started') else "Not Started"
        st.markdown(f"<p class='hud-label'>Workout Status</p><p class='hud-value'>{status_text}</p>", unsafe_allow_html=True)

        if st.button("End Workout & Save", key="save_workout"):
            if not st.session_state.get('current_workout_id'):
                st.error("No active workout session. Start a workout first.")
            else:
                reps = st.session_state['tracker'].counter
                acc = st.session_state['tracker'].accuracy
                workout_id = st.session_state['current_workout_id']
                db_manager.log_exercise(
                    workout_id,
                    exercise,
                    reps,
                    acc,
                    st.session_state['last_ai_feedback'],
                )
                calories = db_manager.calculate_burned_calories(exercise, reps)
                db_manager.end_workout(workout_id, calories)
                st.success(f"Saved {reps} reps and estimated {calories:.1f} kcal.")
                st.session_state['current_workout_id'] = None
                st.session_state['workout_started'] = False
                st.session_state['tracker'].reset()

        st.markdown("</div>", unsafe_allow_html=True)
