import os
import re
import sys
import types

# 🩹 Patch: Fake chromadb so CrewAI never loads real sqlite-backed Chroma
fake_chroma = types.ModuleType("chromadb")
fake_chroma.Client = lambda *a, **k: None
sys.modules["chromadb"] = fake_chroma

from crewai import Crew
from tasks import GameTasks
from agents import GameAgents


def build_game(game_description: str):
    """Creates agents, tasks, runs Crew, and returns final Python code string."""

    tasks = GameTasks()
    agents = GameAgents()

    senior_engineer = agents.senior_engineer_agent()
    qa_engineer = agents.qa_engineer_agent()
    chief_qa = agents.chief_qa_engineer_agent()

    code_task = tasks.code_task(senior_engineer, game_description)
    review_task = tasks.review_task(qa_engineer, game_description)
    evaluate_task = tasks.evaluate_task(chief_qa, game_description)

    crew = Crew(
        agents=[senior_engineer, qa_engineer, chief_qa],
        tasks=[code_task, review_task, evaluate_task],
        verbose=True,
        # 🚫 no DB, no Chroma
        knowledge=None,
        storage=None
    )

    final_game_code = crew.kickoff()
    code_str = str(getattr(final_game_code, "output", final_game_code))

    # Extract Python code if wrapped in ```python ... ```
    match = re.search(r"```python(.*?)```", code_str, re.DOTALL)
    extracted_code = match.group(1).strip() if match else code_str.strip()

    # Save generated game
    with open("generated_game.py", "w", encoding="utf-8") as f:
        f.write(extracted_code)

    return extracted_code
