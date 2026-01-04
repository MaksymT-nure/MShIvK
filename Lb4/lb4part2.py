import ollama

with open('article.txt', 'r', encoding='utf-8') as f:
    text_content = f.read()

model = 'gemma3:27b'

prompt = f"""
Прочитай текст і коротко розкажи, про що в ньому йдеться, 2 речення ":

Текст:
{text_content}
"""

response = ollama.chat(model=model, messages=[
    {'role': 'user', 'content': prompt}
])

result = response['message']['content']
with open('results_summary3.txt', 'w', encoding='utf-8') as f:
    f.write(f"--- Summary by {model} ---\n")
    f.write(result)
