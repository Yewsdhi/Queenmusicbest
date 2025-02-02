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
│├ ᴛɢ ɴᴀᴍᴇ - [ sᴧʀᴋᴀʀ ꭙ sᴧʀᴋᴀʀɪ ](https://t.me/II_ROYALENTRY1128_II)
│├ ғᴜʟʟ ɪɴғᴏ - [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/II_ROYALENTRY1128_II)
│├─────────────────╯
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ [sᴧʀᴋᴀʀ ꭙ sᴧʀᴋᴀʀɪ]((https://t.me/II_ROYALENTRY1128_II)
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton(" 𝗔𝗟𝗢𝗡𝗘 𝗖𝗢𝗗𝗘𝗥 ", url=f"https://t.me/HARRYASHU")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/HARRYASHU"),
          InlineKeyboardButton("𝗥𝗘𝗣𝗢", url="https://t.me/HARRYASHU"),
          ],
               [
                InlineKeyboardButton(" 𝗔𝗟𝗢𝗡𝗘 𝗡𝗘𝗧𝗪𝗢𝗥𝗞 ", url=f"https://t.me/HARRYASHU"),
],
[
InlineKeyboardButton("𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 𝗕𝗢𝗧", url=f"https://t.me/HARRYASHU"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/hxvx8c.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
