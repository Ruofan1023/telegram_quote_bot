# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import constants as keys
from telegram.ext import *
import zenQuote as zenQuote

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('I am Quote Bot')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def start_command(update, context):
    update.message.reply_text("Type something interesting!")

def zenquote_command(update, context):
    update.message.reply_text(zenQuote.get_random_zen_quote())

def handle_message(update, contest):
    text = str(update.message.text)
    update.message.reply_text(text)

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("zen", zenquote_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()

main()
