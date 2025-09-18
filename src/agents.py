from textwrap import dedent
from crewai import Agent
from model import GEMINI_LLM

class GameAgents:
    def senior_engineer_agent(self):
        return Agent(
            role="Senior Software Engineer",
            goal="Create software as needed",
            backstory=dedent(
                """\
                You are a Senior Software Engineer at a leading tech think tank.
                Your expertise in Python allows you to produce perfect, clean, and efficient code.
                """
            ),
            llm=GEMINI_LLM,
            allow_delegation=False,
            verbose=True,
        )

    def qa_engineer_agent(self):
        return Agent(
            role="Software Quality Control Engineer",
            goal="Create perfect code by analyzing the code that is given for errors",
            backstory=dedent(
                """\
                You specialize in checking code for errors. You fix missing imports, variable declarations,
                mismatched brackets, syntax errors, logic errors, and security vulnerabilities.
                """
            ),
            llm=GEMINI_LLM,
            allow_delegation=False,
            verbose=True,
        )

    def chief_qa_engineer_agent(self):
        return Agent(
            role="Chief Software Quality Control Engineer",
            goal="Ensure that the code does the job it is supposed to do",
            backstory=dedent(
                """\
                You ensure programmers deliver high-quality, reliable code. You verify correctness and completeness.
                """
            ),
            llm=GEMINI_LLM,
            allow_delegation=True,
            verbose=True,
        )
