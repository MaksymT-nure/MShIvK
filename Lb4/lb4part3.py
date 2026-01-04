import ollama

image_path = 'photo.jpg'
models = ['ministral-3:8b','gemma3:27b']

open('results_vision2.txt', 'w').close()

for model in models:
    print(f"The model {model} is analyzing the picture...")

    try:
        response = ollama.chat(
            model=model,
            messages=[{
                'role': 'user',
                'content': 'Опиши подробно, что ты видишь на этом изображении?',
                'images': [image_path]
            }]
        )

        desc = response['message']['content']

        with open('results_vision.txt', 'a', encoding='utf-8') as f:
            f.write(f"--- Model: {model} ---\n")
            f.write(desc + "\n\n")

    except Exception as e:
        print(f"Error {model}: {e}")