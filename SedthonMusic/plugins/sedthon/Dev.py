import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from SedthonMusic import app, Telegram
import random
@app.on_message(
    command(["جزار","سورس","سورس الجزار", "الجزار"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/08fd322ff781e6eaceb77.jpg",
        caption=f"""
 [𝙎𝙊𝙐𝙍𝘾𝞝★𝞝𝙇𝙂𝘼𝙕𝘼𝙍](https://t.me/A_M_030)
 —————————————
 [اެݪ تِــاެࢪيٰــخَ ¦ ELGAZAR](https://t.me/A_M_0_3)
 
 [𓏺𝙂𝙍𝙊𝙐𝙋 𝙃𝞝𝙇𝙋](https://t.me/jvjv785)
  
 [⍟𓏺𝙒𝞝𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙎𝙊𝙐𝙍𝘾𝞝★𝞝𝙇𝙂𝘼𝙕𝘼𝙍](https://t.me/A_M_030)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اެݪ تِــاެࢪيٰــخَ ¦ ELGAZAR", url=f"https://t.me/A_M_0_3"), 
                ],[
                    InlineKeyboardButton(
                        "𝙎𝙊𝙐𝙍𝘾𝞝★𝞝𝙇𝙂𝘼𝙕𝘼𝙍", url=f"https://t.me/A_M_030"),
                ],

            ]

        ),

    )

@app.on_message(command([f"غنيلي", "غني", "غ", "{BOT_USERNAME} غنيلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/iV_P_Nl/{rl}"
    await client.send_voice(message.chat.id,url,caption="`🔥 ¦ تـم اختيـار الاغـنـية لـك`",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(command(["صورة","صور"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/lli1w/{rs}"
    await client.send_photo(message.chat.id,url,caption="`💕 ¦ تـم اختيـار الصوره لـك`",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

                        
