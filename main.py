# -*- coding: utf-8 -*-
import config
import telebot
import requests

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    print(message.text)

    bot.send_message(message.chat.id, message.text)
    series = get_new_series()
    bot.send_message(message.chat.id, series)


def get_new_series():
    # Use 'with' to ensure the session context is closed after use.

    with requests.Session() as s:
        # Sign in ororo.tv to be able to see all series
        json = 'https://ororo.tv/en/users/sign_in.json'
        p = s.post(json, data=config.ororo_payload, proxies=config.proxies, headers=config.headers)
        # TODO check if status is 200
        print(p.text)

        # Load series page
        r = s.get('https://ororo.tv/en/shows/gotham',  proxies=config.proxies, headers=config.headers)
        print( r.text)
        return r.text
        #     # etc...
if __name__ == '__main__':
     bot.polling(none_stop=True)