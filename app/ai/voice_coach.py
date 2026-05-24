import os
from groq import Groq
from gtts import gTTS
import base64
import streamlit as st
import io

class AIVoiceCoach:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if self.api_key:
            try:
                self.client = Groq(api_key=self.api_key)
            except Exception as e:
                print(f"Groq client initialization failed: {e}")
                self.client = None
        else:
            self.client = None

        self.system_prompt = """
You are an AI personal trainer. You are energetic, motivating, and strict but fair.
Your goal is to provide short, punchy feedback to the user based on their current workout state.
Keep responses under 2 sentences. Use fitness terminology but keep it accessible.
"""

    def generate_feedback(self, exercise, reps, form_accuracy):
        prompt = f"The user is doing {exercise}. They have completed {reps} reps. Their form accuracy is {form_accuracy}%. Give them brief, motivating feedback."
        if not self.client:
            return f"Keep going on your {exercise}! Stay focused and keep the pace up."

        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt,
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                model="llama3-8b-8192",
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"Groq API Error: {e}")
            return "You're doing great! Keep pushing!"

    def text_to_audio_html(self, text):
        try:
            tts = gTTS(text=text, lang="en", tld="us")
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            b64 = base64.b64encode(fp.read()).decode()
            return f"<audio autoplay='true' style='display:none;'><source src='data:audio/mp3;base64,{b64}' type='audio/mp3'></audio>"
        except Exception as e:
            print(f"TTS Error: {e}")
            return ""

    def play_feedback(self, text):
        audio_html = self.text_to_audio_html(text)
        if audio_html:
            st.markdown(audio_html, unsafe_allow_html=True)
