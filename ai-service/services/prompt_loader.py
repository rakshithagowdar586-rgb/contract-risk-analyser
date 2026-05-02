def load_prompt(file_path, text):
    with open(file_path, "r", encoding="utf-8") as f:
        prompt = f.read()

    return prompt.replace("{text}", text)