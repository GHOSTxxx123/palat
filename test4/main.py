from telebot import types
import telebot

token = '5437122371:AAGGHwLKXMEWGhm75Un_fIKt6Z7WF4XcFgs'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn1 = types.KeyboardButton("Графический дизайн")
    btn2 = types.KeyboardButton("3D печать")
    btn3 = types.KeyboardButton("3D дизайн")
    btn4 = types.KeyboardButton("Веб технологии")
    markup.add(btn1, btn2, btn3, btn4)

    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}  ✌️</b>\nКакие курсы вас интересують\n<b>1:</b> Графический дизайн\n<b>2:</b> 3D печать\n<b>3:</b> 3D дизайн\n<b>4:</b> Веб технологии\nВыберите что вам нужно"
    
    msg = bot.send_message(message.chat.id, send_mess, parse_mode="html", reply_markup=markup)

    bot.register_next_step_handler(msg, text)

def text(message):
    # Вот лови ссылку на канал:\nhttps://t.me/+bM5Qas5ic9BmYmQy
    if message.text == "Графический дизайн":
        messa = "Ведите пожалуйста\nФ.И"
    # Вот лови ссылку на канал:\nhttps://t.me/+Lbd0OvCqq3tiZmI6
    elif message.text == "3D печать":
        messa = "Ведите пожалуйста\nФ.И"
    # Вот лови ссылку на канал:\nhttps://t.me/+6oSnbbEaVhU1YmMy
    elif message.text == "3D дизайн":
        messa = "Ведите пожалуйста\nФ.И"
    # Вот лови ссылку на канал:\nhttps://t.me/+WOJRR9oCoGhmZDJi
    elif message.text == "Веб технологии":
        messa = "Ведите пожалуйста\nФ.И"

    else:
        messa = "Ты что то пишеш не понятное"

    msg = bot.send_message(message.chat.id, messa)

    bot.register_next_step_handler(msg, emaill)

def emaill(message):
    print(message.text)
    bot.send_message(message.chat.id, "Ведите пожалуйста\nE-mail")
    print(message.text)

@bot.message_handler(content_types='text')
def auth(message):
    print(message.text)
    msg = bot.send_message(message.chat.id, "Тебе отправили ссылку на E-mail веди его")
    bot.register_next_step_handler(msg, cod)

def cod(message):
    if message.text == "0091":
        msg1 = "Вот лови ссылку на канал:\nhttps://t.me/+WOJRR9oCoGhmZDJi"
        bot.send_message(message.chat.id, msg1)

bot.infinity_polling()