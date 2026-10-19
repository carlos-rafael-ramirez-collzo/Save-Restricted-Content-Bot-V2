# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29860993"))
API_HASH = getenv("API_HASH", "b0e23e8daeac124e838dcb6f07eb4a2b")
BOT_TOKEN = getenv("BOT_TOKEN", "8350847393:AAEVTMgm9bnWM93Il8pzBubmsgZnwpTvSzA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7150137515").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://carlos:Mmcmqlt(17186)@cluster0.ukz2v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
