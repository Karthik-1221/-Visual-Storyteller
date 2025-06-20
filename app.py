import streamlit as st
from PIL import Image
from transformers import pipeline
import random

# Load generator once
@st.cache_resource
def load_generator():
    return pipeline("text-generation", model="gpt2")

# Generate multiple story drafts with tone
def generate_story(prompt, tone):
    styles = {
        "humorous": "Write a funny story about: ",
        "dramatic": "Write a dramatic tale involving: ",
        "poetic": "Write a poetic narrative about: "
    }

    base_prompt = styles[tone]
    story_prompts = [
        base_prompt + prompt,
        base_prompt + "This scene reminds me of " + prompt,
        base_prompt + "Imagine this: " + prompt
    ]

    generator = load_generator()
    stories = [generator(p, max_length=150, do_sample=True, temperature=0.9)[0]['generated_text'] for p in story_prompts]
    return stories

# --- Streamlit Interface ---
st.set_page_config(page_title="Visual Storyteller", layout="centered")

st.title("📖 Visual Storyteller")
st.caption("Upload images, enter a prompt, choose a tone, and let the AI weave a story.")

uploaded_files = st.file_uploader("Upload 1–3 images", type=["jpg", "png"], accept_multiple_files=True)
prompt = st.text_input("Enter your story prompt")
tone = st.selectbox("Choose a tone", ["humorous", "dramatic", "poetic"])

if "story_index" not in st.session_state:
    st.session_state.story_index = 0
if "stories" not in st.session_state:
    st.session_state.stories = []

if st.button("Generate Story"):
    if uploaded_files and prompt:
        images = [Image.open(f) for f in uploaded_files]  # Placeholder for future use
        st.session_state.stories = generate_story(prompt, tone)
        st.session_state.story_index = 0

if st.session_state.stories:
    st.markdown("### ✨ Your Story")
    st.write(st.session_state.stories[st.session_state.story_index])

    if st.button("🔄 Regenerate"):
        st.session_state.story_index = (st.session_state.story_index + 1) % len(st.session_state.stories)