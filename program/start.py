import asyncio

from datetime import datetime
from sys import version_info
from time import time

from config import (
    BG_IMG,
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
)
from driver.decorators import check_blacklist
from program import __version__, LOGS
from driver.core import bot, me_bot, me_user
from driver.filters import command
from driver.database.dbchat import add_served_chat, is_served_chat
from driver.database.dbpunish import is_gbanned_user
from driver.database.dbusers import add_served_user, is_served_user
from driver.database.dblockchat import blacklisted_chats

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, ChatAdminRequired
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
@check_blacklist()
async def start_(c: Client, message: Message):
    user_id = message.from_user.id
    if await is_served_user(user_id):
        pass
    else:
        await add_served_user(user_id)
        return
    await message.reply_text(
        f"""👋 **اهلا💫 {message.from_user.mention()} !**\n
🤖 [{me_bot.first_name}](https://t.me/{BOT_USERNAME}) **يسمح لك بتشغيل اغاني🎶 و أفلام 🎥 في المحادثه الصوتيه بالجروب!**\n
📕 **لمعرفه جميع اوامر البوت الكامله الرجاء الضغط علي » 🛠️ الاوامر!**\n
🔖 **لمعرفة كيفية استعمال البوت الرجاء الضغط علي » 📕 دليل الاستعمال!**\n
👽 **للتواصل مع صاحب السورس الرجاء الضغط علي» 👉 𝐅𝐑𝟑𝐎𝐍 𝐒𝐎𝐔𝐑𝐂𝐄🌐 **\n """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ اضفني الي مجموعتك ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("📕 دليل الاستعمال", callback_data="user_guide")],
                [
                    InlineKeyboardButton("🛠️ الاوامر", callback_data="command_list"),
                    InlineKeyboardButton("🌐 صاحب البوت", url=f"https://t.me/{OWNER_USERNAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👨🏾‍🤝‍👨🏼 جروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🔗 قناه الدعم", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐌𝐒𝐌🌐", url="https://t.me/source_frawn"
                    )
                ],
                [    InlineKeyboardButton(
                    "🌐للتواصل مع صاحب السورس🌐", url="https://t.me/DEV_FRAWN"
                     )
                ],
                [
                    InlineKeyboardButton(
                    "🌐شات للدعم والاستفسارات🌐", url="https://t.me/f_r_a_w_n_a"
                    )
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
    
@Client.on_message(
    command(["/help", f"/help@{BOT_USERNAME}", "help", "الاوامر"]) & filters.group & ~filters.edited
)
@check_blacklist()
async def ghelp(c: Client, message: Message):
    await message.reply_text(
        f""" ✨ **اهلا [{query.message.chat.first_name}] !**\n
⌯ **لمعرفة كيفية إعداد هذا البوت؟  اقرأ➢ اعداد البوت في هاذه المجموعه **\n
⌯ **لمعرفة تشغيل الفيديو / الصوت / لايف؟  اقرا اوامر الاستخدام السريع **\n
⌯ **لمعرفة كل أمر من البوتات؟  اقرأ كل الاوامر**\n """,
        reply_markup=InlineKeyboardMarkup(
        
        [
            [
                InlineKeyboardButton(
                    "- إعداد هذا البوت في المجموعة -", callback_data="user_guide"
                )
            ],
            [
                InlineKeyboardButton(
                    "- أوامر الاستخدام السريع -", callback_data="quick_use"
                )
            ],
            [
                InlineKeyboardButton(
                    "- كل الاوامر هنا -", callback_data="command_list"
                )
            ],
            [
                InlineKeyboardButton(
                    "- للرجوع من هنا -", callback_data="home_start"
                )
            ],
            [
                InlineKeyboardButton("- جـروب الـدعـم -", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "- قـنـاه الـسـورس -", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
            
        ]      
  ),
    disable_web_page_preview=True,
    )
@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}", "بوت"]) & filters.group & ~filters.edited
)
@check_blacklist()
async def alive(c: Client, message: Message):
    chat_id = message.chat.id
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- 𝐆𝐑𝐎𝐔𝐏 -", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "- 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 -", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, I'm {me_bot.first_name}**\n\n🧑🏼‍💻 My Master: [{ALIVE_NAME}](https://t.me/{OWNER_USERNAME})\n👾 Bot Version: `v{__version__}`\n🔥 Pyrogram Version: `{pyrover}`\n🐍 Python Version: `{__python_version__}`\n✨ PyTgCalls Version: `{pytover.__version__}`\n🆙 Uptime Status: `{uptime}`\n\n❤ **Thanks for Adding me here, for playing video & music on your Group's video chat**"

    await c.send_photo(
        chat_id,
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", "بنج", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", "الحاله", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(c: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )


@Client.on_chat_join_request()
async def approve_join_chat(c: Client, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as e:
        await asyncio.sleep(e.x + 2)
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    for member in m.new_chat_members:
        try:
            if member.id == me_bot.id:
                if chat_id in await blacklisted_chats():
                    await m.reply_text(
                        "❗️ This chat has blacklisted by sudo user and You're not allowed to use me in this chat."
                    )
                    return await bot.leave_chat(chat_id)
            if member.id == me_bot.id:
                return await m.reply(
                    "❤️ Thanks for adding me to the **Group** !\n\n"
                    "Appoint me as administrator in the **Group**, otherwise I will not be able to work properly, and don't forget to type `/userbotjoin` for invite the assistant.\n\n"
                    "Once done, then type `/reload`",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("- 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 -", url=f"https://t.me/{UPDATES_CHANNEL}"),
                                InlineKeyboardButton("- 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 -", url=f"https://t.me/{GROUP_SUPPORT}")
                            ],[
                                InlineKeyboardButton("- 𝐀𝐒𝐒𝐈𝐒𝐓𝐀𝐍𝐓 -", url=f"https://t.me/{me_user.username}")
                            ]
                        ]
                    )
                )
            return
        except BaseException:
            return

@Client.on_message(command("/start") & filters.private & ~filters.edited)
async def startt_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f""" اهلا بك انا بوت اسمي {me_bot.first_name} 📌 !**\n
➥ ** لو عاوز تشوف الاوامر وطريقه التشغيل اضغط علي اول زر↯ **\n
➥ ** تخصصي تشغيل الموسيقي والافلام في المحدثات الصواتيه الخاصه بي التليحرام↯ **\n
➥ ** الزر التاني للتواصل مع المبرمج سمسم **\n
➥ ** اضغط علي اسم المطور للدخول الي شاتو تلقائي↯**\n """,
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("قم بي الضغط للاستمرار -", callback_data="rbic")
                        ],
                        [   
                            InlineKeyboardButton("تواصل المطور من هنا -", callback_data="nglish")
                        ],
                        [
                            InlineKeyboardButton("[⌯ 𝗙𝙍𝗔𝙒𝗡 𝙒𝗔 ⌯", url=f"https://t.me/DEV_FRAWN")
                        ]
                    ]
                )
            )

chat_watcher_group = 5

@Client.on_message(group=chat_watcher_group)
async def chat_watcher_func(_, message: Message):
    userid = message.from_user.id
    suspect = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if await is_gbanned_user(userid):
        try:
            await message.chat.ban_member(userid)
        except ChatAdminRequired:
            LOGS.info(f"can't remove gbanned user from chat: {message.chat.id}")
            return
        await message.reply_text(
            f"👮🏼 (> {suspect} <)\n\n**Gbanned** user detected, that user has been gbanned by sudo user and was blocked from this Chat !\n\n🚫 **Reason:** potential spammer and abuser."
        )
