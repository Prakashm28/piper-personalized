# 📊 DIAGRAMS – Piper TTS Personalization Engine

This document contains all architecture and workflow diagrams required for the Piper personalization project.  
All diagrams are written in **Mermaid** format and compatible with GitHub markdown.

---

# 🔹 1. System Architecture Diagram

```mermaid
flowchart TD
    A[User Audio Input] --> B[Audio Preprocessor<br/>• Noise Reduction<br/>• Silence Trimming<br/>• Normalization<br/>• Resampling]
    B --> C[Feature Extractor<br/>• Pitch / Energy<br/>• Speaking Rate<br/>• Pauses<br/>• Emotion Features]
    C --> D[Pattern Learner<br/>• Prosody Patterns<br/>• Speaking Style<br/>• Emotional Tendencies]
    D --> E[Voice Profile Manager<br/>Store as JSON/YAML]
    E --> F[Synthesis Adapter<br/>• Pitch Shift<br/>• Speed Adjust<br/>• Pause Control<br/>• Emotion Coloring]
    F --> G[Piper TTS Engine<br/>Base Voice Generation]
    G --> H[Final Personalized Voice Output]
```

---

# 🔹 2. Data Flow Diagram (DFD – Level 1)

```mermaid
flowchart LR
    UA[User Audio] --> AP[Audio Preprocessor]
    AP --> FE[Feature Extractor]
    FE --> PL[Pattern Learner]
    PL --> VP[Voice Profile JSON]
    TXT[Input Text] --> PIPER[Piper TTS Engine]
    PIPER --> SA[Synthesis Adapter]
    VP --> SA
    SA --> OUT[Final Output Audio]
```

---

# 🔹 3. Component Interaction Diagram

```mermaid
sequenceDiagram
    participant User
    participant Preprocessor
    participant Extractor
    participant Learner
    participant ProfileManager
    participant Piper
    participant SynthAdapter
    participant Output

    User->>Preprocessor: Upload Audio
    Preprocessor->>Extractor: Cleaned Audio
    Extractor->>Learner: Extracted Features
    Learner->>ProfileManager: Save Profile JSON
    User->>Piper: Provide Text
    Piper->>SynthAdapter: Base Piper Output
    ProfileManager->>SynthAdapter: Load User Profile
    SynthAdapter->>Output: Personalized Audio
```

---

# 🔹 4. Personalization Workflow Diagram

```mermaid
flowchart TD
    A[Start Training] --> B[Load User Audio]
    B --> C[Preprocess Audio]
    C --> D[Extract Features]
    D --> E[Learn Patterns]
    E --> F[Save Voice Profile JSON]
    F --> G[Training Complete]

    G --> H[Start Synthesis]
    H --> I[Generate Base Audio (Piper)]
    I --> J[Apply Personalization<br/>Pitch / Speed / Pauses / Emotion]
    J --> K[Save Final Output]
```

---

# 🔹 5. Piper Integration Diagram

```mermaid
flowchart LR
    TEXT[Input Text] --> P[Piper Base Model]
    P --> RAW[Raw Audio Output]
    PROFILE[User Voice Profile] --> SA[Synthesis Adapter]
    RAW --> SA
    SA --> FINAL[Personalized Audio Output]
```

---

# ✅ END OF DIAGRAMS.md
