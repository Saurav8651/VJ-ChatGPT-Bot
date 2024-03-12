import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "26387767"))
API_HASH = environ.get("API_HASH", "d02f58640448a5ec63b63a679c1643d1")
BOT_TOKEN = environ.get("BOT_TOKEN", "6993860625:AAEgyN-JHD-y3lHcXJnPzOTav2yjX8c1-Yk")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002132856354"))
ADMINS = int(environ.get("ADMINS", "6215438910"))
DB_URI = environ.get("DB_URI", "mongodb+srv://hackerboymzf:3-Sb9-.CL5jbS4j@cluster0.0pvztkd.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
