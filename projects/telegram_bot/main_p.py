import telebot
import json


bot = telebot.TeleBot('6746732884:AAF0JuOOQAgeRjDNs6mstjp9sCRlQCdhMz0')  
user_data = {}
current_step = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет я твои заметки. Чтобы начать запись дaнных нaжми /to_do')


@bot.message_handler(commands=['to_do'])
def record_data(message):
    user_id = message.chat.id
    current_step[user_id] = 'name'
    user_data[user_id] = {'step': 'name'}
    bot.send_message(message.chat.id, 'Введите ваше имя')

@bot.message_handler(func=lambda message: current_step.get(message.chat.id) == 'name')
def process_name(message):
    user_id = message.chat.id
    current_step[user_id] = 'task'
    user_data[user_id]['name'] = message.text
    bot.send_message(message.chat.id, 'Какое задание вы хотите выполнить')

@bot.message_handler(func=lambda message: current_step.get(message.chat.id) == 'task')
def process_task(message):
    user_id = message.chat.id
    user_data[user_id]['task'] = message.text
    write_to_json(user_data)
    bot.send_message(message.chat.id, 'Конец')
    
    

def write_to_json(user_data):
    with open('data.json', 'w+') as file_:
        data = json.dump(user_data, file_)
        

bot.polling(none_stop=True)