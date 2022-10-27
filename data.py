from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ꜱᴛᴀᴛʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("sᴜᴩᴩᴏʀᴛ", url="https://t.me/kazusupportgrp"),
         InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴩᴇʀ", url="https://t.me/disinikazu"),
        ],
    ]

    START = """
**Hey** {},

**This is** {},
**Bot untuk Mengambil String Session!**

**Made With 👑 By:** [ᴋᴀᴢᴜ](https://t.me/disinikazu)
—
**Group Support:** [ᴋᴀᴢᴜ sᴜᴘᴘᴏʀᴛ](https://t.me/kazusupportgrp)
    """
