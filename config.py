from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "21803165"))
API_HASH = getenv("API_HASH", "05e5e695feb30e25bef47484cc006da7")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "7403621976"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "Purvi_UPdates")
UPDATE_CHNL = getenv("UPDATE_CHNL", "PURVI_SUPPORT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ll_ALPHA_BABY_lll")

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
