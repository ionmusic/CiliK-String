from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ꜱᴛᴀᴛʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("sᴜᴩᴩᴏʀᴛ", url="https://t.me/CilikSupport"),
         InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴩᴇʀ", url="https://t.me/greyyvbss"),
        ],
    ]

    START = """
**Hey** {},

**This is** {},
**Bot untuk Mengambil String Session!**

**Made With 👑 By:** [ɢʀᴇʏ](https://t.me/greyyvbss)
—
**Group Support:** [ᴄɪʟɪᴋ ꜱᴜᴘᴘᴏʀᴛ](https://t.me/CilikSupport)
    """
