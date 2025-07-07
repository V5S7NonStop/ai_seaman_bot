# AI Seaman Bot

Телеграм-бот для моряков. Поддерживает мотивацию, советы, викторины и обучение по типам судов.

## Как запустить

1. Склонируй репозиторий или загрузи архив
2. Установи зависимости:

```bash
pip install -r requirements.txt
```

3. Создай файл `.env` и вставь свой Telegram токен:

```
BOT_TOKEN=твой_токен
```

4. Запусти бота:

```bash
python main.py
```

## Для Render

- Добавь переменную окружения `BOT_TOKEN` в настройках
- Build command: `pip install -r requirements.txt`
- Start command: `python main.py`