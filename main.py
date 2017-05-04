# -*- coding: utf-8 -*-
import config
import telebot
import lib
import time
import logging
# TODO rewrite using threading as better concurrency lib in python3
import _thread


bot = telebot.AsyncTeleBot(config.token)
series_subscribers = {}
TIMEOUT = 60  * 5 # 5 minutes


@bot.message_handler(commands=['check_series'])
def check_new_series(message):
    global previous_series
    series = lib.get_new_series()
    if previous_series != series:
        bot.send_message(message.chat.id, lib.format_message(series))
        previous_series = series


@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    series_subscribers[message.chat.id] = {"previous_series": []}
    bot.send_message(message.chat.id, "subscribed on series updates")


@bot.message_handler(commands=['unsubscribe'])
def unsubscribe(message):
    series_subscribers.pop(message.chat.id)
    bot.send_message(message.chat.id, "unsubscribed on series updates")


def broadcast_new_series():
    global previous_series
    while True:
        logging.info("[SERIES] Started new broadcasting")
        logging.info("[SERIES] Subscribers {0}".format(series_subscribers))
        series = lib.get_new_series()
        for user in series_subscribers.items():
            previous_series = user[1]["previous_series"]
            if previous_series != series:
                bot.send_message(user[0], lib.format_message(series))
                user[1]["previous_series"] = series
        time.sleep(TIMEOUT)


if __name__ == '__main__':
    previous_series = []
    logging.getLogger('requests').setLevel(logging.CRITICAL)
    logging.basicConfig(format='[%(asctime)s] %(filename)s:%(lineno)d %(levelname)s - %(message)s', level=logging.INFO,
                        # filename='bot_log.log',
                         datefmt='%d.%m.%Y %H:%M:%S')
    logging.info("[App] Logger init")
    _thread.start_new_thread(broadcast_new_series, ())
    logging.info("[App] Bot start")
    bot.polling(none_stop=True)

