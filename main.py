import datetime
from datetime import date
import telegram
from telegram.ext import Updater, CallbackContext, CommandHandler
import time
from pytz import timezone

import telebot
from telebot.types import ChatPermissions

TOKEN = 'xxx'

# bot = telebot.TeleBot(TOKEN)
u = Updater(TOKEN)

j = u.job_queue
# Ask your Peer advisor chat_id: -1001258717612

# @bot.message_handler(commands=['close'])
def closechat(context: telegram.ext.CallbackContext):
    context.bot.set_chat_permissions("-1001258717612",
                                     ChatPermissions(can_send_messages=None, can_send_media_messages=None,
                                                     can_send_polls=None, can_send_other_messages=None,
                                                     can_add_web_page_previews=None,
                                                     can_change_info=None, can_invite_users=True,
                                                     can_pin_messages=None))
    #    bot.reply_to(message, "Chat closed")
    context.bot.send_message("-1001258717612", "Friday evening. Chat CLOSED")


# @bot.message_handler(commands=['open'])
# def openchat(message):
#    bot.set_chat_permissions("-1001258717612", ChatPermissions(can_send_messages=True, can_send_media_messages=True,
#                                                               can_send_polls=True, can_send_other_messages=True,
#                                                               can_add_web_page_previews=True,
#                                                               can_change_info=None, can_invite_users=True,
#                                                               can_pin_messages=None))
#    #    bot.reply_to(message, "Chat closed")
#    bot.send_message("-1001258717612", "Monday morning. Chat OPEN")

def check_date_and_time(context: telegram.ext.CallbackContext):
    thetime = datetime.datetime.now()
    print("Check called - hour now is: {} day num is: {}".format(thetime.hour, thetime.weekday()))

    #    if (thetime.hour == 17)

    context.bot.send_message(chat_id="-1001258717612", text='The time is now')


j.run_repeating(check_date_and_time, 2)


u.start_polling()
u.idle()
