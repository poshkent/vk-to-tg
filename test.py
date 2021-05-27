from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import telebot

bot = telebot.TeleBot('1865332498:AAG_YdPxLZWqeNjA2BJRb6qWHHdi5TaxZaw')
login, password = '375291110684','vitalyapidor'
vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)
vk_session.auth(token_only=True)

vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


bot.poll(debug=True)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        user_get=vk.users.get(user_ids = (event.user_id))
        user_get=user_get[0]
        first_name=user_get['first_name']
        last_name=user_get['last_name']
        full_name=first_name+" "+last_name
        text = "{author}\n{text} \n{time}".format(author = full_name,
        text = event.text, time = datetime.strftime(datetime.now(), "%H:%M:%S"))
        print(text)
        bot.send_message(629075242, text)  
        bot.send_message(752872267, text) 



