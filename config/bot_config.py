import os
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from pathlib import Path
from aiogram.fsm.storage.memory import MemoryStorage

# === Автозагрузка .env ТОЛЬКО ЛОКАЛЬНО ===
if Path("config/.env").exists():
    try:
        from dotenv import load_dotenv
        load_dotenv("config/.env")
    except ImportError:
        pass  # python-dotenv не установлен — ок
# =========================================

API_TOKEN = os.getenv("TOKEN")

if not API_TOKEN:
    raise RuntimeError("TOKEN is not set! Set it in environment or config/.env (locally)")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

'''
config = dotenv_values("./config/.env")
API_TOKEN = config['TOKEN']
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
'''