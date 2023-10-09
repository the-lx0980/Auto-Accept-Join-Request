import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest
from bot import Bot
from db.database import add_user, del_user, full_userbase, present_user
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from config import ADMINS, CHAT_ID

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client: Client, message: Message):
    approvedbot = await client.get_me() 
    button=[[
      InlineKeyboardButton("UPDATES", url="https://t.me/lx0980AI")
      ]]
    await message.reply_text(text="**Hello...⚡\n\n I'M SIMPLE TELEGRAM AUTO REQUEST ACCEPT BOT**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@Client.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: Client, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    if not await present_user(user.id):
        try:
            await add_user(id)
        except:
            pass
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    buttons = [[
        InlineKeyboardButton('Support', url=f'https://t.me/{SUPPORT_CHAT}')
    ]]
    reply_markup=InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=user.id,
        text  = f"""
नमस्ते {user.name} डीएफएफ अपडेट चैनल में आपका स्वागत है।

आपको यह संदेश इसलिए प्राप्त हुआ क्योंकि आपने 
DFF UPDATE ⚡ चैनल से जुड़ने का अनुरोध किया था।

आपका अनुरोध स्वीकार कर लिया गया है। ✅


Hello {user.name} Welcome To DFF UPDATE Channel.

You received this message because you 
requested to join {chat.title} Channel.

Your request has been accepted ✅
""",
    )
    await client.send_message(
        chat_id = user.id,
        text = "चैनल लिंक\nChannel Link",
        reply_markup = reply_markup,
    )
    

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>Broadcast Completed</u>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked Users: <code>{blocked}</code>
Deleted Accounts: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply("""<code>Use this command as a replay to any telegram message with out any spaces.</code>""")
        await asyncio.sleep(8)
        await msg.delete()
