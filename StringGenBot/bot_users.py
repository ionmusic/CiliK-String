from pyrogram.types import Message
from pyrogram import Client, filters

from env import OWNER_ID
from StringGenBot.db import SESSION
from StringGenBot.db.users_sql import Users, num_users


@Client.on_message(~filters.service, group=1)
async def users_sql(_, msg: Message):
    if msg.from_user:
        if q := SESSION.query(Users).get(int(msg.from_user.id)):
            SESSION.close()
        else:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()


@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = await num_users()
    await msg.reply(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ ᴢᴇᴛsᴜ sᴛʀɪɴɢ:\n\n {users} ᴜsᴇʀs", quote=True)
