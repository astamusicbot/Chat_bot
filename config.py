from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "21678249"))
API_HASH = getenv("API_HASH", "223f921be65b67bee7d78070767f6be9")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "7464690589"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "oldskoolgc")
UPDATE_CHNL = getenv("UPDATE_CHNL", "ixasta1")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ixasta")

# Random Start Images
IMG = [
    "https://files.catbox.moe/1fxeku.jpg",
    "https://files.catbox.moe/2830tj.jpg",
    "https://files.catbox.moe/nmqde0.jpg",
    "https://files.catbox.moe/pzjwvx.jpg",

]


# Random Stickers
STICKER = [
    "CAACAgEAAxkBAAIJomRdLhVJVebkx0JRsp1STwTv3t3eAAJrAgAClpxhRD4z4bgqlIF0LwQ",
    "CAACAgUAAxkBAAIJo2RdLhjLjCpmPipMT8ksrqwUjGAIAAK1BQACLZ8oVFVNmhalU8eOLwQ",
    "CAACAgUAAxkBAAIJpGRdLkpU7t2WDj9zUFgCJ5uHUdGHAALTBAAC59CYV3t9x-f0tt4OLwQ",
]


EMOJIOS = [
    "🎲",
    "🔥",
    "⚡️",
    "⛈",
    "🌩",
    "🌦",
    "☀️",
    "💫",
    "🐳",
    "🦑",
]
