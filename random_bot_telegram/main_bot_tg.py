from config import TOKEN_1
import telebot
from telebot import types
import pandas as pd

clasik_data_input = 'clasik_data106.xlsx'
fentasy_data_input = "fentasy_data105_1.xlsx"
roman_data_input = "roman_data107.xlsx"


def choos_random(a):
    excel_data = pd.read_excel(a)
    selected_data = excel_data.sample()
    name_and_about_columns = selected_data[["link","name","about"]]#'reader',, "img" 'reader', 
    return name_and_about_columns


bot = telebot.TeleBot(token=TOKEN_1)

@bot.message_handler(commands=['start'])
def hello(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('Жанры'))
    keyboard.add(types.KeyboardButton('Ответить на вопрос'))
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.text == 'Жанры':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('Фентази'))
        keyboard.add(types.KeyboardButton('Классика'))
        keyboard.add(types.KeyboardButton('Роман'))
        keyboard.add(types.KeyboardButton('Другое'))
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, выбери нужный жанр!', reply_markup=keyboard)

    elif message.text == 'Фентази':
        random_data = choos_random(fentasy_data_input)  # Get new values for random_data
        if len(random_data) > 0:
            audiobook_link = random_data.iloc[0]['link']
            audiobook_name = random_data.iloc[0]["name"]
            audiobook_about = random_data.iloc[0]["about"]
            response_message = f"\n\n{audiobook_name}\n\n{audiobook_about}\n\n{audiobook_link}"
        else:
            response_message = "Нет доступных данных."
        bot.send_message(message.chat.id, response_message)

    elif message.text == 'Классика':
        random_data = choos_random(clasik_data_input)  # Get new values for random_data
        if len(random_data) > 0:
            audiobook_link = random_data.iloc[0]['link']
            audiobook_name = random_data.iloc[0]["name"]
            audiobook_about = random_data.iloc[0]["about"]
            response_message = f"\n\n{audiobook_name}\n\n{audiobook_about}\n\n{audiobook_link}"
        else:
            response_message = "Нет доступных данных."
        bot.send_message(message.chat.id, response_message)

    elif message.text == 'Роман':
        random_data = choos_random(roman_data_input)  # Get new values for random_data
        if len(random_data) > 0:
            audiobook_link = random_data.iloc[0]['link']
            audiobook_name = random_data.iloc[0]["name"]
            audiobook_about = random_data.iloc[0]["about"]
            response_message = f"\n\n{audiobook_name}\n\n{audiobook_about}\n\n{audiobook_link}"
        else:
            response_message = "Нет доступных данных."
        bot.send_message(message.chat.id, response_message)

    elif message.text == 'Другое':
        anser_1 = 'Этот бот который по нажатию \n "Случайная аудиокнига" \n высылает очень интересную аудеокнигу с названием, описанием и изображением обложки.'
        bot.send_message(message.chat.id, anser_1)

    elif message.text == 'Ответить на вопрос':
        anser = 'Это бот который по нажатию \n "Случайная аудиокнига" \n высылает очень интересную аудеокнигу с названием, описанием и изображением обложки.'
        bot.send_message(message.chat.id, anser)

if __name__ == '__main__':
    bot.polling(none_stop=True)