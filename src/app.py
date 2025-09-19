
import streamlit as st
import subprocess
import sys
from main import build_game

st.set_page_config(page_title="🎮 Game Builder AI", layout="centered")
st.title("🎮 Game Builder AI")
st.write("Describe your game and let AI build & run it automatically!")

# Input fields
game_name = st.text_input("Game Name", placeholder="e.g., Snake Game")
game_type = st.selectbox("Game Type", ["Console", "Tkinter", "Pygame"])
difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
mechanics = st.text_area(
    "Game Mechanics",
    placeholder="Describe rules, scoring system, and gameplay flow here...",
    height=150
)

def launch_game(code_path):
    """Run the generated game in a new window."""
    try:
        subprocess.Popen([sys.executable, code_path])
        st.info("Game is running in a new window!")
    except Exception as e:
        st.error(f"Failed to run game automatically: {e}")

# Build & Run
if st.button("🚀 Build & Run Game"):
    if not mechanics.strip():
        st.warning("Please describe the game mechanics before building.")
    else:
        description = f"Game: {game_name}\nType: {game_type}\nDifficulty: {difficulty}\nMechanics: {mechanics}"

        with st.spinner("🛠️ AI is building your game..."):
            final_code_str = build_game(description)

        st.subheader("✅ Generated Game Code")
        st.code(final_code_str, language="python")
        st.success("Game generated successfully!")

        # Save & launch
        file_path = "generated_game.py"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(final_code_str)

        launch_game(file_path)

        # Play Again button
        if st.button("🔄 Play Again"):
            st.info("Re-launching the game...")
            launch_game(file_path)
