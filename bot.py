import sys
from pyrogram import Client
from pyrogram.enums import ParseMode
from config import API_HASH, APP_ID, LOGGER, BOT_TOKEN

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=8,
            bot_token=BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/Lx0980AI")
        self.username = usr_bot_me.username
        
    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
