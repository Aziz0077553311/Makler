import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import schedule
import time
import threading

# Токен вашего бота
token = '7653124309:AAE2O_kF6ZajJzSaQbwdqDKXYMMeLU5GdKw'
bot = telebot.TeleBot(token)

# ID чата, куда отправлять объявление
CHAT_ID = "7183098167"  # Убрал пробел в начале

# Функция отправки объявления
def send_ad():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("NAVOIY ARZON UYLAR ✅", url='https://t.me/Arzon_uylari'))
    markup.add(InlineKeyboardButton("1 XONALI UYLAR ✅", url='https://t.me/+OAbLerahLHM4NGEy'))
    markup.add(InlineKeyboardButton("2 XONALI UYLAR ✅", url='https://t.me/+0d1ikFWh7Ww1NTYy'))
    markup.add(InlineKeyboardButton("3-4 XONALI UYLAR ✅", url='https://t.me/+FX3nGqvgT64zOGJi'))
    markup.add(InlineKeyboardButton("XOVLILAR ✅", url='https://t.me/+vMyhdyq278FkOTky'))
    markup.add(InlineKeyboardButton("ADMIN ✅", url='https://t.me/Baxtiyor_makler'))
    
    try:
        with open('1.jpg', 'rb') as photo:
            bot.send_photo(CHAT_ID, photo, reply_markup=markup)
    except FileNotFoundError:
        bot.send_message(CHAT_ID, "❌ Файл '1.jpg' не найден!")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    send_ad()  # Вызываем функцию отправки объявления

# Функция для запуска планировщика в отдельном потоке
def run_scheduler():
    # Планируем отправку объявления каждую минуту
    schedule.every(10).minutes.do(send_ad)

    # Бесконечный цикл для проверки расписания
    while True:
        schedule.run_pending()
        time.sleep(1)

# Запуск бота и планировщика
if __name__ == "__main__":
    print("Бот запущен...")

    # Запускаем планировщик в отдельном потоке
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    # Запускаем бота
    bot.polling()