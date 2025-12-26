# 📘 CHANGELOG – Piper TTS Personalization Engine

This changelog documents all major updates, fixes, and enhancements made during the development of the Personalized Piper TTS system.

---

## 🗓️ Version 1.0.0 – Initial Release
### ✔ Project Structure Setup
- Created base project folders:
  - `personalization/`
  - `samples/`
  - `docs/`
  - `tools/`

### ✔ Environment Setup
- Installed required Python dependencies  
- Configured virtual environment  
- Installed *espeak-ng*, *phonemizer*, *librosa*, *soundfile*, *numpy*

### ✔ Core Module Creation
- Added `audio_preprocessor.py`
- Added `feature_extractor.py`
- Added `pattern_learner.py`
- Added `voice_profile_manager.py`
- Added `synthesis_adapter.py`

### ✔ Tools Added
- `dataset_analyzer.py` to inspect audio quality  
- Automatic WAV scanning  
- SNR, pitch, speaking rate calculation

### ✔ Documentation Added
- `README.md`  
- `DATASET_ANALYSIS.md`  
- `ARCHITECTURE.md`  
- `DIAGRAMS.md`  
- Basic file placeholders for logs and changelog  

---

## 🗓️ Version 1.1.0 – Personalization Engine Stable
### ✔ Completed Personalization Pipeline  
- User audio preprocessing  
- Feature extraction pipeline  
- Pattern learning system  
- JSON profile generation  
- Integration with Piper TTS  
- Personalized synthesis output  

### ✔ Added CLI Commands
- Training:
  ```
  python main.py train --user_audio path.wav --user_id user
  ```
- Synthesis:
  ```
  python main.py synthesize --text "Hello" --profile profiles/user.json
  ```

### ✔ Added Exception Handling
- Missing audio directory  
- Invalid WAV formats  
- Missing profile  
- Piper execution errors  

---

## 🗓️ Version 1.2.0 – Documentation Expansion
### ✔ Added Mermaid diagrams
- System architecture  
- Data flow  
- Component interaction  
- Personalization workflow  
- Piper integration  

### ✔ Improved README.md
- Setup instructions  
- Requirements  
- Usage flow  
- Example commands  

---

## 🗓️ Version 1.3.0 – Final Submission Prep
### ✔ Ensured folder structure matches project PDF  
### ✔ Validated dataset analysis output  
### ✔ Verified personalized pipeline end-to-end  
### ✔ Created complete documentation set for interview/demo  

---

# ✅ END OF CHANGELOG.md
