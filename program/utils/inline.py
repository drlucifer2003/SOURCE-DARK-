""" inline section button """

from config import BOT_USERNAME
from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="𝗠𝗲𝗻𝘂 🖱️", callback_data=f'stream_menu_panel | {user_id}'),
      InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲 🗑️", callback_data=f'set_close'),
    ],
    [
      InlineKeyboardButton("[⌯ 𝗙𝙍𝗔𝙒𝗡 𝙒𝗔 ⌯", callback_data="fr3onelkbeer")
  ]
 ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="𝗘𝗡𝗗 ⏹", callback_data=f'set_stop | {user_id}'),
      InlineKeyboardButton(text="𝗣𝗔𝗨𝗦𝗘 ⏸", callback_data=f'set_pause | {user_id}'),
      InlineKeyboardButton(text="𝗥𝗘𝗦𝗨𝗠𝗘 ▶️", callback_data=f'set_resume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="𝗠𝗨𝗧𝗘 🔇", callback_data=f'set_mute | {user_id}'),
      InlineKeyboardButton(text="𝗨𝗡 𝗠𝗨𝗧𝗘 🔊", callback_data=f'set_unmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="[⌯ 𝗙𝙍𝗔𝙒𝗡 𝙒𝗔 ⌯", callback_data='stream_home_panel'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "𝗖𝗹𝗼𝘀𝗲 🗑️", callback_data="set_close"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 𝗚𝗼 𝗕𝗮𝗰𝗸", callback_data="stream_menu_panel"
      )
    ]
  ]
)
