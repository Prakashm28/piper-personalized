import numpy as np

class PatternLearner:

    def __init__(self):
        self.profiles = {}

    def learn_speaking_pattern(self, features):
        return {
            "speaking_rate": float(features["speaking_rate"]),
            "avg_pause": float(features["pauses"]["avg_pause"]),
            "max_pause": float(features["pauses"]["max_pause"]),
            "min_pause": float(features["pauses"]["min_pause"]),
        }

    def learn_pitch_pattern(self, features):
        pitch_mean, pitch_std = features["pitch_mean_std"]
        return {
            "pitch_mean": float(pitch_mean),
            "pitch_std": float(pitch_std),
            "energy": float(features["energy"])
        }

    def learn_emotion_pattern(self, features):
        emo = features["emotion_features"]
        return {
            "spectral_centroid": float(emo["spectral_centroid"]),
            "spectral_bandwidth": float(emo["spectral_bandwidth"]),
            "rolloff": float(emo["rolloff"])
        }

    def learn(self, features):
        """Combine all pattern types into one learned profile."""
        speaking = self.learn_speaking_pattern(features)
        pitch = self.learn_pitch_pattern(features)
        emotion = self.learn_emotion_pattern(features)

        combined_profile = {
            "speaking_patterns": speaking,
            "prosody_patterns": pitch,
            "emotion_patterns": emotion
        }

        return combined_profile


if __name__ == "__main__":
    ##Example dummy data for testing
    dummy_features = {
        "speaking_rate": 120.0,
        "pauses": {"avg_pause": 0.2, "max_pause": 1.0, "min_pause": 0.05},
        "pitch_mean_std": (210.0, 20.0),
        "energy": 0.5,
        "emotion_features": {"spectral_centroid": 1200, "spectral_bandwidth": 300, "rolloff": 3800}
    }

    learner = PatternLearner()
    profile = learner.learn(dummy_features)
    print("\nLearned Pattern Profile:\n", profile)
