from telegram import InlineQueryResultArticle, InputTextMessageContent, Bot
from telegram.ext import *

import uselessFacts
import zenQuote as zenQuote
import greetings

import logging
import os
import schedule
from threading import Thread
from time import sleep


api_key = os.environ['API_KEY']
chat_id = os.environ['CHAT_ID']
# api_key = "5048383719:AAHb9yhpp1wTEcrG-JWg_eL18M4HQw3shuM"
# chat_id = 1132574244
bot = Bot(api_key)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('I am Quote Bot')


def start_command(update, context):
    update.message.reply_text("Type something interesting!")
    chat_id = update.message.chat.id
    print("chat id: " + str(chat_id))


def zen_quote_command(update, context):
    update.message.reply_text(zenQuote.get_random_zen_quote())


def useless_fact_command(update, context):
    update.message.reply_text(uselessFacts.get_random_useless_quote())


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


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


def send_a_quote(greeting):
    return bot.send_message(chat_id, greeting + " \n" + zenQuote.get_random_zen_quote())


def check_on_bot():
    return bot.send_message(chat_id, "Hi I am still alive...\n^_^")


def main():
    # These are scheduled events
    # schedule.every(1).minute.do(check_on_bot)
    for hour in range(10, 24):
        schedule.every().day.at(str(hour) + ":05").do(send_a_quote, greeting=greetings.get_greeting())
    Thread(target=schedule_checker).start()

    # Listens for user events
    updater = Updater(api_key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("zen", zen_quote_command))
    dp.add_handler(CommandHandler("fact", useless_fact_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(InlineQueryHandler(inline_randome_zen_quote))
    updater.start_polling()
    updater.idle()


main()
