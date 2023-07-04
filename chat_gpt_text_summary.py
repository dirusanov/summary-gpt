import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ['API_KEY']


def extract_key_points(input_text):
    messages = [
        {
            "role": "system",
            "content": "Ты - помощник по созданию ключевых идей. "
                       "Твоя задача - предоставить краткую ключевые мысли из текста, "
                       "Ключевые мысли должны быть представлены в виде списка с тире"
        },
        {
            "role": "user",
            "content": input_text,
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message['content']


def generate_title(key_points):
    messages = [
        {
            "role": "system",
            "content": "Ты - помощник по созданию заголовков. "
                       "Твоя задача - сгенерировать короткий и информативный заголовок на сонове переданного текста"
        },
        {
            "role": "user",
            "content": key_points,
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message['content']


def generate_image(prompt: str) -> str:
    new_prompt = f"{prompt}. Generate an image in either photorealistic or colored pencil style"
    image_resp = openai.Image.create(
        prompt=new_prompt,
        n=1,
        size="512x512"
    )
    image_url = image_resp['data'][0]['url']
    return image_url


def main():
    print("Введите текст (вводите 'END' в отдельной строке для завершения ввода):")
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    input_text = "\n".join(lines)

    print("Ожидайте...")
    print("================================================================")

    key_points = extract_key_points(input_text)
    title = generate_title(key_points)
    image_url = generate_image(title)

    print("Заголовок:")
    print(title)

    print("Ключевые пункты:")
    print(key_points)

    print("URL изображения:")
    print(image_url)


if __name__ == "__main__":
    main()
