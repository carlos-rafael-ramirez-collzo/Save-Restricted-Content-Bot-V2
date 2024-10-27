# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29860993"))
API_HASH = getenv("API_HASH", "b0e23e8daeac124e838dcb6f07eb4a2b")
BOT_TOKEN = getenv("BOT_TOKEN", "7720686444:AAFIqRd2E0nL8wgm8qeuyBXSGFLa85ZbhHU")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
