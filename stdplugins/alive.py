""".alive Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="alive"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`AƁƐƳ SAALƐ!╰(°ㅂ°)╯Ƶιη∂α нυ мαι! Mααƒ кαяηα gυѕѕє мє ι∂нαя υ∂нαя ηιкαℓ נαтα нυ..\n\nƬєℓєтнση νєяѕιση:69.69\nƤутнση:6.9\nƤєяυ Uѕєя:`[█▬█ █ ▀█▀](tg://user?id=705627922) \n`Ɓσт Ƈяєαтσя:`@CallMe_HIT\n\n`Sєχвαѕє Sтαтυѕ:Ƭєℓєgяαм ѕєχвαѕєѕ ƒυηcтισηιηg ησямαℓℓу!\n\nI am ꔠ༏ⲧᏰ❍ⲧ swagat toh karo hamara...`\n\n**Ƈαℓℓ Jσнηηу Sιηѕ тσ ∂єρℓσу тнιѕ υѕєявσт ησω:**+916969696969"
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
