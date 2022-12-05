# (c) @RoyalKrrishna

import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", 12345))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MdiskSearchRobot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", -100))
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    BOT_OWNER = int(os.getenv("BOT_OWNER"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = """
<b>Hey! {}😅,
I'm Doraemon Pocket.🤖</a>
I Can Search 🔍 What You Want❗
<a>Made With ❤ By @movies_halt</a></b>
"""
    START_PHOTO = os.getenv("START_PHOTO")
    HOME_TEXT = """
<b>Hey! {}😅,
I'm Doraemon Pocket.🤖</a>
I Can Search 🔍 What You Want❗
<a>Made With ❤ By @movies_halt</a></b>
"""
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", None)
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", ""))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 300))
    MDISK_API = os.getenv("MDISK_API", "12334")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "1"))
    ABOUT_BOT_TEXT = """<b>This is Movie Search Bot.
🤖 My Name: <a href='https://t.me/DoraemonPocket_bot'>Doraemon Pocket</a>
📝 Language : <a href='https://www.python.org'> Python V3</a>
📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>
📡 Server: <a href='https://heroku.com'>Heroku</a>
👨‍💻 Created By: <a href='https://t.me/aarthur_dayne'>Arthur Dayne</a></b>
"""
    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/aarthur_dayne'>Click Me</a>
If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""
