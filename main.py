import datetime
from datetime import date
import telegram
from telegram.ext import Updater, CallbackContext, CommandHandler
import time
from pytz import timezone

import telebot
from telebot.types import ChatPermissions

# bot = telebot.TeleBot('1647052009:AAH4WbN11l_ty7178cA47wnQsIKWfN91wgY')
u = Updater('1647052009:AAH4WbN11l_ty7178cA47wnQsIKWfN91wgY')

j = u.job_queue




t = datetime.time(16, 3, 00, 000000)
g = time.tzname
print("Today's date:", t)
print("Today's date:", g)


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
    print("Check called - hour now is:", thetime.hour)
    print("Check called - day num now is:", thetime.weekday())

#    if (thetime.hour == 17)

    context.bot.send_message(chat_id="-1001258717612", text='The time is now')


#j.run_repeating(check_date_and_time, 3600)

# t = datetime.time(16, 8, 00, 000000)

# j.run_daily(callback_30, t, days=(2,3))

# j.run_once(callback_30, datetime.time(16, 18, 00))


#target_time = datetime.time(hour=16, minute=56).replace(tzinfo=timezone('Asia/Qyzylorda'))
#j.run_daily(callback_30, target_time, days=(0, 1, 2, 3, 4, 5, 6))
#print(target_time)

# timer_handler = CommandHandler('timer', callback_timer)
# u.dispatcher.add_handler(timer_handler)

# schedule.every(1).minutes.do(openchat)
# schedule.every(2).minutes.do(closechat)
# schedule.every().monday.at("08:30").do(openchat)
# schedule.every().friday.at("18:00").do(closechat)

# j.run_once(openchat, 10)
# j.run_once(closechat, 15)

# bot.polling()

u.start_polling()
u.idle()

# updater.start_polling()
