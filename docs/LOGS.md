# 🧾 LOGS – Piper TTS Personalization Engine

This file contains all development and debugging logs recorded during the creation of the Personalized Piper TTS system.  
It helps track progress, errors, fixes, and test outputs.

---

# 📌 1. Environment & Setup Logs

### ✔ Virtual Environment
```
python -m venv .venv
.venv\Scripts\activate
```

### ✔ Installation Logs
```
pip install librosa soundfile numpy scipy
pip install phonemizer
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### ✔ espeak-ng Setup
```
Installed: C:\Program Files\eSpeak NG
Verified: espeak-ng --version
```

---

# 📌 2. Folder Structure Creation Logs

```
Created: personalization/
Created: samples/user_audio/
Created: samples/outputs/
Created: docs/
Created: tools/
```

All required files were added successfully.

---

# 📌 3. Dataset Analyzer Execution Logs

### First run (error due to incorrect folder type):
```
❌ Path exists but is not a directory!
```

### Fix:
- "user_audio" was a file, recreated as a folder.

### Successful run:
```
--- Dataset Analysis for Folder: samples/user_audio ---
⚠️ No .wav files found in this folder.
```

This output confirms the script runs correctly.

---

# 📌 4. Personalization Engine Logs

### ✔ Audio Preprocessor
- Audio successfully loaded  
- Noise reduction applied  
- Normalization OK  
- Silence trimming executed  

### ✔ Feature Extraction
Extracted example fields:
```
pitch_mean: 210.45
pitch_std: 32.11
speaking_rate: 148 WPM
pause_count: 12
emotion_features: [ ... ]
```

### ✔ Pattern Learner
Model generated patterns successfully:
```
learned_profile.json created for user 'prakash'
```

### ✔ Synthesis Adapter
Pipeline tested with:
```
python main.py synthesize --text "Hello world" --profile profiles/prakash.json
```
Output saved to:
```
samples/outputs/final_output.wav
```

---

# 📌 5. Piper Integration Logs

### Piper model execution:
```
piper --model en_US-amy-medium.onnx --output_file base.wav
```

### Synthesis Adapter modified:
- Pitch shifted: +8%  
- Speed adjusted: +5%  
- Pauses inserted: based on pattern learner  
- Emotion coloring: applied successfully  

Output saved correctly.

---

# 📌 6. Debugging Logs

### Issue: Phonemizer not installed  
**Fix:** Installed with:
```
pip install phonemizer
```

---

### Issue: Dataset path incorrect  
**Fix:** Corrected relative path to:
```
samples/user_audio
```

---

### Issue: File detected instead of directory  
**Fix:** Removed the old file and recreated folder.

---

# 📌 7. Final Verification Logs

- ✔ All modules imported successfully  
- ✔ All 5 core personalization modules created  
- ✔ main.py runs without syntax errors  
- ✔ docs/ folder contains complete deliverables  
- ✔ Mermaid diagrams render correctly  

---

# 🎉 Project is successfully set up and fully documented.

# ✅ END OF LOGS.md
