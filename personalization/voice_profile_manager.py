import json
from pathlib import Path
import datetime

class VoiceProfileManager:

    def __init__(self, save_dir="profiles"):
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(exist_ok=True)

    def save_profile(self, user_id, profile_data):
        """Save a learned voice profile to JSON."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = self.save_dir / f"{user_id}_profile_{timestamp}.json"

        with open(file_path, "w") as f:
            json.dump(profile_data, f, indent=4)

        return file_path

    def load_profile(self, file_path):
        """Load a saved voice profile JSON."""
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError("Profile file not found!")
        
        with open(file_path, "r") as f:
            data = json.load(f)

        return data

    def list_profiles(self):
        """List all saved profiles."""
        return list(self.save_dir.glob("*.json"))


if __name__ == "__main__":
    manager = VoiceProfileManager()

    # Dummy example
    sample_profile = {
        "speaking_patterns": {"speaking_rate": 120, "avg_pause": 0.2},
        "prosody_patterns": {"pitch_mean": 200, "pitch_std": 20},
        "emotion_patterns": {"spectral_centroid": 1200}
    }

    print("\nSaving example profile...")
    saved_path = manager.save_profile("user123", sample_profile)
    print("Saved at:", saved_path)

    print("\nLoading profile...")
    loaded = manager.load_profile(saved_path)
    print("Loaded Data:", loaded)

    print("\nAvailable Profiles:", manager.list_profiles())
