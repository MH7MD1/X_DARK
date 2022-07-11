from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


button1 = [
    [
        InlineKeyboardButton(text="التحديثات", url=f"https://t.me/X_DARK1"),
        InlineKeyboardButton(text="اضفني الي مجموعتك", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="المالك", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text="الدعم", url=f"https://t.me/{SUPPORT_GROUP}"),
    ],                
    [                    
        InlineKeyboardButton(text="مساعده!", callback_data="help_"),
    ],
]


button2 = [
    [
        InlineKeyboardButton(text="العام!", callback_data="basic_"),
        InlineKeyboardButton(text="متقدم!", callback_data="admin_cmd"),
    ],
    [
        InlineKeyboardButton(text="اغلاق", callback_data="close_"),
        InlineKeyboardButton(text="رجوع", callback_data="HOME"),
    ],
]



button3 = [
    [
        InlineKeyboardButton(text="Source", url="https://github.com/ItsmeHyper13/DevuMusic"),
        InlineKeyboardButton(text="رجوع", callback_data="HOME"),
    ],
]


button4 = [
    [
        InlineKeyboardButton(text="اغلاق", callback_data="close_"),
        InlineKeyboardButton(text="رجوع", callback_data="help_"),
    ],
]





