import librosa
import numpy as np
import soundfile as sf
from scipy.signal import wiener
from pathlib import Path

def calculate_snr(audio):
    """Estimate Signal-to-Noise Ratio."""
    noise = audio - wiener(audio)
    signal_power = np.mean(audio ** 2)
    noise_power = np.mean(noise ** 2)
    snr = 10 * np.log10(signal_power / (noise_power + 1e-8))
    return snr

def extract_pitch(audio, sr):
    """Extract F0 Pitch contour."""
    pitches, magnitudes = librosa.piptrack(y=audio, sr=sr)
    pitch_values = pitches[magnitudes > np.median(magnitudes)]
    if len(pitch_values) == 0:
        return 0, 0
    return np.mean(pitch_values), np.std(pitch_values)

def speaking_rate(audio, sr):
    """Estimate speaking rate (words per minute)."""
    intervals = librosa.effects.split(audio, top_db=30)
    total_voiced_seconds = sum((end - start) / sr for start, end in intervals)
    # Approx 150 words/min normal speech
    estimated_wpm = (total_voiced_seconds / 60) * 150
    return estimated_wpm

def analyze_audio_file(file_path):
    print(f"\nAnalyzing: {file_path}")
    audio, sr = librosa.load(file_path, sr=None)

    duration = librosa.get_duration(y=audio, sr=sr)
    snr = calculate_snr(audio)
    pitch_mean, pitch_std = extract_pitch(audio, sr)
    wpm = speaking_rate(audio, sr)

    print(f"Sample Rate: {sr}")
    print(f"Duration: {duration:.2f} seconds")
    print(f"SNR: {snr:.2f} dB")
    print(f"Pitch Mean: {pitch_mean:.2f}")
    print(f"Pitch Std Dev: {pitch_std:.2f}")
    print(f"Estimated Speaking Rate: {wpm:.2f} words/min")

def analyze_dataset(folder_path):
    folder = Path(folder_path)
    print(f"\n--- Dataset Analysis for Folder: {folder} ---")

    if not folder.exists():
        print("❌ Folder does not exist!")
        return
    
    if not folder.is_dir():
        print("❌ Path exists but is not a directory!")
        return

    wav_files = list(folder.glob("*.wav"))

    if not wav_files:
        print("⚠️ No .wav files found in this folder.")
        return

    for file_path in wav_files:
        analyze_audio_file(str(file_path))

if __name__ == "__main__":
    folder = r"./samples/user_audio"
    analyze_dataset(folder)
