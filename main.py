from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.error import Conflict
from telegram.ext import *
import zenQuote as zenQuote
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('I am Quote Bot')


def start_command(update, context):
    update.message.reply_text("Type something interesting!")


def zen_quote_command(update, context):
    update.message.reply_text(zenQuote.get_random_zen_quote())


def handle_message(update, context):
    text = str(update.message.text)

    update.message.reply_text(text)


def inline_randome_zen_quote(update, context):
    results = [InlineQueryResultArticle(
        id="id",
        title='Random Zen Quote',
        input_message_content=InputTextMessageContent(zenQuote.get_random_zen_quote()),
    )]
    context.bot.answer_inline_query(update.inline_query.id, results)


def main():
    updater = Updater('5048383719:AAGodRcenQaFHOOjLKmc0JeIPIkEzoTzLiw', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("zen", zen_quote_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(InlineQueryHandler(inline_randome_zen_quote))

    updater.start_polling()



main()
