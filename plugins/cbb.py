#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

HELP_TXT = f"""➤ 𝐇𝐞𝐥𝐩: 𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝕭𝕺𝕿../

𝙱𝚈 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚂𝚃𝙾𝚁𝙴 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝙼𝚈 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 𝙰𝙽𝙳 𝙸 𝚆𝙸𝙻𝙻 𝙶𝙸𝚅𝙴 𝚈𝙾𝚄 𝙰 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝙻𝙸𝙽𝙺  𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝚃𝙷𝙴 𝚂𝙰𝚅𝙴𝙳 𝙵𝙸𝙻𝙴𝚂.𝙸𝙵 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙵𝙸𝙻𝙴𝚂 𝙵𝚁𝙾𝙼 𝙰 𝙿𝚄𝙱𝙻𝙸𝙲 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝙵𝙸𝙻𝚆 𝙻𝙸𝙽𝙺 𝙾𝙽𝙻𝚈  𝙾𝚁 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙵𝙸𝙻𝙴𝚂 𝙵𝚁𝙾𝙼 𝙰  𝙿𝚁𝙸𝚅𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽 𝙾𝙽 𝚃𝙷𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝙵𝙸𝙻𝙴𝚂...//

⪼ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞 ›

➪ /genlink ›› 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽𝚈 𝙼𝙴𝙳𝙸𝙰 𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝙽𝙺.

➪ /batch ›› 𝚃𝙾 𝙲𝚁𝙴𝙰𝚃𝙴 𝙻𝙸𝙽𝙺 𝙵𝙾𝚁 𝙼𝚄𝙻𝚃𝙸𝙿𝙻𝙴 𝙵𝙸𝙻𝙴𝚂.

➪ /users ›› view bot statistics

➪ /broadcast ›› broadcast any messages to bot users

➪ /stats ›› checking your bot uptime

⪼ 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 ›

/batch https://t.me/KR_Picture

𝙲𝚁𝙴𝙳𝙸𝚃𝚂 ›› ᴍᴜʜᴀᴍᴍᴀᴅ ᴢɪɴᴀɴ"""

ABOUT_TXT = f"""✮ 𝙼𝚈 𝙽𝙰𝙼𝙴"""

START_TXT = f"""Friends.......🖤 We have already lost many channels due to copyright... So join us by giving your support, cooperation and blessings to this new channel of ours 🙏🙏"""

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

                    ],[

                    InlineKeyboardButton('ʜᴇʟᴩ', callback_data='help'),

                    InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about')

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
