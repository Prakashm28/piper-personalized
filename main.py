import argparse
import soundfile as sf
import numpy as np

from personalization.audio_preprocessor import AudioPreprocessor
from personalization.feature_extractor import FeatureExtractor
from personalization.pattern_learner import PatternLearner
from personalization.voice_profile_manager import VoiceProfileManager
from personalization.synthesis_adapter import SynthesisAdapter

class PersonalizationEngine:

    def __init__(self):
        self.preprocessor = AudioPreprocessor()
        self.extractor = FeatureExtractor()
        self.learner = PatternLearner()
        self.profile_manager = VoiceProfileManager()
        self.adapter = SynthesisAdapter()

    # -------------------------------------------------------------
    # TRAIN USER PERSONALIZED PROFILE
    # -------------------------------------------------------------
    def train(self, file_path, user_id):
        print("\n🔄 Preprocessing audio...")
        audio, sr = self.preprocessor.preprocess(file_path)

        print("🔍 Extracting features...")
        features = self.extractor.extract_all(audio)

        print("🧠 Learning user-specific patterns...")
        profile = self.learner.learn(features)

        print("💾 Saving profile...")
        path = self.profile_manager.save_profile(user_id, profile)

        print(f"\n✅ Profile saved successfully at:\n{path}")
        return path

    # -------------------------------------------------------------
    # GENERATE PERSONALIZED SPEECH
    # -------------------------------------------------------------
    def synthesize(self, text, profile_path, output_path="output.wav"):
        print("\n📂 Loading voice profile...")
        profile = self.profile_manager.load_profile(profile_path)

        print("🗣 Generating base TTS output using Piper...")
        import subprocess
        subprocess.run([
    "piper",
    "--model", "piper-voices/en_US-amy-medium.onnx",
    "--config", "piper-voices/en_US-amy-medium.onnx.json",
    "--output_file", "base.wav"
], input=text, text=True)

        base_audio, sr = sf.read("base.wav")

        print("🎨 Applying personalization...")
        personalized_audio = self.adapter.apply_personalization(
            base_audio, sr, profile
        )

        print(f"💾 Saving personalized audio to: {output_path}")
        sf.write(output_path, personalized_audio, sr)

        print("\n✅ Personalized audio generation complete!")

# -------------------------------------------------------------
# CLI HANDLER
# -------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("mode", choices=["train", "synthesize"], help="Choose mode")

    parser.add_argument("--user_audio", type=str, help="Path to user audio file")
    parser.add_argument("--user_id", type=str, help="Unique user ID")

    parser.add_argument("--text", type=str, help="Text to synthesize")
    parser.add_argument("--profile", type=str, help="Path to saved voice profile")

    args = parser.parse_args()
    engine = PersonalizationEngine()

    if args.mode == "train":
        if not args.user_audio or not args.user_id:
            print("❌ Missing arguments. Use: python main.py train --user_audio <file> --user_id <id>")
            return
        engine.train(args.user_audio, args.user_id)

    elif args.mode == "synthesize":
        if not args.text or not args.profile:
            print("❌ Missing arguments. Use: python main.py synthesize --text <text> --profile <file>")
            return
        engine.synthesize(args.text, args.profile)

if __name__ == "__main__":
    main()
