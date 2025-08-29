# (©) Codexbotz

import sys
from datetime import datetime

from aiohttp import web
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode

from plugins import web_server
from config import (
    API_HASH,
    APP_ID,
    LOGGER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
    FORCE_SUB_CHANNEL,
    CHANNEL_ID,
    PORT,
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            bot_token=TG_BOT_TOKEN,
            workers=TG_BOT_WORKERS,
            plugins={"root": "plugins"},
            parse_mode=ParseMode.HTML,  # ✅ modern way
        )
        self.LOGGER = LOGGER
        self.uptime: datetime | None = None
        self.username: str | None = None
        self.invitelink: str | None = None
        self.db_channel = None

    async def start(self):
        """Start the bot and perform setup checks."""
        await super().start()
        usr_bot_me = await self.get_me()
        self.username = usr_bot_me.username
        self.uptime = datetime.now()

        log = self.LOGGER(__name__)

        # ✅ Force-sub channel check
        if FORCE_SUB_CHANNEL:
            try:
                chat = await self.get_chat(FORCE_SUB_CHANNEL)
                self.invitelink = (
                    chat.invite_link
                    or await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                )
            except Exception as e:
                log.warning(e)
                log.error(
                    "Bot cannot export invite link from Force Sub Channel!\n"
                    f"Check FORCE_SUB_CHANNEL={FORCE_SUB_CHANNEL} "
                    "and ensure bot is admin with 'Invite Users via Link' permission."
                )
                await self.stop()
                return

        # ✅ DB channel check
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(db_channel.id, "✅ Bot is active!")
            await test.delete()
        except Exception as e:
            log.warning(e)
            log.error(
                "Bot is not admin in DB Channel!\n"
                f"Check CHANNEL_ID={CHANNEL_ID} and ensure proper permissions."
            )
            await self.stop()
            return

        # ✅ Logging banner
        log.info("🚀 Bot Running..! Created by https://t.me/CodeXBotz")
        log.info(
            """
░█████╗░░█████╗░██████╗░███████╗██╗░░██╗██████╗░░█████╗░████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝╚════██║
██║░░╚═╝██║░░██║██║░░██║█████╗░░░╚███╔╝░██████╦╝██║░░██║░░░██║░░░░░███╔═╝
██║░░██╗██║░░██║██║░░██║██╔══╝░░░██╔██╗░██╔══██╗██║░░██║░░░██║░░░██╔══╝░░
╚█████╔╝╚█████╔╝██████╔╝███████╗██╔╝╚██╗██████╦╝╚█████╔╝░░░██║░░░███████╗
░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚══════╝
            """
        )

        # ✅ Proper aiohttp web server startup
        app = await web_server()  # must return web.Application
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, host="0.0.0.0", port=PORT)
        await site.start()
        log.info(f"🌐 Web server started on http://0.0.0.0:{PORT}")

    async def stop(self, *args):
        """Stop the bot cleanly."""
        await super().stop()
        self.LOGGER(__name__).info("🛑 Bot stopped.")
