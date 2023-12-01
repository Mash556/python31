import telebot
from telebot import types

bot = telebot.TeleBot('6720341350:AAF54NcH1_Wo096Oaj64rqLHpX50mTgWG6c')


keyboard = types.ReplyKeyboardMarkup()

button = types.KeyboardButton('Играть')
button2 = types.KeyboardButton('Не играть')

keyboard.add(button)
keyboard.add(button2)

@bot.message_handler(commands=['start','hi'])
def start_message(message):
    bot.send_message(message.chat.id, 'How are you?',reply_markup=keyboard)
    bot.register_next_step_handler(message, func)  #отвечает за сценарий

def func(message):
    if message.text == 'Играть':
        bot.send_message(message.chat.id, 'Начнем игру')  
    # elif message.text == 'Не играть':
    #    bot.send_message(message.chat.id, 'Удачи') 
    else:
        bot.send_message(message.chat.id, 'Пока')
    bot.register_next_step_handler(message, start_message)
    
@bot.message_handler(content_types=['sticker'])
def echo_all(message):
    print(message.sticker)
    #bot.send_message(message.chat.id, message.text)
    # bot.reply_to(message, message.text)
    #bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEKqkBlQ6E2Vn0iVgcl0Y_1P7FGbXh7gwACSwADwDZPE9_7IYdUrTDsMwQ')

    bot.reply_to(message, message.sticker.file_id) #отправит нам id стикера

bot.polling()
