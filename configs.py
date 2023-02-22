# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "29513127"))
    API_HASH = os.environ.get("API_HASH", "bd4ec4de9bb7c3b018ce18a4957e1739")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6255453309:AAG5FVR_pv9km8P40FbVVf1PTn3LtMEMEvk")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQA4Qm_DfGisrKHBnPG3os-4ZqhSejkQ5NdlUmlzCoKSE4VBkdiufTn_3T1CGHt-qfV3XWCB0C1UvRWeCkrmBQAzlQoaBMyfBXNP0zvYCTpXrLzR9gZyMTCRypvanEiP9a4nGYv1IUJTnR8mC4lSNYRT-4Hz9desFHxtkmkb4bkQFVEZFkKcYN2DKQJ4M0yXX-N2QRORDEs-tvtL5bUJQGMqHVnfdu-u3c6bVS1faQAMtW_Rhm3LWnykngNHnTZLcGh2RyYNNH9s0wcXq0pVt6mFjb9yju0J7KtRj1JdR2lUeJ4RSdoX4_Ab150_Eht-FLb_mR_rmiLAkOnaOl-AisAAAAAVyYLBYA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001836945914"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Mdisk_Movies_Searcher2_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER","5848443926"))
    DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://Sohanrazz:Sohanrazz@cluster0.bjr2jrh.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/LazyUrlHunterrBOT'>Lazy Url Hunterr</a> is an open source project.

    Devs: 
        <a href='https://t.me/mRiderDM'>❤️ LazyDeveloper ❤️</a>
    
    
🤖 My Name: <a href='https://t.me/Official_Movies_Group'>Mdisk Search Robot</a>

📝 Language: <a href='https://www.python.org'>Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'>Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

📡 Server 2: <a href='https://heroku.com'>koyeb</a> <i>comming soon</i>

👨‍💻 Developer Channel: <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a></b>
"""

    ABOUT_HELP_TEXT = """<b>💋 Developer : <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL finder BOT. Add me to any Group and Give me Hunting rights !!

I will be only yours if you will restrict adding me to other groups.
Go to @BotFather to change settings.

Don't be sad ! Your all urls are in safe Hand.

»»» <b>Happy Hunting</b> «««

🔺Thank You <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>🔺 </b>
"""


    START_MSG = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL & post finder BOT. Add me to any Group and Give me Hunting rights !!

Don't be sad ! Your all urls are in safe Hand.</b>

   »»»» <b>Happy Hunting</b> ««««

💸<b>Donate us to Keep service Alive.💸</b>
»» A small amount of ₹5 - ₹20 - ₹50 - ₹100 will be great help !
🔺 Thank You 🔺 
"""

