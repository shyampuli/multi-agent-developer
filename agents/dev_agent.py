from utils.llm import get_llm_response


class DevAgent:
    def run(self, task: str) -> str:
        prompt = f"""
You are a senior Python developer.

Task:
{task}

Requirements:
- Write clean, modular Python code
- Use functions
- Add comments
- Follow best practices

Return only code.
"""
        return get_llm_response(prompt)