# Извлечение из текста ключевых идей, создание заголовков и изображений

Эта программа предназначена для автоматического извлечения ключевых идей из предоставленного пользователем текста, генерации на его основе заголовка, а также создания изображения, соответствующего этому заголовку.

## Использование

1.  Запустите программу и следуйте инструкциям.
2.  Введите текст, из которого вы хотите извлечь ключевые идеи. Вводите каждую строку по отдельности и используйте 'END' на новой строке, чтобы завершить ввод.

Программа выполнит следующие действия:

1.  Извлечение ключевых точек из введенного текста.
2.  Генерация заголовка на основе извлеченных ключевых точек.
3.  Генерация изображения, соответствующего заголовку.

Результаты этих операций будут отображены на экране. Вы получите заголовок, список ключевых точек и URL изображения.

## Требования

Для работы с программой вам потребуется ключ API OpenAI. Вставьте его в файл `.env` под именем 'API_KEY'.

## Установка зависимостей

Установите необходимые зависимости, используя pip:


```pip install openai```

```pip install python-dotenv```

## Запуск программы

Запустите программу, используя Python 3:


```python main.py```

Используйте эту программу, чтобы автоматически генерировать ключевые точки, заголовки и изображения из введенного вами текста!
