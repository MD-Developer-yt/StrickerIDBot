# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from database import add_sticker
from buttons import copy_buttons

waiting_users = set()

def ask_sticker(_, msg):
    waiting_users.add(msg.from_user.id)
    msg.reply_text("𝖭𝗈𝗐 𝖲𝖾𝗇𝖽 𝖠 𝖲𝗍𝗋𝗂𝖼𝗄𝖾𝗋")

def handle_sticker(_, msg):
    uid = msg.from_user.id

    if uid not in waiting_users:
        return

    file_id = msg.sticker.file_id
    unique_id = msg.sticker.file_unique_id

    add_sticker(uid, file_id, unique_id)

    msg.reply_text(
        f"""
🎯 𝗬𝗼𝘂𝗿 𝗦𝘁𝗶𝗰𝗸𝗲𝗿 𝗜𝗗 𝗶𝘀

››𝗦𝘁𝗶𝗰𝗸𝗲𝗿 𝗜𝗗:
`{file_id}`

🆔 𝗨𝗻𝗶𝗾𝘂𝗲 𝗜𝗗:
`{unique_id}`
""",
        reply_markup=copy_buttons(file_id)
    )

    waiting_users.remove(uid)

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
