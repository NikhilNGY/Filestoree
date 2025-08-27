#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

HELP_TXT = f"""Any Issues Movie Files Contact Owner

🧑🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/Nikhil5757h>Owner</a>"""

ABOUT_TXT = f"""Any Issues Movie Files Contact Owner

🧑🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/Nikhil5757h>Owner</a>"""

START_TXT = f"""Friends.......🖤 
We have already lost many channels due to copyright... So join us by giving your support, cooperation and blessings to this new channel of ours 🙏🙏"""

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if query.data == "help":
        buttons = [[
            InlineKeyboardButton('𝙱𝙰𝙲𝙺', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=HELP_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    if query.data == "about":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)

        await query.message.edit_text(
            text=ABOUT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    if query.data == "start":
        reply_markup = InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton('ᴜᴩᴅᴀᴛꜱ', url='https://t.me/KR_Picture'),

                    InlineKeyboardButton('ɢʀᴏᴜᴩ', url='https://t.me/+x6OfRDdUPrUwZTZl')
                
                ]

            ]

        )

        await query.message.edit_text(
            text=START_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
            )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
