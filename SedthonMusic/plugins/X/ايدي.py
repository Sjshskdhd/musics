import asyncio
import pyrogram
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from SedthonMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from config import LOG, LOG_GROUP_ID
from SedthonMusic import app
from SedthonMusic.utils.database import is_on_off
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from SedthonMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME
from SedthonMusic.misc import SUDOERS
import re
import sys
import os
import random
from time import time
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters




load_dotenv()




def get_file_id(msg: Message):

    if msg.media:

        for message_type in (

            "photo",

            "animation",

            "audio",

            "document",

            "video",

            "video_note",

            "voice",

            # "contact",

            # "dice",

            # "poll",

            # "location",

            # "venue",

            "sticker",

        ):

            obj = getattr(msg, message_type)

            if obj:

                setattr(obj, "message_type", message_type)

                return obj







#@app.on_message(command([""]) & filters.group &
#async def khalid(client: Client, message: Message):
    #usr = await client.get_users(message.from_user.id)
    #name = usr.first_name
    #async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    #await message.reply_photo(photo.file_id,       caption=f"""ᴜsᴇʀ -› {message.from_user.mention}\n𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲 -› @{message.from_user.username}\nɪᴅ -› {message.from_user.id}\nbio » {bio}""", 
        #reply_markup=InlineKeyboardMarkup(

            #[

                #[

                    #InlineKeyboardButton(

                        #name, url=f"https://t.me/{message.from_user.id}")

                #],

            #]

        #),

    #)



    )

@app.on_message(filters.command("ايدي الجروب", ["", "."]) & filters.group & SUDOERS)
async def mira(client: Client, message: Message):
    m_reply = await message.reply_text(f"ID chat** [`{message.chat.id}`]")
    await m_reply_text("")


#السورس - المطور


@app.on_message(filters.regex("^السورس$") & filters.group)
async def sourc(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/08fd322ff781e6eaceb77.jpg",
        caption=f"""✧ ᭙ᥱᥣᥴ᥆ꪔᥱ ƚ᥆ ᥉᥆ᥙᖇᥴᥱ ᥱᥣgᥲᤁᥲᖇ . ♪\n\n• ძᥱ᥎ᥱᥣ᥆ρᥱᖇ -› @A_M_0_3\n• ᥴɦᥲꪀᥱᥣ  𝙎𝙊𝙐𝙍𝘾𝞝★𝞝𝙇𝙂𝘼𝙕𝘼𝙍 . -› @A_M_030\n\n**- للتنصيب او للاستفسار تواصل مع مطور السورس**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "مطور السورس", user_id=5492061372)
                ],[
                    InlineKeyboardButton(
                       "تحديثات البوت", url=f"https://t.me/A_M_030")
                
                 ],

            ]

        ),

    )


@app.on_message(filters.regex("^المطور$") & filters.group & SUDOERS)
async def aboutd5ev(client: Client, message: Message):
    usr = await client.get_chat(5492061372)
    name = usr.first_name
    bio = (await client.get_chat(5492061372)).bio
    async for photo in client.iter_profile_photos(5492061372, limit=1):
                    await message.reply_photo(photo.file_id, caption=f"""- ძᥱ᥎ᥱᥣ᥆ρᥱᖇ ƚ᥆ ᥉᥆ᥙᖇᥴᥱ ᥱᥣgᥲᤁᥲᖇ . . ♪ -› @A_M_0_3\n\n- ძᥱ᥎ᥱᥣ᥆ρᥱᖇ ხᎥ᥆ -› {bio}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, user_id=5492061372)
                ],
            ]
        ),
    )
