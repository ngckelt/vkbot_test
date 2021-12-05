from environs import Env
env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')

STORAGE_DIR = "bot/storage/storage"

LOG_FILE = f"logs/logs.log"

WEEK_DAYS = ("пн", "вт", "ср", "чт", "пт", "сб")

SITE_URL = env.str("SITE_URL")

ADMIN_VK_ID = env.int("ADMIN_VK_ID")

