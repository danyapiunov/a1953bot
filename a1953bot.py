import config
import telethon
from telethon import TelegramClient, events
api_id = config.API_ID
api_hash = config.API_HASH
bot_token = config.BOT_TOKEN
client = TelegramClient('testbot', api_id, api_hash).start(bot_token=bot_token)
@client.on(events.NewMessage)
async def handler(event):
    await event.respond('Сталин сдох!')
client.run_until_disconnected()