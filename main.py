import datetime
import telegram
import os
from telegram.ext import Updater
from telebot.types import ChatPermissions

TOKEN = os.getenv("TG_BOT_TOKEN")

u = Updater(TOKEN)
j = u.job_queue

# Ask your Peer advisor chat_id: -1001258717612

def openchat(context: telegram.ext.CallbackContext):
    context.bot.set_chat_permissions("-1001258717612",
                                     ChatPermissions(can_send_messages=True, can_send_media_messages=True,
                                                     can_send_polls=True, can_send_other_messages=True,
                                                     can_add_web_page_previews=True,
                                                     can_change_info=None, can_invite_users=True,
                                                     can_pin_messages=None))
    context.bot.send_message("-1001258717612", "Dear Students,\n\n"
                                               "💬 The chat is open for your messages.\n\n "
                                               "Have a productive week!")
    print("Found match: Monday 8am, opening chat...")


def closechat(context: telegram.ext.CallbackContext):
    context.bot.set_chat_permissions("-1001258717612",
                                     ChatPermissions(can_send_messages=None, can_send_media_messages=None,
                                                     can_send_polls=None, can_send_other_messages=None,
                                                     can_add_web_page_previews=None,
                                                     can_change_info=None, can_invite_users=True,
                                                     can_pin_messages=None))
    context.bot.send_message("-1001258717612", "Dear Students,\n\n"
                                               "As usual, on weekend, messaging to our chat is restricted. We will "
                                               "resume messaging again on Monday morning.\n\n"
                                               "❔ If you have any questions, please check pinned messages above and "
                                               "use "
                                               "search, most likely, these questions have been already answered.\n\n"
                                               "Have a great weekend!")
    print("Found match: Friday 6pm, closing chat...")


def check_date_and_time(context: telegram.ext.CallbackContext):
    thetime = datetime.datetime.now()
    print("Check called - hour now is: {} day num is: {}".format(thetime.hour, thetime.weekday()))

    if thetime.weekday() == 4 and thetime.hour == 17:
        closechat(context)
    elif thetime.weekday() == 0 and thetime.hour == 8:
        openchat(context)


j.run_repeating(check_date_and_time, 3600)
print("done")

u.start_polling()
u.idle()
