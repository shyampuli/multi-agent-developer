import os
from typing import Optional, List, Dict
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


def get_llm_response(
    prompt: str,
    model: str = "nvidia/nemotron-3-nano-30b-a3b",
    temperature: float = 0.1,
    max_tokens: Optional[int] = 1024,
    system_prompt: str = "You are a helpful assistant."
) -> str:

    api_key = os.getenv("NVIDIA_API_KEY")

    if not api_key:
        return "Error: NVIDIA_API_KEY not found in .env file"

    client = OpenAI(
        api_key=api_key,
        base_url="https://integrate.api.nvidia.com/v1"
    )

    messages: List[Dict[str, str]] = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error calling NVIDIA LLM: {str(e)}"