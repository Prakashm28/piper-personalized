import librosa
import numpy as np
from pathlib import Path

class FeatureExtractor:

    def __init__(self, sr=22050):
        self.sr = sr

    # Speaking Pattern Features
    def speaking_rate(self, audio):
        intervals = librosa.effects.split(audio, top_db=30)
        voiced_sec = sum((end - start) / self.sr for start, end in intervals)
        return (voiced_sec / 60) * 150  # Approx 150 wpm standard

    def pause_statistics(self, audio):
        intervals = librosa.effects.split(audio, top_db=30)
        pauses = []
        last_end = 0
        for start, end in intervals:
            pauses.append((start - last_end) / self.sr)
            last_end = end
        return {
            "avg_pause": float(np.mean(pauses)) if pauses else 0.0,
            "max_pause": float(np.max(pauses)) if pauses else 0.0,
            "min_pause": float(np.min(pauses)) if pauses else 0.0
        }

    # Prosody Features
    def extract_pitch(self, audio):
        f0, voiced_flag, voiced_probs = librosa.pyin(
            audio,
            fmin=50,
            fmax=400,
            sr=self.sr
        )
        f0 = f0[~np.isnan(f0)]
        if len(f0) == 0:
            return 0, 0
        return float(np.mean(f0)), float(np.std(f0))

    def energy(self, audio):
        energy = np.sum(np.square(audio)) / len(audio)
        return float(energy)


    # Emotion-Related Features
    def emotion_features(self, audio):
        spectral_centroid = float(np.mean(librosa.feature.spectral_centroid(y=audio, sr=self.sr)))
        spectral_bandwidth = float(np.mean(librosa.feature.spectral_bandwidth(y=audio, sr=self.sr)))
        rolloff = float(np.mean(librosa.feature.spectral_rolloff(y=audio, sr=self.sr)))

        return {
            "spectral_centroid": spectral_centroid,
            "spectral_bandwidth": spectral_bandwidth,
            "rolloff": rolloff
        }


    # Main Feature Extraction Pipeline
    def extract_all(self, audio):
        return {
            "speaking_rate": self.speaking_rate(audio),
            "pauses": self.pause_statistics(audio),
            "pitch_mean_std": self.extract_pitch(audio),
            "energy": self.energy(audio),
            "emotion_features": self.emotion_features(audio),
        }


if __name__ == "__main__":
    import soundfile as sf

    file_path = input("Enter audio file path: ")
    audio, sr = sf.read(file_path)
    extractor = FeatureExtractor(sr=sr)
    features = extractor.extract_all(audio)
    print("\nExtracted Features:\n", features)
