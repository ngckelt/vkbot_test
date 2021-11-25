from datetime import datetime
from environs import Env
env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')

STORAGE_DIR = "bot/storage/storage"

LOG_FILE = f"logs/logs.log"

