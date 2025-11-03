import json
import os


def get_user_list(config, key):
    with open("{}/Emilia/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    API_HASH = "0abc83883262245c90ca337b7a0375c4" # API_HASH from my.telegram.org
    API_ID = 29245477 # API_ID from my.telegram.org

    BOT_ID = 8015912062 # BOT_ID
    BOT_USERNAME = "OsaragiXRobot" # BOT_USERNAME

    MONGO_DB_URL = "" # MongoDB URL from MongoDB Atlas

    SUPPORT_CHAT = "EternalsHelplineBot" # Support Chat Username
    UPDATE_CHANNEL = "AnimeNexusNetwork" # Update Channel Username
    START_PIC = "https://i.ibb.co/DgpFbXsW/tmpfgm5zme3.jpg" # Start Image
    DEV_USERS = [7654385403,7852686677] # Dev Users
    TOKEN = "" # Bot Token from @BotFather
    CLONE_LIMIT = 0 # Number of clones your bot can make

    EVENT_LOGS = -1002456565415 # Event Logs Chat ID
    OWNER_ID = 7654385403 # Owner ID
 
    TEMP_DOWNLOAD_DIRECTORY = "./" # Temporary Download Directory
    BOT_NAME = "Osaragi" # Bot Name
    WALL_API = "6950f53" # Wall API from wall.alphacoders.com
    ORIGINAL_EVENT_LOOP = True # Do not Change


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
