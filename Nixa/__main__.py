import os
import logging
import pyrogram
from os import environ, getenv
from pyrogram import Client
import config 
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
OWNER_ID = int(getenv("OWNER_ID", 0))



if __name__ == "__main__" :
    print("Starting Bot...")
    
    app = pyrogram.Client(
        "Nixa",        
        config.API_ID,
        config.API_HASH,
        bot_token=BOT_TOKEN,
        plugins = dict(root="Nixa/plugins")
 
        )
                          
app.run()          
 
