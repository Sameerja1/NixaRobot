import asyncio
import random
from time import time
from datetime import datetime
from Nixa.plugins.commands import command
from Nixa.plugins.commands import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# bot ka username yha pel do kon baar baar config se uthayega
BOT_USERNAME = "NixaRobot"



NIXA_IMG = (
"https://te.legra.ph/file/fa6c391baeca4594e7ca5.jpg",
"https://te.legra.ph/file/b3079e6041c32f91aa8cc.jpg",
"https://te.legra.ph/file/87a36639d2dac42da7ec2.jpg",
"https://te.legra.ph/file/640f00d7f0fea2640dcee.jpg",
"https://te.legra.ph/file/af4e385ad2d039fc7fb55.jpg",
"https://te.legra.ph/file/d48e10f96c47b9234447d.jpg",
"https://te.legra.ph/file/91163718437d62b6a9b05.jpg",
"https://te.legra.ph/file/617d689c8a1e4d7f03512.jpg",
"https://te.legra.ph/file/dacd6bed230ebe1802eb2.jpg",
"https://te.legra.ph/file/e1ea346c66e98ee8e773c.jpg",
"https://te.legra.ph/file/4cce92e16ea6dc3b68989.jpg",
"https://te.legra.ph/file/bf62629bfa33eed1fe39d.jpg",
"https://te.legra.ph/file/1f36469d073c63fe6603c.jpg",
"https://te.legra.ph/file/e1fe736cb651f507c8b38.jpg",
)

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        random.choice(NIXA_IMG),
        caption="""ʜᴇʟʟᴏ sɪʀ ɪ ᴀᴍ ɴɪxᴀ ʀᴏʙᴏᴛ\n
ᴛʜɪs ɪs sɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴜsᴇᴅ ғᴏʀ ғᴜɴ""",
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("👥 sᴜᴘᴘᴏʀᴛ", url="https://t.me/TheSupportBots"),
            InlineKeyboardButton("📣 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/TechQuard")
        ],
        
   
     ]
  ),
)
    
#vai support change krdiya hai new wale me join ho jaao
    
@Client.on_message(commandpro(["/start", "/alive", "/repo"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        random.choice(NIXA_IMG),
         caption="""ʜᴇʟʟᴏ sɪʀ ɪ ᴀᴍ ɴɪxᴀ ʀᴏʙᴏᴛ\n
ᴛʜɪs ɪs sɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴜsᴇᴅ ғᴏʀ ғᴜɴ""",        
    reply_markup=InlineKeyboardMarkup(
             [
            [
                InlineKeyboardButton(text="👥 ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/TheSupportbots"),
                InlineKeyboardButton(text="📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/TechQuard"),
            ]
        ]
     ),
  ) 

@Client.on_message(command(["ping"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢ..... 👀")
    delta_ping = time() - start
    await message.reply_photo(
        random.choice(NIXA_IMG),
        caption=f"ᴘ ᴏ ɴ ɢ ! \n" f"`{delta_ping * 1000:.3f} ᴍs`")
