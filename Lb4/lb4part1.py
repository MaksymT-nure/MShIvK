import ollama
import markdown

def save_result(filename, model_name, task_type, content):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"--- Model: {model_name} | Task: {task_type} ---\n")
        f.write(content + "\n\n" + "="*30 + "\n\n")

models = ['qwen3:8b', 'gemma3:latest','ministral-3:8b']
chat_question = "Объясни научным языком в академическом стиле, до 500 слов, что такое Гало, почему возникает и в каких условиях его вероятнее всего увидеть?"
gen_prompt = "Придумай короткий хоррор рассказ, который который строится на временных петлях"

html_data = []
open('results_chat.txt', 'w').close()
open('results_generate.txt', 'w').close()

for model in models:
    print(f"Using {model} for now...")

    # Chat test
    response = ollama.chat(model=model, messages=[{'role': 'user', 'content': chat_question},])
    res_text = response['message']['content']
    save_result('results_chat.txt', model, 'Chat', res_text)
    html_data.append({'model': model, 'task': 'Generate', 'content': res_text})

    # Generate test
    gen_response = ollama.generate(model=model, prompt=gen_prompt)
    gen_text = gen_response['response']
    save_result('results_generate.txt', model, 'Generate', gen_text)
    html_data.append({'model': model, 'task': 'Generate', 'content': gen_text})

html_template = """
<html>
<head>
<meta charset="UTF-8">
<style>
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 40px auto; background-color: #f0f2f5; }
    .card { background: white; padding: 25px; margin-bottom: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-left: 6px solid #007bff; }
    .model-header { font-weight: bold; color: #007bff; font-size: 1.2em; border-bottom: 1px solid #eee; margin-bottom: 10px; }
    .task-badge { background: #e7f3ff; color: #007bff; padding: 2px 8px; border-radius: 4px; font-size: 0.8em; text-transform: uppercase; }
    pre { background: #f8f9fa; padding: 10px; border-radius: 5px; overflow-x: auto; }
</style>
</head>
<body>
    <h1 style="text-align:center;">Отчет работы моделей Ollama</h1>
"""

for item in html_data:
    formatted_content = markdown.markdown(item['content'])
    html_template += f"""
    <div class="card">
        <div class="model-header">{item['model']} <span class="task-badge">{item['task']}</span></div>
        <div class="result-text">{formatted_content}</div>
    </div>
    """

html_template += "</body></html>"

with open('report.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Files are saves as results_chat.txt & results_generate.txt & report.html ")