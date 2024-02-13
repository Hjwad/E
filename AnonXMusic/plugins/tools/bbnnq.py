# telegram: @bbnnQ ~ My channel: @ccooR حقوق.
import os
import random
import asyncio
from pyrogram import Client,filters
from strings.filters import command
from pyrogram.types import (Message,
InlineKeyboardMarkup,InlineKeyboardButton)
from typing import Union
from AnonXMusic import app
@app.on_message(
  command(["المطور"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("lllby")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"≭︰Information Devloper ↯.\n\n━─━─────━─────━─━\n\n≭︰Name ↬ ❲{name}❳\n≭︰Bio ↬{usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
@app.on_message(command(["تفعيل الحماية"]))
async def ahmad(client: Client, message: Message):
    await message.reply_text(f"‹ تم تفعيل الحماية المطورة لمجموعتك 🦾",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝐃ᴇᴠᴇʟᴏᴘᴇʀ", user_id=117913435),
                InlineKeyboardButton("𝐒ᴏụʀᴄᴇ", url="t.me/mmmsc"),
            ],
            ]
        ),
    )
