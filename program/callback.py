# Copyright (C) 2022 By SuraVCProject

from driver.core import me_bot, me_user
from driver.queues import QUEUE
from driver.decorators import check_blacklist
from program.utils.inline import menu_markup, stream_markup

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import (
    BOT_USERNAME,
    BG_IMG,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)



@Client.on_callback_query(filters.regex("rbic"))
async def rbic(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""مرحباً بك \n
⌁ ⁞  بوت تشغيل الأغاني والفيديو  في المكالمه ' المرئية
 البوت قيد التشغيل الان ⌯
⌁ ⁞ my developer [[⌯ 𝗙𝙍𝗔𝙒𝗡 𝙒𝗔 ⌯](https://t.me/DEV_FRAWN)
⌁ ⁞  قم بإضافة البوت اللي مجموعتك واستمع إلى الموسيقى ومشاهدة الفيديوهات ⌯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- اضف البوت اللي مجموعتك -",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("- طريقة التفعيل -", callback_data="quick_use")],
                [
                    InlineKeyboardButton("- طريقة التشغيل -", callback_data="command_list"),
                    InlineKeyboardButton("- المطور -", url=f"https://t.me/DEV_FRAWN"),
                ],
                [
                    InlineKeyboardButton(
                        "- الجروب -", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "- القناة -", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "[⌯ 𝗙𝙍𝗔𝙒𝗡 𝙒𝗔 ⌯", url="https://t.me/DEV_FRAWN"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("nglish"))
async def nglish(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"هنا لنكات تواصل  \n لو احتجت اي حاجه كلم المطور \n عن طريق الضغط علي تواصل واتساب \nاو الضغط علي اسم المطور ده➼ [[⌯ 𝗙𝙍𝗔𝙒𝗡 𝙒𝗔⌯](https://t.me/𝗙𝙍𝗔𝙒𝗡 𝙒𝗔)",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- اضف البوت الي مجموعتك -",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("- للتواصل واتساب -", url=f"http://wa.me/+201010294706")],
                [
                    InlineKeyboardButton("- جروب دردشه -", url=f"https://t.me/f_r_a_w_n_a"),
                    InlineKeyboardButton("- المطور -", url=f"https://t.me/DEV_FRAWN"),
                ],
                [
                    InlineKeyboardButton(
                        "- جروب الدعم -", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "- قناه البوت -", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "[⌯ 𝗙𝙍𝗔𝙒𝗡 𝙒𝗔 ⌯", url="https://t.me/DEV_FRAWN"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )    
    
@Client.on_callback_query(filters.regex("help_command"))
@check_blacklist()
async def help(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("help message")
    await query.edit_message_text(
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
 

@Client.on_callback_query(filters.regex("quick_use"))
@check_blacklist()
async def quick_set(_, query: CallbackQuery):
    await query.answer("quick bot usage")
    await query.edit_message_text(
        f"""ᯤ دليل بوت سريع الاستخدام ، يرجى القراءة بالكامل !

» /play - play - شغل - تشغيل Type this with give the song title or youtube link or audio file to play Music. (Remember to don't play YouTube live stream by using this command!, because it will cause unforeseen problems.)

» /vplay - vplay - فيديو Type this with give the song title or youtube link or video file to play Video. (Remember to don't play YouTube live video by using this command!, because it will cause unforeseen problems.)

» /vstream - لايف Type this with give the YouTube live stream video link or m3u8 link to play live Video. (Remember to don't play local audio/video files or non-live YouTube video by using this command!, because it will cause unforeseen problems.)

❓ Still Have questions? Contact us in [Support Group](https://t.me/{GROUP_SUPPORT}).""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("- رجوع الي قائمه طريقه التشغيل -", callback_data="user_guide")],
                [InlineKeyboardButton("- للرجوع الي الاوامر  -", callback_data="help_command")]    
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
@check_blacklist()
async def guide_set(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f""" ᯤ كيف يتم إعداد هذا الروبوت في المجموعة؟ ، !
1.) أولاً ، أضف هذا الروبوت إلى مجموعتك.
2.) بعد ذلك ، قم بترقية هذا الروبوت كمسؤول في المجموعة ، وقم أيضًا بمنح جميع الأذونات باستثناء المسؤول المجهول..
3.) بعد الترويج لهذا البوت  /reload أعد التحميل في المجموعة لتحديث بيانات المسؤول.
3.) قم بدعوة @{me_user.username} إلى مجموعتك أو اكتب /userbotjoin او اكتب انضم لدعوتها ، لسوء الحظ ، سينضم الحساب المساعد بنفسه عند استخدام أوامر تشغيل الأغنية.
4.) قم بتشغيل  بدء محادثة الفيديو أولاً قبل البدء في تشغيل الفيديو  الموسيقى.

`- النهاية ، تم إعداد كل شيء -`

ᯤ إذا لم ينضم المستخدم الروبوت إلى الدردشة المرئية ، فتأكد من تشغيل دردشة الفيديو بالفعل ومن أن المستخدم الروبوت في الدردشة.

ᯤ إذا كانت لديك أسئلة متابعة حول هذا الروبوت ، فيمكنك إخبارها في دردشة الدعم هنا: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("- دليل الاستخدام السريع -", callback_data="quick_use")
                ],[
                    InlineKeyboardButton("- للرجوع الي القائمه الرائسيه -", callback_data="rbic")
                ],[
                    InlineKeyboardButton("- للرجوع الي الاوامر -", callback_data="help_command")
                ]
            ]   
      ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨ **اهلا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

»تحقق من القائمة أدناه لقراءة معلومات الوحدة والاطلاع على قائمة الأوامر المتاحة!

ارجو الاستمتاع بي المميزات💞""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("- اوامر الادمن -", callback_data="admin_command"),
                ],[
                    InlineKeyboardButton("- أوامر المستخدمين -", callback_data="user_command"),
                ],[
                    InlineKeyboardButton("- اوامر المسؤلين -", callback_data="sudo_command"),
                    InlineKeyboardButton("- اوامر المالك -", callback_data="owner_command"),
                ],[
                    InlineKeyboardButton("- للرجوع الي القائمه الرائسيه -", callback_data="rbic")
                ],[
                    InlineKeyboardButton("- للرجوع الي قائمه الاوامر -", callback_data="help_command")
                ]
                   
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✏️ Command list for all user.

» /play - play - شغل - تشغيل (song name/link) - play music on video chat
» /vplay - فيديو - vplay (video name/link) - play video on video chat
» /vstream - لايف (m3u8/yt live link) - play live stream video
» /playlist - القائمه see the current playing song
» /lyric (query) - scrap the song lyric
» /video (query) - download video from youtube
» /song - تنزيل للاغنيه- نزيل للفيديو  (query) - download song from youtube
» /search (query) - search a youtube video link
» /ping - بنج show the bot ping status
» /uptime -  show the bot uptime status
» /alive - بوت show the bot alive info (in Group only)
» /help - الاوامر to Show Help Message (Full Bot Guide)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("- للرجوع -", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("admin_command"))
@check_blacklist()
async def admin_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""هنا اوامر الادمن 💞.

» /pause - مؤقت pause the current track being played
» /resume - استمرار play the previously paused track
» /skip - تخطي goes to the next track
» /stop - /end - اسكت - وقف - ايقاف stop playback of the track and clears the queue
» /vmute - mute the streamer userbot on group call
» /vunmute - unmute the streamer userbot on group call
» /volume `1-200` - adjust the volume of music (userbot must be admin)
» /reload - reload bot and refresh the admin data
» /userbotjoin - انضم invite the userbot to join group
» /userbotleave - غادر order userbot to leave from group
» /startvc - افتح start/restart the group call
» /stopvc - اقفل stop/discard the group call

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("- للرجوع -", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("sudo_command"))
@check_blacklist()
async def sudo_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me_bot.first_name
    if user_id not in SUDO_USERS:
        await query.answer("⚠️ You don't have permissions to click this button\n\n» This button is reserved for sudo members of this bot.", show_alert=True)
        return
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""✏️ Command list for sudo user.

» /stats - get the bot current statistic
» /calls - show you the list of all active group call in database
» /block (`chat_id`) - use this to blacklist any group from using your bot
» /unblock (`chat_id`) - use this to whitelist any group from using your bot
» /blocklist - show you the list of all blacklisted chat
» /speedtest - run the bot server speedtest
» /sysinfo - show the system informatio
» /logs - generate the current bot logs
» /eval - execute any code (`developer stuff`)
» /sh - run any command (`developer stuff`)

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("- للرجوع -", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("owner_command"))
@check_blacklist()
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me_bot.first_name
    if user_id not in OWNER_ID:
        await query.answer("⚠️ You don't have permissions to click this button\n\n» This button is reserved for owner of this bot.", show_alert=True)
        return
    await query.answer("owner commands")
    await query.edit_message_text(
        f"""✏️ Command list for bot owner.

» /gban - حظر  (`username` or `user_id`) - for global banned people, can be used only in group
» /ungban - فكحظر (`username` or `user_id`) - for un-global banned people, can be used only in group
» /update - update your bot to latest version
» /restart - restart your bot directly
» /leaveall - order userbot to leave from all group
» /leavebot (`chat id`) - order bot to leave from the group you specify
» /broadcast (`message`) - send a broadcast message to all groups in bot database
» /broadcast_pin (`message`) - send a broadcast message to all groups in bot database with the chat pin

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("- للرجوع -", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer(" الازار دي مش ليك يحب🙂 !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("control panel opened")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("❌ لا يوجود شئ مشغل", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗ الازار دي مش ليك يحل🙂 !", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗ بسلعب الازار للادمن بس💞 !", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()

@Client.on_callback_query(filters.regex("ahmedelnqyb"))
async def ahmedelnqyb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>◉ انا سمسم الكبير يمكنك التواصل معي..↑↓ \n\n◉ عن طريق معرفي اول جروب التواصل بلاسفل..↑↓ \n\n [[⌯ 𝗗͛𝗲͛𝘃͛ 𝗦͛𝗺͛𝗦͛𝗺͛ 𝗘͛𝗹͛𝗞͛𝗯͛𝗘͛𝗿͛ - ⌯]𝟏𝟎𝐊🍷𖣩ًََِْٰٓ ⃝⃙🇽🇰 ⌯](https://t.me/PV_SMSM)</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("- القناة -", url=f"https://t.me/S_S9_V"),
                    InlineKeyboardButton("- الجروب -", url=f"https://t.me/CO0O00"),
                ],
                [
                    InlineKeyboardButton("- جروب الدردشه -", url=f"https://t.me/CO0O00"),
                    InlineKeyboardButton("- تواصل واتساب -", url=f"http://wa.me/+201025515706"),
                ],
                [InlineKeyboardButton("[⌯ 𝗗͛𝗲͛𝘃͛ 𝗦͛𝗺͛𝗦͛𝗺͛ 𝗘͛𝗹͛𝗞͛𝗯͛𝗘͛𝗿͛ - ⌯]𝟏𝟎𝐊🍷𖣩ًََِْٰٓ ⃝⃙🇽🇰 ⌯", url=f"https://t.me/PV_SMSM")],
            ]
        ),
    )
