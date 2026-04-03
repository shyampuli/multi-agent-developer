from utils.llm import get_llm_response


class ReviewAgent:
    def run(self, code: str) -> str:
        prompt = f"""
You are a senior Python code reviewer.

Given this code:
{code}

Your tasks:
- Improve code quality
- Fix bugs (if any)
- Improve readability
- Keep SAME functionality

IMPORTANT:
- Do NOT change the problem
- Do NOT generate unrelated code
- Only return the improved version of the SAME code

Return only Python code.
"""
        return get_llm_response(prompt)