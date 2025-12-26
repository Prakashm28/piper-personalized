import librosa
import numpy as np
import soundfile as sf
from scipy.signal import wiener
from pathlib import Path

class AudioPreprocessor:

    def __init__(self, target_sr=22050):
        self.target_sr = target_sr

    def load_audio(self, file_path):
        audio, sr = librosa.load(file_path, sr=None)
        return audio, sr

    def resample(self, audio, sr):
        if sr != self.target_sr:
            audio = librosa.resample(audio, orig_sr=sr, target_sr=self.target_sr)
        return audio

    def denoise(self, audio):
        return wiener(audio)

    def normalize(self, audio):
        # Peak normalization
        return audio / (np.max(np.abs(audio)) + 1e-9)

    def trim_silence(self, audio):
        trimmed, _ = librosa.effects.trim(audio, top_db=30)
        return trimmed

    def preprocess(self, file_path):
        audio, sr = self.load_audio(file_path)
        audio = self.resample(audio, sr)
        audio = self.denoise(audio)
        audio = self.normalize(audio)
        audio = self.trim_silence(audio)
        return audio, self.target_sr


if __name__ == "__main__":
    pre = AudioPreprocessor()
    test_file = input("Enter path to audio file: ")
    processed, sr = pre.preprocess(test_file)
    print(f"Processed audio length: {len(processed)} samples at {sr} Hz")
