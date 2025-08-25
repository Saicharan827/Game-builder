from textwrap import dedent
from crewai import Task


class GameTasks:
    def code_task(self, agent, game):
        return Task(
            description=dedent(
                f"""You will create a game using Python. These are the instructions:

                Instructions
                ------------
                {game}

                Your final answer must be the full Python code, only the Python code and nothing else.
                """
            ),
            agent=agent,
            expected_output="Full Python code of the game",  # Add the expected_output field here
        )

    def review_task(self, agent, game):
        return Task(
            description=dedent(
                f"""\
                You are helping create a game using Python. These are the instructions:

                Instructions
                ------------
                {game}

                Using the code you received, check for errors. Check for logic errors,
                syntax errors, missing imports, variable declarations, mismatched brackets,
                and security vulnerabilities.

                Your final answer must be the full Python code, only the Python code and nothing else.
                """
            ),
            agent=agent,
            expected_output="Reviewed Python code with fixes",  # Add the expected_output field here
        )

    def evaluate_task(self, agent, game):
        return Task(
            description=dedent(
                f"""\
                You are helping create a game using Python. These are the instructions:

                Instructions
                ------------
                {game}

                You will look over the code to ensure that it is complete and
                does the job that it is supposed to do.

                Your final answer must be the full Python code, only the Python code and nothing else.
                """
            ),
            agent=agent,
            expected_output="Evaluated Python code",  # Add the expected_output field here
        )
