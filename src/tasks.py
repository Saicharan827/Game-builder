from textwrap import dedent
from crewai import Task

class GameTasks:
    def code_task(self, agent, game):
        return Task(
            description=dedent(
                f"""
                You are a Senior Software Engineer tasked with creating a Python game.

                Instructions
                ------------
                {game}

                Requirements
                ------------
                - Write clean, efficient, and well-structured Python code.
                - Include all necessary imports.
                - Include a "Play Again" option if the game ends.
                - Output ONLY the full Python code, nothing else.
                """
            ),
            agent=agent,
            expected_output="Full working Python code for the game",
        )

    def review_task(self, agent, game):
        return Task(
            description=dedent(
                f"""
                You are a QA Engineer reviewing Python game code.

                Instructions
                ------------
                {game}

                Review Criteria
                ---------------
                - Fix syntax, logic, and runtime errors.
                - Ensure Play Again works correctly.
                - Ensure the game runs without crashing.
                - Output ONLY the corrected Python code.
                """
            ),
            agent=agent,
            expected_output="Reviewed and corrected Python game code",
        )

    def evaluate_task(self, agent, game):
        return Task(
            description=dedent(
                f"""
                You are the Chief QA Engineer ensuring the Python game is production-ready.

                Instructions
                ------------
                {game}

                Evaluation Criteria
                -------------------
                - Verify the code is complete and functional.
                - Ensure no missing parts (imports, variables, functions).
                - Confirm Play Again works correctly.
                - Output ONLY the final Python code.
                """
            ),
            agent=agent,
            expected_output="Final validated Python game code",
        )
