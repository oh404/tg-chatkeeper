import datetime
from datetime import date
import telegram
from telegram.ext import Updater, CallbackContext, CommandHandler
import time
from pytz import timezone

import telebot
from telebot.types import ChatPermissions

TOKEN = '1647052009:AAH4WbN11l_ty7178cA47wnQsIKWfN91wgY'

u = Updater(TOKEN)

j = u.job_queue
# Ask your Peer advisor chat_id: -1001258717612

# @bot.message_handler(commands=['open'])
def openchat(context: telegram.ext.CallbackContext):
    context.bot.set_chat_permissions("-1001258717612", ChatPermissions(can_send_messages=True, can_send_media_messages=True,
                                                               can_send_polls=True, can_send_other_messages=True,
                                                               can_add_web_page_previews=True,
                                                               can_change_info=None, can_invite_users=True,
                                                               can_pin_messages=None))
    context.bot.send_message("-1001258717612", "Monday morning. Chat OPEN")

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



def check_date_and_time(context: telegram.ext.CallbackContext):
    thetime = datetime.datetime.now()
    print("Check called - hour now is: {} day num is: {}".format(thetime.hour, thetime.weekday()))

    if thetime.weekday() == 2 and thetime.hour == 17:
        print("Found match: Friday 6pm, closing chat...")
        context.bot.send_message(chat_id="-1001258717612", text='The time is NOW')
    elif thetime.weekday() == 0 and thetime.hour == 8:
        print("Found match: Monday 8am, opening chat...")
        context.bot.send_message(chat_id="-1001258717612", text='The time is NOW')


j.run_repeating(check_date_and_time, 5)

u.start_polling()
u.idle()
