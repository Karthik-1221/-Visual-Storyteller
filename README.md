
![Ghibli storyteller](https://github.com/user-attachments/assets/f1361dbc-b2e2-49fe-b3cd-9c15358ab1b7)

# 📖 Visual Storyteller

**Visual Storyteller** is a lightweight multimodal generative AI app that transforms image sequences and user prompts into creative short stories. It blends pre-trained language models (transfer learning) with ensemble-style prompt engineering to generate engaging narratives across tones like *humorous*, *dramatic*, and *poetic*.

---

##  Project Goals

- Utilize **transfer learning** with GPT-2 for fluent, story-like text generation
- Simulate **ensembling** by producing multiple outputs from varied prompts
- Build a minimal, intuitive **Streamlit web app** for real-time storytelling
- Support creative expression on resource-limited systems (e.g., laptops)

---

##  Tech Stack

| Component        | Tool / Framework                      |
|------------------|----------------------------------------|
| UI & Deployment  | Streamlit                             |
| Text Generation  | Hugging Face `transformers` (GPT-2)    |
| Image Handling   | Pillow (PIL)                          |
| Programming Lang | Python 3.9+                            |

---

## 🛠️ Features

-  Upload up to 3 images (optional inspiration cues)
-  Custom prompt input from the user
-  Tone selector: `humorous`, `dramatic`, or `poetic`
-  Multiple story outputs using ensemble-style generation
- "Regenerate" button to switch between outputs

---

##  How It Works

1. User uploads images (optional, placeholders for future multimodal features)
2. Prompt and tone are used to craft 3 creative story starters
3. **GPT-2**, a pre-trained transformer model, generates stories for each
4. User can view and cycle through all outputs

---

##  Transfer Learning & Ensembling

- **Transfer Learning**: GPT-2 is used out-of-the-box, leveraging its language understanding without training from scratch.
- **Ensembling**: Prompt variations act as an ensemble mechanism, producing different versions of the story and letting the user rerank manually.

---

##  Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Karthik-1221/-Visual-Storyteller.git
cd Visual-Storyteller
```

2. Install Dependencies
pip install -r requirements.txt

3. Run the App
streamlit run app.py

📌 Future Improvements
-  Add CLIP-based image embeddings to condition stories on image features
-  Incorporate story-tone classifiers for real ensemble reranking
-  Deploy on Hugging Face Spaces or Streamlit Community Cloud
-  Improve layout and image preview on mobile device


