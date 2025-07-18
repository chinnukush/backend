import json
from os import getenv, path
from dotenv import load_dotenv
from Backend import LOGGER


load_dotenv(path.join(path.dirname(path.dirname(__file__)), "config.env"))
class Telegram:
    API_ID = int(getenv("API_ID", "15671595"))
    API_HASH = getenv("API_HASH", "bb8f36f9c39a24c7f8b2acbc7ea8c60a")
    BOT_TOKEN = getenv("BOT_TOKEN", "7390174586:AAGlfMP3iN70hjpHAfB8YcUna5tDgpLXC4w")
    PORT = int(getenv("PORT", "8000"))
    BASE_URL = getenv("BASE_URL", "0.0.0.0").rstrip('/')
  # https://grim-robenia-koyebuser123-05b315bb.koyeb.ap
  
    AUTH_CHANNEL = [channel.strip() for channel in (getenv("AUTH_CHANNEL") or "-1002723124765").split(",") if channel.strip()]
    DATABASE = getenv("DATABASE", "mongodb+srv://fyviodemo:XKr72sW6QOzDAU8Y@cluster0.5y1fiek.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").split(", ")
    TMDB_API = getenv("TMDB_API", "")
    IMDB_API = getenv("IMDB_API", "imdb.kyt43843.workers.dev")
    UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/chinnukush/backend")
    UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
    MULTI_CLIENT = getenv("MULTI_CLIENT", "False").lower() == "true"
    USE_CAPTION = getenv("USE_CAPTION", "False").lower() == "true"
    USE_TMDB = getenv("USE_TMDB", "False").lower() == "true"
    OWNER_ID = int(getenv("OWNER_ID", "7253187871"))
    USE_DEFAULT_ID = getenv("USE_DEFAULT_ID", None)



# Startup Config
