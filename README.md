# Game Builder AI

🎮 **Game Builder AI** is a Streamlit-powered application that lets you describe a game and have AI automatically generate and run it for you!

## Features

- **Game Generation:** Describe your game (name, type, difficulty, mechanics) and let AI build the code.
- **Supported Game Types:** Console, Tkinter, Pygame.
- **Instant Play:** Generated games can be launched directly from the app.

## How to Run

1. **Install dependencies:**
   ```
   pip install streamlit
   ```

2. **Start the app:**
   ```
   streamlit run src/app.py
   ```

3. **Describe your game and click "Build & Run Game".**

## File Structure

- `src/app.py` — Main Streamlit app.
- `src/main.py` — Contains the `build_game` function (AI logic).


## Requirements

- Python 3.7+
- Streamlit

## Contributing

Feel free to open issues or submit pull requests!

## License

This project is licensed under the MIT License.
