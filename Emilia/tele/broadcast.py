from pyrogram import filters
from pyrogram.errors import FloodWait, UserIsBlocked, PeerIdInvalid
from Emilia import pgram, LOGGER
from Emilia.data import HELPABLE
from Emilia.utils.admins import dev_plus

__mod_name__ = "Broadcast"
__help__ = """
<u><b>Broadcast Module</b></u>

• /broadcast <text>
   — Broadcast text message to all users

• Reply to any photo/video/document using:
   — /broadcast
"""

async def send_msg(user_id, message):
    try:
        await message.copy(user_id)
        return True
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await send_msg(user_id, message)
    except (UserIsBlocked, PeerIdInvalid):
        return False
    except Exception:
        return False

@pgram.on_message(filters.command("broadcast") & dev_plus)
async def broadcast_handler(client, message):
    msg = message.reply_to_message
    text = None

    if msg:
        to_send = msg
    else:
        if len(message.command) < 2:
            return await message.reply("Give some text or reply to a message.")
        text = message.text.split(None, 1)[1]
        to_send = await message.reply(text)

    await message.reply("Broadcast Started...")

    from Emilia.data.users import get_all_users
    users = await get_all_users()

    success = 0
    failed = 0

    for user_id in users:
        ok = await send_msg(user_id, to_send)
        if ok:
            success += 1
        else:
            failed += 1

    LOGGER.info(f"Broadcast finished: Success={success}, Failed={failed}")

    await message.reply(
        f"**Broadcast Completed**\n"
        f"✔️ Sent: `{success}`\n"
        f"❌ Failed: `{failed}`"
    )
