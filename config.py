from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","27383453"))
API_HASH = getenv("API_HASH","4c246fb0c649477cc2e79b6a178ddfaa")

BOT_TOKEN = getenv("BOT_TOKEN","6878567316:AAFNWjNAk7-KyJRsqD_1mKSpc3yF-T4B-a8")
OWNER_ID = int(getenv("OWNER_ID","6474527080"))

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://SHASHANK:STRANGER@shashank.uj7lold.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN","")
