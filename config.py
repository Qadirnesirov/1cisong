import os

class Config(object):
    DATABASE = os.environ.get("DB_URI", "mongodb+srv://nesirovq1997:qadir1997@cluster0.pavador.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6184936428").split())
    SUPPORT = os.environ.get("SUPPORT", "otobotsport")
