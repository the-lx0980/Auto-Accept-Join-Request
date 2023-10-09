import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

TEXT  = """
नमस्ते {} डीएफएफ अपडेट चैनल में आपका स्वागत है।

आपको यह संदेश इसलिए प्राप्त हुआ क्योंकि आपने 
DFF UPDATE ⚡ चैनल से जुड़ने का अनुरोध किया था।

आपका अनुरोध स्वीकार कर लिया गया है। ✅


Hello {} Welcome To DFF UPDATE Channel.

You received this message because you 
requested to join DFF UPDATE ⚡ Channel.

Your request has been accepted ✅
"""
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
    
