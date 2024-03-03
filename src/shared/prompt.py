import re
from pathlib import Path


def read_prompt(file_name: str):
    try:
        file_path = Path("src/prompts") / f"{file_name}.txt"
        prompt_content = file_path.read_text()
        return prompt_content
    except Exception as e:
        print(e)
        return None


def normalize_prompt_input(input: str) -> str:
    return re.sub(r"[^\w\s\'\"]", "", input.lower())
