# 🏗️ System Architecture – Piper TTS Personalization Engine

This document explains the full architecture of the **Personalized Speech Learning System**, created on top of **Piper TTS**.

It includes:
- High-level system architecture  
- Module responsibilities  
- Data flow pipeline  
- Personalization workflow  
- Integration points with Piper  

---

# 🔹 1. High-Level Architecture Overview

```
+-------------------------------------------------------------+
|                        User Audio                           |
+-------------------------------------------------------------+
                              │
                              ▼
+-------------------------------------------------------------+
|                    Audio Preprocessor                       |
|  - Noise reduction                                           |
|  - Silence trimming                                          |
|  - Normalization                                             |
|  - Resampling                                                |
+-------------------------------------------------------------+
                              │
                              ▼
+-------------------------------------------------------------+
|                    Feature Extractor                        |
|  - Pitch / Energy                                            |
|  - Speaking rate / pauses                                    |
|  - Emotion spectral features                                 |
+-------------------------------------------------------------+
                              │
                              ▼
+-------------------------------------------------------------+
|                       Pattern Learner                       |
|  Learns:                                                     |
|    - Speaking patterns                                       |
|    - Prosody / stress patterns                               |
|    - Emotion tendencies                                      |
+-------------------------------------------------------------+
                              │
                              ▼
+-------------------------------------------------------------+
|               Voice Profile Manager (JSON/YAML)             |
|  Stores learned profile using user ID                        |
+-------------------------------------------------------------+
                              │
                              ▼
+-------------------------------------------------------------+
|                      Synthesis Adapter                      |
|  Applies personalization to Piper output:                    |
|    - Pitch shift                                             |
|    - Speed adjustment                                        |
|    - Pause insertion                                         |
|    - Emotion coloration                                      |
+-------------------------------------------------------------+
                              │
                              ▼
+-------------------------------------------------------------+
|                     Final Audio Output                      |
+-------------------------------------------------------------+
```

---

# 🔹 2. Component Responsibilities

### **AudioPreprocessor**
- Loads audio  
- Removes noise (Wiener filter)  
- Removes silence  
- Normalizes amplitude  
- Resamples to 22,050 Hz  

### **FeatureExtractor**
Extracts:
- Speaking rate  
- Pause statistics  
- Pitch mean + variance  
- Energy  
- Spectral emotion features  

### **PatternLearner**
Learns:
- Speaking patterns  
- Prosody (pitch, energy)  
- Emotional tendencies  

### **VoiceProfileManager**
- Saves profiles as JSON  
- Loads profiles  
- Lists profile versions  
- Organizes profiles by user  

### **SynthesisAdapter**
Applies personalization to Piper-generated audio:
- Pitch shift based on user pitch mean  
- Speed modifications from speaking rate  
- Pause insertion from user pauses  
- Emotion coloration from spectral features  

---

# 🔹 3. End-to-End Data Flow

```
User Audio
    → Preprocessor
    → FeatureExtractor
    → PatternLearner
    → VoiceProfile (JSON)
    → Piper TTS Output
    → SynthesisAdapter
    → Final Personalized Voice
```

---

# 🔹 4. Integration with Piper TTS

### 1️⃣ Piper generates base speech audio:

```
piper --model en_US-amy-medium.onnx --output_file base.wav
```

### 2️⃣ The SynthesisAdapter modifies this audio:
- Pitch  
- Speed / Rate  
- Pauses  
- Emotional tone  

### 3️⃣ Output saved as:

```
output.wav
```

---

# 🔹 5. Runtime Workflow (Training)

### Command:

```
python main.py train --user_audio path.wav --user_id prakash
```

### Steps:
1. Preprocess audio  
2. Extract features  
3. Learn patterns  
4. Save profile JSON  

---

# 🔹 6. Runtime Workflow (Synthesis)

### Command:

```
python main.py synthesize --text "Hello" --profile profiles/prakash_profile.json
```

### Steps:
1. Piper generates neutral audio  
2. Synthesis adapter personalizes the audio  
3. Saves final output  

---

# 🔹 7. Notes and Limitations
- Not a neural fine-tune of Piper (statistical personalization)  
- Requires clean audio for high-quality results  
- Emotion processing is simplified  
- Works offline and runs fast  

---

# ✅ END OF ARCHITECTURE.md
