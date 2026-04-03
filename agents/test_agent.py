from utils.llm import get_llm_response


class TestAgent:
    def run(self, code: str) -> str:
        prompt = f"""
You are a QA engineer.

Given this Python code:
{code}

Generate:
- Unit tests using unittest or pytest
- Include edge cases
- Ensure coverage

Return only test code.
"""
        return get_llm_response(prompt)