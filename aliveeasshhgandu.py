""".alive Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("alive"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n█░░░░░░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░░░░░█\n█░░░░░░░║║║╠─║─║─║║║║║╠─░░░░░░█\n█░░░░░░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░░░░░█\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n█                             █\n█       ÚSΞЯ:@ᴀᴀsʜɪǫ_ᴛɢ       █\n█      Sᴇʀᴠᴇʀ:🄾🄽🄻🄸🄽🄴        █\n█ ᴅᴏɴ'ᴛ ᴡᴏʀʀʏ ɪ ɢᴏᴛ ʏᴏᴜʀ ʙᴀᴄᴋ █\n█       ɪ'ᴀᴍ ᴀʟɪᴠᴇ ʙᴏss       █\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
