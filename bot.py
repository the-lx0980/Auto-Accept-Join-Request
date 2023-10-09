import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

app=Client(
    "Auto-Accept-Join-Request-Bot",
    bot_token = "6285956621:AAHF-zSJa3D_1JjUnF7ODx2H0Ih9JbjYj8g",
    api_id = 6353248,
    api_hash = "1346f958b9d917f0961f3e935329eeee"
)

CHAT_ID=-1001300164856
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@app.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button=[[
      InlineKeyboardButton("𝚄𝙿𝙳𝙰𝚃𝙴𝚉", url="https://t.me/lx0980AI")
      ]]
    await message.reply_text(text="**Hello...⚡\n\n I'M SIMPLE TELEGRAM AUTO REQUEST ACCEPT BOT**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@app.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: app, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))       

print("Bot Started ✨")
app.run()
