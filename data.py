from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("sᴜᴩᴩᴏʀᴛ", url="https://t.me/damprivateroom"),
         InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴩᴇʀ", url="https://t.me/xflsdam"),
        ],
    ]

    START = """
Hᴇʏ {},

Tʜɪs ɪs {},
Aɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇᴅ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ!

Mᴀᴅᴇ ᴡɪᴛʜ 👑 ʙʏ: [ᴅᴀϻ•](https://t.me/xflsdam)
—
ɢʀᴏᴜᴘ ꜱᴜᴘᴘᴏʀᴛ: [ᴢᴇᴛsᴜ sᴜᴘᴘᴏʀᴛ](https://t.me/damprivateroom)
    """
