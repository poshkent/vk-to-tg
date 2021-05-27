from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
from telebot import TeleBot


app = TeleBot(__name__)
login, password = '375291110684','vitalyapidor'
vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)
vk_session.auth(token_only=True)
beseda_id = -1001185015555
dima_id = 752872267
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
app.config['api_key'] = '1865332498:AAG_YdPxLZWqeNjA2BJRb6qWHHdi5TaxZaw'


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
        app.send_message(beseda_id, text)  
        app.send_message(dima_id, text) 


app.poll(debug=True)