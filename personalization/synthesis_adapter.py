import numpy as np
import librosa

class SynthesisAdapter:

    def __init__(self):
        pass


    # Pitch Modification
    def apply_pitch_shift(self, audio, sr, semitones):
        if semitones == 0:
            return audio
        return librosa.effects.pitch_shift(audio, sr=sr, n_steps=semitones)

    # Speaking Rate (Speed) Modification  **FIXED**
    def apply_speed_change(self, audio, rate):
        import numpy as np

        if rate == 1.0:
            return audio

        # Convert stereo → mono (librosa requires mono)
        if len(audio.shape) > 1:
            audio = np.mean(audio, axis=1)

        # librosa time_stretch must use keyword arguments
        return librosa.effects.time_stretch(y=audio, rate=rate)


    # Insert Pauses Based on User Profile
    def apply_pause_insertion(self, audio, sr, pause_sec):
        if pause_sec <= 0:
            return audio

        pause_samples = int(pause_sec * sr)
        pause = np.zeros(pause_samples)
        return np.concatenate((audio, pause))


    # Emotion Adjustment (Simplified)
    def apply_emotion(self, audio, sr, emotion_profile):
        """
        Modify audio tone/energy based on emotion profile.
        This is a lightweight simulation.
        """

        centroid = emotion_profile.get("spectral_centroid", 0)
        bandwidth = emotion_profile.get("spectral_bandwidth", 0)

        # Increase brightness for "excited" profiles
        if centroid > 1500:
            audio = audio * 1.1  # boost energy slightly

        # Reduce harshness for calm/sad tones
        if bandwidth < 200:
            audio = audio * 0.9

        # Normalize audio to avoid clipping
        audio = audio / (np.max(np.abs(audio)) + 1e-9)
        return audio


    # Main Adaptation Pipeline
    def apply_personalization(self, audio, sr, profile):
        # Extract patterns
        speaking_rate = profile["speaking_patterns"]["speaking_rate"]
        avg_pause = profile["speaking_patterns"]["avg_pause"]

        pitch_mean = profile["prosody_patterns"]["pitch_mean"]
        user_pitch_shift = (pitch_mean - 200) / 25  # shift relative to neutral pitch

        emotion_profile = profile["emotion_patterns"]

        # Apply pitch
        audio = self.apply_pitch_shift(audio, sr, user_pitch_shift)

        # Apply speaking rate (convert wpm to speed factor)
        speed_factor = min(max(speaking_rate / 150, 0.5), 1.5)
        audio = self.apply_speed_change(audio, speed_factor)

        # Apply pause insertion
        audio = self.apply_pause_insertion(audio, sr, avg_pause)

        # Apply emotion adjustment
        audio = self.apply_emotion(audio, sr, emotion_profile)

        return audio


if __name__ == "__main__":
    print("SynthesisAdapter module loaded successfully.")
