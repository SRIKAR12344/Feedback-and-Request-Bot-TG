import logging

from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import bot.configs as vars

logging.getLogger(__name__).setLevel(logging.INFO)


# IMPORTANT VARIABLES
OWNER_ID = vars.OWNER_ID

LOG_TEXT = "ID: <code>{}</code>\nName: <a href='tg://user?id={}'>{}{}</a>\nStarted the bot..."
START_TEXT = "𝗛𝗘𝗬 𝗪𝗔𝗦𝗦𝗨𝗣 𝗠𝗔𝗧𝗘 😍\n➜𝗪𝗘 𝗔𝗥𝗘 𝗧𝗛𝗘 𝗢𝗪𝗡𝗘𝗥𝗦 𝗢𝗙 𝗞𝗢𝗥𝗘𝗔𝗡 𝗗𝗥𝗔𝗠𝗔𝗦\n➜𝗛𝗢𝗣𝗘 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗗𝗢𝗜𝗡𝗚 𝗪𝗘𝗟𝗟\n➜𝗦𝗢 𝗛𝗘𝗥𝗘 𝗪𝗘 𝗔𝗥𝗘 𝗬𝗢𝗨 𝗖𝗔𝗡 𝗚𝗜𝗩𝗘 𝗙𝗘𝗘𝗗𝗕𝗔𝗖𝗞 𝗛𝗘𝗥𝗘 𝗔𝗕𝗢𝗨𝗧 𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n➜𝗥𝗘𝗤𝗨𝗘𝗦𝗧 𝗔𝗡𝗬 𝗞𝗗𝗥𝗔𝗠𝗔𝗦 𝗢𝗥 𝗠𝗢𝗩𝗜𝗘𝗦 𝗦𝗢 𝗪𝗘 𝗨𝗣𝗟𝗢𝗔𝗗 𝗜𝗧😇\n\n➜𝗥𝗨𝗟𝗘𝗦 𝗔𝗡𝗗 𝗖𝗢𝗡𝗗𝗜𝗧𝗜𝗢𝗡𝗦\n\n˚₊· ͟͟͞͞➳❥𝗣𝗟𝗦 𝗗𝗢𝗡𝗧 𝗦𝗣𝗔𝗠 𝗧𝗛𝗘 𝗕𝗢𝗧\n˚₊· ͟͟͞͞➳❥𝗝𝗨𝗦𝗧 𝗟𝗘𝗔𝗩𝗘 𝗧𝗛𝗘 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗪𝗘 𝗪𝗜𝗟𝗟 𝗦𝗨𝗥𝗘𝗟𝗬 𝗥𝗘𝗣𝗟𝗬\n˚₊· ͟͟͞͞➳❥𝗗𝗢𝗡𝗧 𝗕𝗟𝗢𝗖𝗞 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗬 𝗔𝗡𝗬 𝗠𝗘𝗔𝗡𝗦 𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗥𝗘𝗣𝗟𝗬\n˚₊· ͟͟͞͞➳❥𝗝𝗨𝗦𝗧 𝗥𝗘𝗤𝗨𝗘𝗦𝗧 𝗧𝗛𝗘 𝗗𝗥𝗔𝗠𝗔𝗦 𝗢𝗥 𝗚𝗜𝗩𝗘 𝗙𝗘𝗘𝗗𝗕𝗔𝗖𝗞\n˚₊· ͟͟͞͞➳❥𝗘𝗡𝗝𝗢𝗬 𝗡𝗢𝗪 𝗧𝗛𝗔𝗡𝗞𝗦 𝗙𝗢𝗥 𝗝𝗢𝗜𝗡𝗜𝗡𝗚 𝗢𝗨𝗥 𝗖𝗛𝗔𝗡𝗡𝗘𝗟😍🥰"
MESSAGE = "<b>Message from:</b> <code>{}</code>\n<b>Name:</b> <a href='tg://user?id={}'>{}{}</a>\n\n{}"


# ADDING HANDLERS
def add_feedback_handlers(bot):
    bot.add_handler(
        CommandHandler(command="start", callback=start, filters=Filters.chat_type.private, run_async=True)
    )

    bot.add_handler(
        CommandHandler(command="about", callback=about, filters=Filters.chat_type.private, run_async=True)
    )

    bot.add_handler(
        CallbackQueryHandler(pattern="about", callback=about, run_async=True)
    )

    bot.add_handler(
        MessageHandler(filters=Filters.chat(OWNER_ID), callback=reply, run_async=True)
    )

    bot.add_handler(
        MessageHandler(filters=Filters.chat_type.private, callback=user, run_async=True)
    )





#***************HANDLERS BELOW******************

def start(update, context):
    context.bot.send_message(
        chat_id = OWNER_ID,
        text = LOG_TEXT.format(update.message.chat.id,update.message.chat.id,update.message.chat.first_name,"" if update.message.chat.last_name == None else " "+update.message.chat.last_name),
        parse_mode = "html"
    )
    inline_keyboard = [[InlineKeyboardButton("💬𝗥𝗘𝗤𝗨𝗘𝗦𝗧 𝗚𝗥𝗢𝗨𝗣💬", url = f"{vars.GROUP_LINK}"), InlineKeyboardButton("📢𝗠𝗔𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟📢", url = f"{vars.CHANNEL_LINK}")],[InlineKeyboardButton("😍𝗞𝗗𝗥𝗔𝗠𝗔𝗦 𝗖𝗛𝗔𝗡𝗡𝗘𝗟😍",url='https://t.me/k_Drama_Hindi_Dubbed_avl'), InlineKeyboardButton("😇𝗠𝗢𝗩𝗜𝗘𝗦 𝗖𝗛𝗔𝗡𝗡𝗘𝗟😇",'https://t.me/+A1kqNqAowME4NTM9')],[InlineKeyboardButton("❗𝗢𝗪𝗡𝗘𝗥❗", url="https://t.me/SIRISH_123")]]
    update.message.reply_text(
        "*Hi {}!*\n".format(update.message.chat.first_name)+START_TEXT,
        reply_markup = InlineKeyboardMarkup(inline_keyboard),
        parse_mode = "markdown"
    )

def about(update, context):
    bot_details = context.bot.get_me()
    if update.message is not None:
        message = update.message
    else:
        message = update.callback_query.message
    message.reply_text(
        "*𝗠𝗬 𝗡𝗔𝗠𝗘: [{}](tg://user?id={})\n𝗖𝗥𝗘𝗔𝗧𝗘𝗥: [𝗦𝗜𝗥𝗜𝗦𝗛](https://t.me/SIRISH_123)\n𝗕𝗔𝗖𝗞𝗨𝗣 𝗖𝗛𝗔𝗡𝗡𝗘𝗟: [𝗖𝗟𝗜𝗖𝗞 𝗛𝗘𝗥𝗘](https://t.me/KDRAMSHINDI)\n𝗞𝗗𝗥𝗔𝗠𝗔𝗦 𝗖𝗛𝗔𝗡𝗡𝗘𝗟: [𝗖𝗟𝗜𝗖𝗞 𝗛𝗘𝗥𝗘](https://t.me/k_Drama_Hindi_Dubbed_avl)\n𝗠𝗢𝗩𝗜𝗘𝗦 𝗖𝗛𝗔𝗡𝗡𝗘𝗟: [𝗖𝗟𝗜𝗖𝗞 𝗛𝗘𝗥𝗘](https://t.me/+A1kqNqAowME4NTM9)*".format(bot_details.first_name, bot_details.id),
        parse_mode = "markdownv2",
        disable_web_page_preview = True
    )

def reply(update, context):
    if update.message.reply_to_message is not None:
        replied_to = update.message.reply_to_message
        try:
            reference_id = replied_to.text.split()[2]
        except Exception:
            reference_id = replied_to.caption.split()[2]

        if update.message.text != None:
            context.bot.send_message(
                text=update.message.text_html,
                chat_id=int(reference_id),
                parse_mode = "html"
            )
        else:
            update.message.copy(
                caption=update.message.caption_html,
                chat_id=int(reference_id),
                parse_mode = "html"
            )
        update.message.reply_text(
            text = "Message Sent...✅",
            quote = True
        )

def user(update, context):
    info = update.message.from_user
    reference_id = info.id
    if update.message.text != None:
        context.bot.send_message(
            chat_id = OWNER_ID,
            text = MESSAGE.format(reference_id, reference_id, info.first_name, "" if info.last_name == None else " "+info.last_name, update.message.text_html),
            parse_mode = "html"
        )
    else:
        update.message.copy(
            chat_id = OWNER_ID,
            caption = MESSAGE.format(reference_id, reference_id, info.first_name, "" if info.last_name == None else " "+info.last_name, update.message.caption_html if update.message.caption_html is not None else ""),
            parse_mode = "html"
        )
