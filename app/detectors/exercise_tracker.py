import cv2
import numpy as np

class ExerciseTracker:
    def __init__(self):
        self.counter = 0
        self.stage = None
        self.feedback = "Ready"
        self.accuracy = 0

    def analyze_squat(self, detector, img):
        angle = detector.calculate_angle(24, 26, 28)
        if angle != 0:
            per = np.interp(angle, (90, 160), (100, 0))
            if per > 85 and self.stage == "up":
                self.stage = "down"
                self.feedback = "Good depth!"
            elif per < 20 and self.stage == "down":
                self.stage = "up"
                self.counter += 1
                self.feedback = "Strong rep!"
            self.accuracy = per
            cv2.putText(img, f"Squats: {self.counter}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, f"Form: {int(per)}%", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if per > 75 else (0, 0, 255), 2)
        return img, self.counter, self.feedback, self.accuracy

    def analyze_bicep_curl(self, detector, img, arm="right"):
        if arm == "right":
            angle = detector.calculate_angle(12, 14, 16)
        else:
            angle = detector.calculate_angle(11, 13, 15)
        if angle != 0:
            per = np.interp(angle, (30, 160), (100, 0))
            if per > 80 and self.stage == "down":
                self.stage = "up"
                self.feedback = "Squeeze and control it!"
            elif per < 20 and self.stage == "up":
                self.stage = "down"
                self.counter += 1
                self.feedback = "Nice curl!"
            self.accuracy = per
            cv2.putText(img, f"Curls: {self.counter}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, f"Form: {int(per)}%", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if per > 75 else (0, 0, 255), 2)
        return img, self.counter, self.feedback, self.accuracy

    def analyze_pushup(self, detector, img):
        angle = detector.calculate_angle(11, 13, 15)
        if angle != 0:
            per = np.interp(angle, (70, 160), (100, 0))
            if per > 85 and self.stage == "up":
                self.stage = "down"
                self.feedback = "Lower with control."
            elif per < 25 and self.stage == "down":
                self.stage = "up"
                self.counter += 1
                self.feedback = "Solid push-up!"
            self.accuracy = per
            cv2.putText(img, f"Pushups: {self.counter}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, f"Form: {int(per)}%", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if per > 70 else (0, 0, 255), 2)
        return img, self.counter, self.feedback, self.accuracy

    def analyze_lunge(self, detector, img):
        angle = detector.calculate_angle(24, 26, 28)
        if angle != 0:
            per = np.interp(angle, (80, 160), (100, 0))
            if per > 85 and self.stage == "up":
                self.stage = "down"
                self.feedback = "Step deep."
            elif per < 25 and self.stage == "down":
                self.stage = "up"
                self.counter += 1
                self.feedback = "Nice lunge!"
            self.accuracy = per
            cv2.putText(img, f"Lunges: {self.counter}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, f"Balance: {int(per)}%", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if per > 70 else (0, 0, 255), 2)
        return img, self.counter, self.feedback, self.accuracy

    def analyze_plank(self, detector, img):
        angle = detector.calculate_angle(11, 23, 25)
        if angle != 0:
            per = np.interp(angle, (140, 180), (0, 100))
            self.accuracy = per
            self.feedback = "Hold strong." if per > 80 else "Keep your hips level."
            cv2.putText(img, f"Plank Hold", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, f"Alignment: {int(per)}%", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if per > 80 else (0, 0, 255), 2)
        return img, self.counter, self.feedback, self.accuracy

    def analyze_jumping_jack(self, detector, img):
        if hasattr(detector, 'lmList') and detector.lmList:
            right_wrist = detector.lmList[16][1]
            left_wrist = detector.lmList[15][1]
            span = abs(right_wrist - left_wrist)
            per = np.interp(span, (80, 220), (0, 100))
            if per > 75 and self.stage == "closed":
                self.stage = "open"
                self.feedback = "Jump wide!"
            elif per < 40 and self.stage == "open":
                self.stage = "closed"
                self.counter += 1
                self.feedback = "Great rep!"
            self.accuracy = per
            cv2.putText(img, f"Jacks: {self.counter}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, f"Range: {int(per)}%", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if per > 70 else (0, 0, 255), 2)
        return img, self.counter, self.feedback, self.accuracy

    def reset(self):
        self.counter = 0
        self.stage = None
        self.feedback = "Ready"
        self.accuracy = 0
