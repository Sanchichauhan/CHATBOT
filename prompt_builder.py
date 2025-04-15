import streamlit as st
import random

# Sample elements to mix and match
genres = ["Fantasy", "Science Fiction", "Romance", "Horror", "Mystery", "Adventure"]
themes = ["Betrayal", "Redemption", "Time Travel", "Forbidden Love", "Apocalypse", "Self-Discovery"]
characters = ["a lonely astronaut", "a rebellious princess", "an AI with emotions", "a vampire detective", "a cursed pirate"]
settings = ["on a distant planet", "in a haunted mansion", "during a world war", "inside a simulation", "in a future dystopia"]

# Page configuration
st.set_page_config(page_title="Creative Prompt Builder", page_icon="✍️")

st.title("✍️ Creative Prompt Builder Chatbot")

st.markdown("Mix and match elements to generate a writing prompt!")

# User selections
genre = st.selectbox("Choose a genre:", genres)
theme = st.selectbox("Choose a theme:", themes)
character = st.selectbox("Choose a main character:", characters)
setting = st.selectbox("Choose a setting:", settings)

if st.button("Generate Prompt"):
    prompt = f"Write a {genre.lower()} story about {character} {setting}, exploring the theme of {theme.lower()}."
    st.success(prompt)

# Add randomizer
if st.button("I'm Feeling Lucky 🎲"):
    prompt = f"Write a {random.choice(genres).lower()} story about {random.choice(characters)} {random.choice(settings)}, exploring the theme of {random.choice(themes).lower()}."
    st.info(prompt)
