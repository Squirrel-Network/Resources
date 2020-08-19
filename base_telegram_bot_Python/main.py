#!/usr/bin/env python
# -*- coding: utf-8 -*-

__copyright__ = "Copyright 2020, SquirrelNetwork"
__credits__ = ["Hersel Giannella"]
__license__ = "GPL 3.0"
__version__ = "8.0.0"
__repository__ = "https://github.com/Squirrel-Network/nebula"
__status__ = "Development"

### IMPORT ###
import logging
from config import Config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Start Command")

def main():
    updater = Updater(Config.TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()