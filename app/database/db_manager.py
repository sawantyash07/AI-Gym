import sqlite3
import os
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path="data/ai_gym.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_path, check_same_thread=False)

    def calculate_burned_calories(self, exercise_name, reps):
        burn_rate = {
            "Squat": 0.18,
            "Pushup": 0.12,
            "Bicep Curl": 0.14,
            "Lunge": 0.16,
            "Plank": 0.08,
            "Jumping Jack": 0.15,
        }
        rate = burn_rate.get(exercise_name, 0.12)
        return round(rate * max(reps, 0), 2)

    def get_user_goals(self, user_id):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, goal_type, target_value, current_value, deadline, is_completed FROM goals WHERE user_id = ?', (user_id,))
            return cursor.fetchall()

    def init_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Users Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    height_cm REAL,
                    weight_kg REAL,
                    fitness_level TEXT DEFAULT 'Beginner'
                )
            ''')
            
            # Workouts Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS workouts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    end_time TIMESTAMP,
                    total_calories REAL DEFAULT 0,
                    workout_type TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            
            # Exercise Logs Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS exercise_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    workout_id INTEGER NOT NULL,
                    exercise_name TEXT NOT NULL,
                    reps INTEGER DEFAULT 0,
                    sets INTEGER DEFAULT 1,
                    accuracy_score REAL DEFAULT 0,
                    ai_feedback TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (workout_id) REFERENCES workouts (id)
                )
            ''')

            # Goals Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS goals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    goal_type TEXT NOT NULL,
                    target_value REAL NOT NULL,
                    current_value REAL DEFAULT 0,
                    deadline DATE,
                    is_completed BOOLEAN DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            conn.commit()

    # User operations
    def create_user(self, username, email, password_hash):
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
                               (username, email, password_hash))
                conn.commit()
                return True, "User created successfully"
        except sqlite3.IntegrityError:
            return False, "Username or email already exists"
        except Exception as e:
            return False, str(e)

    def get_user_by_username(self, username):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, username, email, password_hash, height_cm, weight_kg, fitness_level FROM users WHERE username = ?', (username,))
            row = cursor.fetchone()
            if row:
                return {
                    'id': row[0],
                    'username': row[1],
                    'email': row[2],
                    'password_hash': row[3],
                    'height_cm': row[4],
                    'weight_kg': row[5],
                    'fitness_level': row[6]
                }
            return None
            
    def get_user_by_email(self, email):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, username, email, password_hash FROM users WHERE email = ?', (email,))
            row = cursor.fetchone()
            if row:
                return {
                    'id': row[0],
                    'username': row[1],
                    'email': row[2],
                    'password_hash': row[3]
                }
            return None

    def update_user_profile(self, user_id, height_cm, weight_kg, fitness_level):
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE users 
                    SET height_cm = ?, weight_kg = ?, fitness_level = ?
                    WHERE id = ?
                ''', (height_cm, weight_kg, fitness_level, user_id))
                conn.commit()
                return True
        except Exception as e:
            print(f"Error updating profile: {e}")
            return False

    # Workout operations
    def start_workout(self, user_id, workout_type="General"):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO workouts (user_id, workout_type) VALUES (?, ?)', (user_id, workout_type))
            conn.commit()
            return cursor.lastrowid

    def end_workout(self, workout_id, total_calories):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE workouts 
                SET end_time = CURRENT_TIMESTAMP, total_calories = ? 
                WHERE id = ?
            ''', (total_calories, workout_id))
            conn.commit()

    def log_exercise(self, workout_id, exercise_name, reps, accuracy_score, ai_feedback):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO exercise_logs (workout_id, exercise_name, reps, accuracy_score, ai_feedback)
                VALUES (?, ?, ?, ?, ?)
            ''', (workout_id, exercise_name, reps, accuracy_score, ai_feedback))
            conn.commit()

    def get_user_workouts(self, user_id, limit=10):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, start_time, end_time, total_calories, workout_type
                FROM workouts 
                WHERE user_id = ? 
                ORDER BY start_time DESC 
                LIMIT ?
            ''', (user_id, limit))
            return cursor.fetchall()
            
    def get_workout_logs(self, workout_id):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT exercise_name, reps, sets, accuracy_score, ai_feedback, timestamp
                FROM exercise_logs
                WHERE workout_id = ?
                ORDER BY timestamp ASC
            ''', (workout_id,))
            return cursor.fetchall()
