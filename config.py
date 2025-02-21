import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")

BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_USERNAME = getenv("OWNER_USERNAME","")
BOT_USERNAME = getenv("BOT_USERNAME" , "")
BOT_NAME = getenv("BOT_NAME" , "")
ASSUSERNAME = getenv("ASSUSERNAME" , "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", ))
OWNER_ID = int(getenv("OWNER_ID", ))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Yewsdhi/Queenmusicroyal",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
PRIVACY_LINK = getenv("PRIVACY_LINK", "")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ll_DPZ_WORLDS_ll")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/queenbotgrup")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "700"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
STRING1 = getenv("STRING_SESSION", "BQFpyqoAVPEZ0SdQVeVNyf048yzNzsj9nk1pfX7zwnpAuwqysBryyclsgTNXsT7bjkB95lTUg9OeGC74ZoXqy9y08qccAexEUQXmaOjDkzEtRVoKsv_HrU7T1pP92rKuJFADJLKmzTltRPodqQEbjSleIJXTJBUWoDK8pKS9SCrK1lnsTB3MI-Qk5yzx_YIeq5l1q0N7AnFKYIrbcm6MxcOEtrsjznpPaKHQH8jLyeQjLvudl7RIreQV0tzJSTf1zdRvAyQl3eQMpgwMv6SwxiduxVPprDorLrfaVRKW6ppN-WPUPI0rtwkUfwci6JGfYvjgy37vXmUM4zeTwI_ItFJ0iXk5jgAAAAG0Yy8hAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/s617ea.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/s617ea.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/s617ea.jpg"
STATS_IMG_URL = "https://files.catbox.moe/s617ea.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/s617ea.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/s617ea.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/s617ea.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/s617ea.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/s617ea.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/s617ea.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/s617ea.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/s617ea.jpg"
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
        
