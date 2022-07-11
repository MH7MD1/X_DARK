# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

from asyncio.queues import QueueEmpty
from config import que, SUPPORT_GROUP
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.admins import set
from helpers.decorators import authorized_users_only, errors
from helpers.channelmusic import get_chat_id
from helpers.filters import command, other_filters
from callsmusic import callsmusic, queues
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, KeyboardButton,
                            ReplyKeyboardMarkup, ReplyKeyboardRemove)



BUTTON = [
    [
        InlineKeyboardButton(text="الدعم", url=f"https://t.me/{SUPPORT_GROUP}"),
        InlineKeyboardButton(text="🗑️اغلاق", callback_data="close_"),
    ],
]

ACTV_CALLS = []

@Client.on_message(command(["pause"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    await callsmusic.pytgcalls.pause_stream(message.chat.id)   
    await message.reply_text(
        f"تم الايقاف مؤقت بواسطة {message.from_user.mention} 🥀\n\n✦"
    )
    await message.delete()


@Client.on_message(command(["resume"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    await callsmusic.pytgcalls.resume_stream(message.chat.id)
    await message.reply_text(
        f"تم اسئناف التشغيل بواسطة {message.from_user.mention} 💫.\n\n✦"
    )
    await message.delete()


@Client.on_message(command(["end"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
        callsmusic.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    await callsmusic.pytgcalls.leave_group_call(message.chat.id)   
    await message.reply_text(
        f"تم انهاء التشغيل بواسطة {message.from_user.mention} \n "
    )
    await message.delete()
    

@Client.on_message(command(["skip"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        
        await message.reply_text(
            "لا🙄!",
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
        await message.delete()
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            await callsmusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        callsmusic.queues.get(chat_id)["file"],
                    ),
                ),
            )   
    await message.reply_text(
        f"تم التخطي الي المسار التالي!\nبواسطة {message.from_user.mention}🥀"
    )
    await message.delete()
