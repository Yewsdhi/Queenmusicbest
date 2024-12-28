from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SACHIN_MUSIC import app
from config import BOT_USERNAME
from SACHIN_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - [⋏ Ł ꪮ ⲛ 𝛆](https://t.me/AlonehuVai)
│├ ғᴜʟʟ ɪɴғᴏ - [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/AloneXAbout/3)
│├─────────────────╯
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ [ᴍʀ ᴀʟᴏɴᴇ]((https://t.me/AlonehuVai)
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton(" 𝗔𝗟𝗢𝗡𝗘 𝗖𝗢𝗗𝗘𝗥 ", url=f"https://t.me/AlonehuVai")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/AlonehuVai"),
          InlineKeyboardButton("𝗥𝗘𝗣𝗢", url="https://t.me/AlonehuVai"),
          ],
               [
                InlineKeyboardButton(" 𝗔𝗟𝗢𝗡𝗘 𝗡𝗘𝗧𝗪𝗢𝗥𝗞 ", url=f"https://t.me/AloneXBots"),
],
[
InlineKeyboardButton("𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 𝗕𝗢𝗧", url=f"https://t.me/AloneXMusicBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/hxvx8c.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
